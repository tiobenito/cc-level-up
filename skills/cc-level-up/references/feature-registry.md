# Claude Code Feature Registry

A database of Claude Code features that the audit checks against. Each entry describes what the feature is, where it lives, what good usage looks like, and common gaps to check for.

---

## Core Configuration

### CLAUDE.md (Project Instructions)

- **What:** Markdown files that Claude reads at session start. Provides persistent instructions across conversations.
- **Locations:** Global (`~/.claude/CLAUDE.md`), project root (`CLAUDE.md`), nested in subdirectories, gitignored personal (`.claude/CLAUDE.md`)
- **Good usage:** Layered instructions — global for cross-project rules, project for project-specific context, nested for subdirectory context. Clear structure with headers. Under 200 lines for global, under 150 for project.
- **Common gaps:** Duplicated instructions across files, stale references, broken file pointers, overly long files, no separation between global and project concerns.
- **Audit checks:** File existence, line count, broken pointers, duplication detection, structure quality.

### Project CLAUDE.md

- **What:** A `CLAUDE.md` file in the project root that provides project-specific instructions.
- **Locations:** Project root, also `.claude/CLAUDE.md` for gitignored personal overrides
- **Good usage:** Contains project-specific conventions, tech stack info, testing commands, deployment notes. Does not duplicate global instructions.
- **Common gaps:** Missing entirely, duplicates global CLAUDE.md content, contains stale project info, too long.
- **Audit checks:** Existence, content quality, duplication with global, freshness.

---

## Persistence & Memory

### Memory System (Auto Memory)

- **What:** Persistent notes stored per-project. `MEMORY.md` is auto-loaded (first 200 lines) into the system prompt at session start.
- **Locations:** `~/.claude/projects/<project-path>/memory/MEMORY.md` and topic files in the same directory
- **Good usage:** MEMORY.md under 200 lines acts as an index linking to topic files. Topic files organized by subject (e.g., `patterns.md`, `setup.md`, `lessons.md`). No duplication with CLAUDE.md.
- **Common gaps:** MEMORY.md too long, references files that don't exist, duplicates CLAUDE.md content, stale entries, no topic file organization.
- **Audit checks:** Line count, pointer validity, duplication, staleness, topic file organization.

### Session Continuity (Handover)

- **What:** A mechanism for preserving context between sessions — typically a HANDOVER.md file that records what was done, decisions made, and next steps.
- **Locations:** Project root (`HANDOVER.md`), or custom location referenced in CLAUDE.md
- **Good usage:** Updated at end of each session (ideally via command or hook), covers what was done + decisions + next steps, connects to persistent memory for long-term retention.
- **Common gaps:** No handover mechanism, file exists but is never updated, no automated update trigger, doesn't connect to memory system.
- **Audit checks:** File existence, freshness (days since update), completeness, update mechanism, memory connection.

---

## Automation & Workflows

### Skills

- **What:** Reusable instruction sets that encode complex workflows. Stored as `SKILL.md` files with optional reference documents.
- **Locations:** `~/.claude/skills/<name>/SKILL.md`, with `references/` subdirectory for supporting docs
- **Good usage:** YAML frontmatter with name, description, and trigger phrases. Body under 500 lines. Progressive disclosure via references. Learnings files for skills that have been refined over time.
- **Common gaps:** Missing or vague trigger phrases in description, overly long bodies, no progressive disclosure, missing references files that are mentioned, placeholder skills that were never completed, no learnings captured.
- **Audit checks:** Frontmatter validity, description quality, trigger phrases, line count, reference file existence, learnings files.

### Hooks

- **What:** Shell commands that execute on Claude Code events. Can automate repetitive tasks, enforce rules, and customize behavior.
- **Locations:** `hooks` key in `~/.claude/settings.json` (or plugin hooks.json)
- **Events available:**
  - `PreToolUse` — runs before a tool executes. Can block execution by exiting non-zero. Use for: auto-approval rules, validation gates.
  - `PostToolUse` — runs after a tool completes. Use for: auto-formatting, logging, follow-up actions.
  - `SessionStart` — runs when a session begins. Use for: environment setup, context loading, status display.
  - `Stop` — runs when Claude stops generating. Use for: cleanup, session logging, handover reminders.
  - `Notification` — runs when Claude sends a notification. Use for: routing notifications to Slack, playing sounds, custom alerts.
- **Good usage:** Covers key automation needs without being overly complex. Scripts are tested and handle errors. Async where possible for non-blocking hooks.
- **Common gaps:** No hooks configured, only covers one event type, hooks reference scripts that don't exist, no error handling, blocking hooks that slow down interaction.
- **Audit checks:** Hook count, event type coverage, script existence, async usage, identified missed opportunities.

### Commands (Slash Commands)

- **What:** User-invokable prompts that appear as `/<name>` in Claude Code. Lighter weight than skills.
- **Locations:** `~/.claude/commands/<name>.md`
- **Good usage:** Clear descriptions, focused purpose, uses frontmatter for model selection and tool access. Quick triggers for common actions.
- **Common gaps:** Overlap with skills (doing the same thing), missing descriptions, commands that are too complex (should be skills instead).
- **Audit checks:** Command count, description quality, overlap with skills.

