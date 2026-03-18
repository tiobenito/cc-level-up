#!/usr/bin/env python3
"""PreToolUse hook: Logs skill invocations to usage-log.jsonl.

Reads tool input from stdin. If tool_name is "Skill", appends a JSON
line to ${CLAUDE_PLUGIN_DATA}/usage-log.jsonl with timestamp, skill
name, and session ID.
"""

import json
import os
import sys
from datetime import datetime, timezone


def main():
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return

        data = json.loads(raw)
        tool_name = data.get("tool_name", "")

        if tool_name != "Skill":
            return

        tool_input = data.get("tool_input", {})
        skill_name = tool_input.get("skill", "unknown")

        plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA", "")
        if not plugin_data:
            return

        os.makedirs(plugin_data, exist_ok=True)
        log_path = os.path.join(plugin_data, "usage-log.jsonl")

        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "skill": skill_name,
            "session": os.environ.get("CLAUDE_SESSION_ID", "unknown"),
        }

        with open(log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    except Exception:
        # Hooks must not break the user's session
        pass


if __name__ == "__main__":
    main()
