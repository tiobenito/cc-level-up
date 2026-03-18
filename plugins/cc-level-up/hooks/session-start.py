#!/usr/bin/env python3
"""SessionStart hook: Nudges users about stale backlog items and overdue audits.

Checks ${CLAUDE_PLUGIN_DATA}/backlog.md for items with status 'ready'
or 'trying' that have been sitting for 2+ weeks. Also checks
${CLAUDE_PLUGIN_DATA}/last-audit.json for audit staleness (30+ days).
Outputs nothing if there is nothing to report.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta


def parse_backlog_for_stale_items(backlog_path):
    """Find ready/trying items that are 2+ weeks old."""
    if not os.path.isfile(backlog_path):
        return []

    try:
        with open(backlog_path, "r") as f:
            content = f.read()
    except Exception:
        return []

    stale = []
    now = datetime.now(timezone.utc)
    two_weeks_ago = now - timedelta(weeks=2)

    # Match table rows: | name | status | ... | date | ...
    # Common formats:
    #   | Feature Name | ready | ... | 2025-12-01 | ... |
    #   | Feature Name | trying | ... | 2025-12-01 | ... |
    # We look for rows containing 'ready' or 'trying' and extract a date.
    for line in content.splitlines():
        line_stripped = line.strip()
        if not line_stripped.startswith("|"):
            continue

        cells = [c.strip() for c in line_stripped.split("|")]
        # cells[0] and cells[-1] are empty strings from leading/trailing pipes
        cells = [c for c in cells if c]

        if len(cells) < 2:
            continue

        # Check if any cell contains 'ready' or 'trying' (case-insensitive)
        status_match = None
        for cell in cells:
            lower = cell.lower().strip()
            if lower in ("ready", "trying"):
                status_match = lower
                break

        if not status_match:
            continue

        # Try to find a date in any cell (YYYY-MM-DD format)
        date_found = None
        for cell in cells:
            date_match = re.search(r"(\d{4}-\d{2}-\d{2})", cell)
            if date_match:
                try:
                    date_found = datetime.strptime(
                        date_match.group(1), "%Y-%m-%d"
                    ).replace(tzinfo=timezone.utc)
                except ValueError:
                    continue
                break

        if date_found and date_found < two_weeks_ago:
            # First non-status, non-date cell is likely the feature name
            name = cells[0] if cells[0].lower().strip() not in ("ready", "trying") else "unnamed"
            stale.append(name)

    return stale


def check_audit_staleness(audit_path):
    """Check if last audit was 30+ days ago. Returns days since audit or None."""
    if not os.path.isfile(audit_path):
        return None

    try:
        with open(audit_path, "r") as f:
            data = json.load(f)
    except Exception:
        return None

    last_audit_str = data.get("last_audit") or data.get("timestamp") or data.get("date")
    if not last_audit_str:
        return None

    try:
        # Try ISO format first
        last_audit = datetime.fromisoformat(last_audit_str.replace("Z", "+00:00"))
        if last_audit.tzinfo is None:
            last_audit = last_audit.replace(tzinfo=timezone.utc)
    except (ValueError, AttributeError):
        # Try YYYY-MM-DD
        try:
            last_audit = datetime.strptime(last_audit_str[:10], "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )
        except (ValueError, AttributeError):
            return None

    now = datetime.now(timezone.utc)
    days_since = (now - last_audit).days

    if days_since >= 30:
        return days_since

    return None


def main():
    plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA", "")
    if not plugin_data:
        return

    messages = []

    # Check backlog for stale items
    backlog_path = os.path.join(plugin_data, "backlog.md")
    stale_items = parse_backlog_for_stale_items(backlog_path)
    if stale_items:
        names = ", ".join(stale_items)
        count = len(stale_items)
        messages.append(
            f'CC LEVEL-UP: {count} feature(s) ready but untouched for 2+ weeks: {names}. '
            f'Say "show my backlog" or "what should I work on next" for details.'
        )

    # Check audit staleness
    audit_path = os.path.join(plugin_data, "last-audit.json")
    days_since = check_audit_staleness(audit_path)
    if days_since is not None:
        messages.append(
            f"It's been {days_since} days since your last setup audit. Try /cc-level-up."
        )

    if messages:
        print("\n".join(messages))


if __name__ == "__main__":
    main()