### Custom Agents

- **What:** Specialized agent types that can be used as subagents. Each has defined roles and tool access.
- **Locations:** `~/.claude/agents/<name>.md`
- **Good usage:** Clear role definition, specific tool access, used for specialized perspectives (security review, performance analysis, code review).
- **Common gaps:** No agents defined, agents with unclear roles, agents without tool access restrictions, overlap with skills.
- **Audit checks:** Agent count, role clarity, tool access definition, overlap detection.

---

## External Integrations

### MCP Servers

- **What:** Model Context Protocol servers that give Claude access to external tools and services.
- **Locations:** `~/.claude/.mcp.json` (global), `.mcp.json` (project root)
- **Good usage:** Key services connected (GitHub, project management, docs). Clean configuration with no duplicates. Global config for universal services, project config for project-specific ones.
- **Common gaps:** No MCP servers configured, missing key integrations, duplicate configs between global and project, broken server configurations.
- **Audit checks:** Server count, service coverage, duplicate detection, configuration validity.

### Plugins

- **What:** Installable packages that bundle commands, skills, agents, hooks, and MCP servers into a single unit.
- **Locations:** `enabledPlugins` in `~/.claude/settings.json`
- **Good usage:** Installed for capabilities that benefit from bundled configuration. Kept up to date.
- **Common gaps:** Not aware plugins exist, outdated plugin versions, plugins that overlap with manual configuration.
- **Audit checks:** Plugin count, version freshness, overlap with manual config.

---

## Advanced Features

### Native Tasks (CLAUDE_TASK_ID)

- **What:** Persistent task lists with dependencies that survive conversation compaction.
- **Locations:** `~/.claude/tasks/`
- **Good usage:** Used for multi-step work (3+ tasks), multi-session projects, tasks with dependencies. Started via `CLAUDE_TASK_ID=project-name claude`.
- **Common gaps:** Not using tasks for multi-step work, managing TODO lists manually instead, not aware the feature exists.
- **Audit checks:** Task directory existence, recent task usage, evidence of multi-step work patterns.

### Agent Teams

- **What:** Multiple Claude instances with shared task boards and bidirectional messaging for parallel work.
- **Good usage:** Used for multi-domain work (backend + frontend + tests), parallel investigations, codebase reviews from multiple angles. Each teammate has distinct role and file ownership.
- **Common gaps:** Not using agent teams for work that spans multiple areas, doing parallel work sequentially instead.
- **Audit checks:** Evidence of agent team usage in history, multi-domain work patterns that could benefit.

### Plan Mode

- **What:** Claude explores the codebase and designs an implementation approach before writing code. Cannot edit files in plan mode.
- **Good usage:** Used before non-trivial implementation, when multiple approaches exist, for architecture decisions.
- **Common gaps:** Jumping straight to implementation without planning, not aware plan mode exists.
- **Audit checks:** Evidence of plan mode usage, complexity of recent work (would planning have helped?).

### Status Line

- **What:** Custom status line at the bottom of the terminal showing at-a-glance information.
- **Locations:** `statusLine` in `~/.claude/settings.json`
- **Good usage:** Shows useful context (git branch, project name, task status, active model).
- **Common gaps:** Not configured, shows stale or unhelpful information.
- **Audit checks:** Configuration existence, content usefulness.

### Key Bindings

- **What:** Custom keyboard shortcuts for common actions.
- **Locations:** `~/.claude/keybindings.json`
- **Good usage:** Shortcuts for frequently used commands or modes. Supports chord bindings (multi-key sequences).
- **Common gaps:** No custom keybindings, default keybindings not leveraged.
- **Audit checks:** File existence, binding count, coverage of frequent actions.

---

## Feature Interaction Patterns

Understanding how features work together is as important as using them individually.

```
CLAUDE.md (rules)   --> drives   --> Proactive behavior, agent behavior
Memory (state)      --> informs  --> What to suggest, context across sessions
Skills (logic)      --> powers   --> Complex, repeatable workflows
Commands (trigger)  --> invokes  --> Skills and quick actions
Hooks (automation)  --> handles  --> Repetitive tasks, enforcement, logging
Agent Teams         --> parallelize --> Multi-domain work
Native Tasks        --> track    --> Multi-step projects with dependencies
MCP Servers         --> connect  --> External services and tools
Plugins             --> bundle   --> All of the above into installable packages
Plan Mode           --> designs  --> Implementation before coding
```

### Powerful Combinations

| Pattern | Features Used | When to Use |
|---------|--------------|-------------|
| Automated quality gates | Hooks (PreToolUse) + CLAUDE.md rules | Enforce standards without manual checks |
| Skill + command combo | Skills (logic) + Commands (trigger) | Quick-trigger for complex workflows |
| Memory-informed sessions | Memory + CLAUDE.md + Handover | Seamless context across sessions |
| Parallel investigation | Agent Teams + Native Tasks | Multi-domain debugging or review |
| Progressive disclosure | CLAUDE.md (rules) + Skills (references/) + Memory (topics/) | Keep context budget low, detail available on demand |
| Feature development | Plan Mode + Agent Teams + Native Tasks | Design first, parallelize implementation, track progress |
