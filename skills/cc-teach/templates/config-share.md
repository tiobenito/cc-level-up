# Claude Code Configuration Guide

> Generated from a proven setup. Follow these steps to replicate.

## Prerequisites
- Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- API key configured

## Global Configuration

### Settings (`~/.claude/settings.json`)

```json
{
  "permissions": {
    "allow": [
      // RECOMMENDED: Read-only tools always allowed
      "Read(**)",
      "Glob(**)",
      "Grep(**)",
      "WebSearch",
      // Add your project-specific permissions
    ],
    "deny": [
      // RECOMMENDED: Always deny sensitive files
      "Read(.env)",
      "Read(.env.*)",
      "Read(~/.aws/**)",
      "Read(~/.ssh/**)"
    ]
  }
}
```

**Why these permissions?** [EXPLANATION]

### Hooks

[HOOK_CONFIGS with explanations]

### MCP Servers

[MCP_CONFIGS with explanations of each server and what it enables]

### Plugins

[PLUGIN_LIST with descriptions]

## Project Configuration

### CLAUDE.md Template

```markdown
# [Project Name]

## Overview
[One paragraph about what this project does]

## Architecture
[Key directories and their purposes]

## Development
- Build: `[command]`
- Test: `[command]`
- Lint: `[command]`

## Conventions
[Team code conventions Claude should follow]
```

### Project MCP Servers (`.mcp.json`)

[PROJECT_SPECIFIC_MCP_CONFIGS]

## Recommended Skills

[LIST_OF_SKILLS with install/setup instructions]

## Customization Notes

[WHAT_TO_CHANGE for your specific setup — paths, API keys, team conventions]
