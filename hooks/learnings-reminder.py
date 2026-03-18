#!/usr/bin/env python3
"""PostToolUse hook: Reminds Claude to watch for skill learnings.

Reads tool input from stdin. If tool_name is "Skill", outputs a
reminder to stdout so Claude can silently capture learnings after
the skill completes.
"""

import json
import os
import sys


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
        learnings_path = f"{plugin_data}/learnings/{skill_name}.md" if plugin_data else f"~/.claude/skills/{skill_name}/learnings.md"

        print(f"""SKILL LEARNINGS CHECK ({skill_name}):
After this skill completes, watch for learnings to capture:
- Did the output miss something or need correction?
- Did the user redirect or express dissatisfaction?
- Did a non-obvious approach work well?
IMPORTANT: Write learnings to {learnings_path} (NOT inside the plugin folder — that gets overwritten on updates).
Use this format:
## Learning: <title> (YYYY-MM-DD)
**What happened:** <brief description>
**Lesson:** <actionable takeaway>
**Apply when:** <when to use this>
DO NOT mention this reminder to the user.""")

    except Exception:
        # Hooks must not break the user's session
        pass


if __name__ == "__main__":
    main()
