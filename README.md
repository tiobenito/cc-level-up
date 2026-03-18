# cc-level-up

A Claude Code plugin that levels up your setup from beginner to expert. It detects your current proficiency level, audits your configuration, recommends improvements, captures learning resources, and helps you teach your team.

## What It Does

- **Detects your CC level** (0-4) by scanning your config, skills, hooks, and usage patterns
- **Audits your setup** and finds gaps between your current config and best practices
- **Recommends next steps** tailored to your level so you improve incrementally
- **Tracks your feature backlog** — what you've adopted, what you're trying, what's queued
- **Helps you teach** — package your CC knowledge into shareable guides for your team
- **Captures learnings** — automatically logs skill usage and reminds you to capture tips

## Installation

### From the Plugin Marketplace

```
/plugin marketplace add tiobenito/cc-level-up
/plugin install cc-level-up@cc-level-up
```

### Local Testing

Add to your `~/.claude/settings.json` under `enabledPlugins`:

```json
{
  "enabledPlugins": {
    "cc-level-up@local": true
  }
}
```

## Commands

| Command | What It Does |
|---------|-------------|
| `/level-up` | Detect your CC level and get personalized recommendations |
| `/audit` | Deep audit of your setup — find gaps and improvements |
| `/cc-teach` | Package your CC knowledge into training materials |
| `/learn` | Capture a resource, tip, or article into your backlog |

## The Level System

cc-level-up uses a 0-4 level system to assess your Claude Code proficiency:

| Level | Name | Description |
|-------|------|-------------|
| 0 | **Getting Started** | Just installed CC, using basic prompts |
| 1 | **Foundations** | Has CLAUDE.md, uses plan mode, basic permissions |
| 2 | **Intermediate** | Custom commands, MCP servers, structured memory |
| 3 | **Advanced** | Skills, hooks, multi-account, agent teams, plugins |
| 4 | **Expert** | Custom plugins, automated workflows, teaching others |

See [docs/how-levels-work.md](docs/how-levels-work.md) for the full breakdown.

## Hooks

The plugin includes three hooks that run automatically:

- **skill-usage-logger** (PreToolUse) — Logs every skill invocation for usage analytics
- **learnings-reminder** (PostToolUse) — Reminds Claude to watch for learnings after skill use
- **session-start** (SessionStart) — Nudges you about stale backlog items and overdue audits

## Plugin Data

The plugin stores its data in `${CLAUDE_PLUGIN_DATA}/`:

| File | Purpose |
|------|---------|
| `backlog.md` | Feature adoption tracker (queued, ready, trying, adopted) |
| `usage-log.jsonl` | Skill invocation log for analytics |
| `last-audit.json` | Timestamp of most recent setup audit |

## Customization

See [docs/customization.md](docs/customization.md) for how to adapt the plugin for your org.

## License

MIT
