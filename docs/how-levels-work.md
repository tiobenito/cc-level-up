# How the Level System Works

cc-level-up assigns you a level from 0 to 4 based on which Claude Code features you have configured and actively use. The goal is not gamification for its own sake — it is a diagnostic tool that tells you where you are and what to try next.

## The Levels

### Level 0 — Getting Started

You have Claude Code installed and can run it, but you have not customized anything yet.

**Detection signals:**
- No `CLAUDE.md` in any project
- Default `settings.json` (no custom permissions)
- No MCP servers configured
- No custom commands, skills, or hooks

**What you should do next:**
- Create a `CLAUDE.md` in your most-used project
- Add basic permission rules to `settings.json`
- Try plan mode on a non-trivial task

### Level 1 — Foundations

You have the basics in place. Claude knows about your project and has sensible permissions.

**Detection signals:**
- At least one project has a `CLAUDE.md`
- `settings.json` has custom allow/deny rules
- You use plan mode occasionally
- You may have tried a slash command or two

**What you should do next:**
- Create custom commands for repeated workflows
- Set up at least one MCP server (GitHub is a good start)
- Build a structured memory system (global `CLAUDE.md` with project-specific files)
- Try `CLAUDE_TASK_ID` for a multi-step project

### Level 2 — Intermediate

You have a productive setup with project-specific configs, external tool integrations, and workflows that go beyond basic prompting.

**Detection signals:**
- Custom commands exist (`~/.claude/commands/` or project-level)
- At least one MCP server configured (`.mcp.json`)
- Structured CLAUDE.md with sections (not just a paragraph)
- Uses native tasks or plan mode regularly
- Has a global `~/.claude/CLAUDE.md`

**What you should do next:**
- Create your first custom skill
- Set up hooks for automation (linting, formatting, logging)
- Try agent teams for a multi-domain task
- Install a plugin or build one
- Set up multi-account if you have work + personal

### Level 3 — Advanced

You have a sophisticated setup with custom automation, reusable skills, and you are pushing Claude Code's capabilities.

**Detection signals:**
- Custom skills defined (personal or via plugins)
- Hooks configured (PreToolUse, PostToolUse, or SessionStart)
- Uses agent teams or has experience with them
- Multiple MCP servers or multi-account setup
- Plugins installed or in development
- Memory system with multiple layers (global, project, daily)

**What you should do next:**
- Build and publish a custom plugin
- Automate your entire development workflow end-to-end
- Create teaching materials for your team
- Contribute patterns to the community
- Optimize hook chains and skill interactions

### Level 4 — Expert

You are at the frontier. You build tools for others, contribute to the ecosystem, and your setup is a reference implementation.

**Detection signals:**
- Has published or maintains a plugin
- Creates training materials for others
- Automated workflows that span multiple tools and sessions
- Contributes to CC community (patterns, plugins, guides)
- Setup serves as a reference for others on the team

**What to focus on:**
- Stay current with new CC releases and features
- Mentor others and refine teaching materials
- Push the boundaries — find new patterns and share them
- Build org-wide standards based on your experience

## How Detection Works

When you run `/cc-level-up`, the plugin scans:

1. **File system** — checks for the existence and content of:
   - `~/.claude/CLAUDE.md` (global instructions)
   - `~/.claude/settings.json` (permissions, hooks, plugins)
   - `~/.claude/commands/` (custom commands)
   - `~/.claude/skills/` (custom skills)
   - `.mcp.json` files (MCP server configs)
   - Project-level `CLAUDE.md` files

2. **Configuration depth** — not just "does it exist" but "is it substantive":
   - A one-line CLAUDE.md counts less than a structured one with sections
   - Default permissions count less than carefully tuned allow/deny rules
   - A single MCP server counts less than multiple integrated servers

3. **Plugin data** — reads from `${CLAUDE_PLUGIN_DATA}/`:
   - `backlog.md` for feature adoption history
   - `usage-log.jsonl` for skill usage patterns
   - `last-audit.json` for audit history

4. **Scoring** — each signal contributes points. The total maps to a level:
   - 0-5 points: Level 0
   - 6-15 points: Level 1
   - 16-30 points: Level 2
   - 31-50 points: Level 3
   - 51+ points: Level 4

   Point values are weighted: foundational features (CLAUDE.md, permissions) are worth less than advanced features (skills, hooks, plugins) because the goal is to reward depth, not just breadth.

## Recommendations

At each level, the plugin generates specific, actionable recommendations. These are not generic advice — they are based on what is missing from your actual setup.

For example, if you are Level 2 and have MCP servers but no hooks, the recommendation will be: "You have external tool integrations but no automation hooks. Try adding a PreToolUse hook for [specific suggestion based on your MCP servers]."

Recommendations are ordered by impact: the plugin suggests the change that will give you the biggest productivity gain first.

## Progression

There is no pressure to reach Level 4. Each level represents a real jump in how effectively you use Claude Code. Many productive users sit comfortably at Level 2 or 3.

The plugin will periodically remind you about features you have marked as "ready" but haven't tried yet. You can dismiss these or act on them at your own pace.
