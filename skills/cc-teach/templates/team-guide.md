# Claude Code Team Guide

> Generated with the cc-teach skill. Customize for your team.

## What is Claude Code?

Claude Code is Anthropic's CLI tool that brings Claude directly into your terminal. It can read your codebase, edit files, run commands, and work alongside you on software engineering tasks.

## Getting Started

### Installation
```bash
npm install -g @anthropic-ai/claude-code
```

### First Run
```bash
cd your-project
claude
```

Claude will read any `CLAUDE.md` files in your project for context and instructions.

### Key Concepts

| Concept | What It Does | How to Use |
|---------|-------------|------------|
| CLAUDE.md | Project instructions Claude reads every session | Create at project root |
| Commands | Quick-trigger actions via `/command-name` | Type `/` to see available |
| Skills | Reusable workflow instructions | Claude uses automatically when relevant |
| Plan Mode | Claude researches before coding | Say "plan this first" |
| Subagents | Parallel worker instances | Claude spawns these automatically |

## Recommended Setup

### 1. Project CLAUDE.md
Create a `CLAUDE.md` in your project root with:
- Project overview and architecture
- Code conventions and patterns
- Common commands (build, test, deploy)
- Team-specific rules

### 2. Global Settings
Your `~/.claude/settings.json` controls permissions, hooks, and plugins.

### 3. MCP Servers
Connect external tools (GitHub, Linear, etc.) via `.mcp.json`.

## Team Conventions

<!-- CUSTOMIZE: Add your team's specific conventions -->

### Code Review with Claude
- Use plan mode for complex changes
- Have Claude explain its approach before implementing

### Working with Tasks
- For multi-step work: `CLAUDE_TASK_ID=project-name claude`
- Track progress across sessions

### When to Use What

```
Simple question or quick fix  -> Just ask Claude directly
Multi-step feature            -> Use native tasks
Multi-domain work             -> Ask for agent teams
Repeated workflow             -> Ask Claude to make it a skill
```

## Tips from the Team

<!-- CUSTOMIZE: Add tips your team has discovered -->

1. **Read before edit**: Always let Claude read files before suggesting changes
2. **Be specific**: "Fix the auth bug in login.ts" > "Fix the bug"
3. **Use plan mode**: For anything non-trivial, plan first
4. **Check the commands**: Type `/` to see available slash commands

## Resources
- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
