---
name: cc-level-up
description: >
  Guided progression tool for improving your Claude Code setup. Detects your
  current level, explains what you can do next, and builds it for you. Works for
  both Cowork (Projects UI) and CLI users. Use when user says "level up my setup",
  "what should I improve", "help me set up Claude", "how do I get better at Claude",
  "improve my Claude Code", "I'm new to Claude Code", or "set up my project".
  Do NOT trigger for improving code quality, debugging help, or general coding questions.
---

# CC Level-Up

Help the user improve their Claude Code setup one step at a time. Detect where they are, explain what's possible, and build it for them.

## References

- `references/level-guide.md` — Full progression path with level descriptions and detection criteria
- `references/org-context-template.md` — Template for org-specific personalization (optional)
- `references/templates/claude-md-starter.md` — CLAUDE.md creation guide + template
- `references/templates/skill-starter.md` — Skill creation guide + template

## State

- **User state:** `${CLAUDE_PLUGIN_DATA}/user-state.json` — Persistent state across runs (level, history, what was built)
- **Backlog:** `${CLAUDE_PLUGIN_DATA}/backlog.md` — What the user is already tracking (read-only, never modify)

Read user state at the start of every run. Write updated state at the end.

## Tone

Friendly, encouraging, conversational. You are a helpful colleague, not an auditor. Teach real terms (CLAUDE.md, skill, reference doc, hook, MCP server) but always explain them in plain language first. Never use jargon without a one-sentence explanation.

## Platform Detection

Before doing anything else, determine whether the user is on **Cowork** (claude.ai Projects UI) or **CLI** (Claude Code terminal). Use these signals:

| Signal | Cowork | CLI |
|--------|--------|-----|
| Working directory | Cloud project folder | Local filesystem (`~/`, repo path) |
| CLAUDE.md location | Project root in cloud | Repo root or `~/.claude/` |
| Skills folder | `skills/` in project | `.claude/skills/` or `~/.claude/skills/` |
| Hooks config | N/A | `.claude/settings.json` or `~/.claude/settings.json` |
| MCP servers | N/A | Settings or `mcp.json` |
| Git repo | No | Often yes |
| `CLAUDE_PLUGIN_DATA` env var | May not exist | Usually set by plugin |

### Adjusting for Platform

**Cowork users:**
- Say "project instructions" in casual language (use "CLAUDE.md" only when creating the file)
- Do not mention hooks, MCP servers, auto-memory, or agents until Level 3+
- Skills live in `skills/` folder at the project root
- Reference docs live in `reference/` folder at the project root
- Focus on file organization within the project

**CLI users:**
- Use standard CLI terminology (CLAUDE.md, hooks, MCP, settings.json)
- Can mention hooks and MCP servers from Level 2 onward
- Skills may live in `~/.claude/skills/` (global) or `.claude/skills/` (project)
- Can leverage git, local tooling, and filesystem
- Focus on development workflow integration

## Performance Notes

- Max 2-3 recommendations per run. Do not overwhelm.
- Take your time on detection — read files, do not guess from names.
- Always show what you built before moving to the next thing.
- The user may not know what a "skill" is yet. Explain before asking if they want one.

---

## Step 1: Detect

Scan the user's setup to determine their current level. Do this silently — do not narrate every file you're reading.

### Read State First

1. Read `${CLAUDE_PLUGIN_DATA}/user-state.json` if it exists. It contains:
   ```json
   {
     "last_run_date": "2025-03-15",
     "level": 2,
     "level_name": "Established",
     "platform": "cli",
     "items_built": [
       {"date": "2025-03-01", "type": "claude-md", "path": "CLAUDE.md"},
       {"date": "2025-03-15", "type": "skill", "path": ".claude/skills/format-report/SKILL.md"}
     ],
     "recommendations_history": [
       {"date": "2025-03-01", "title": "Create CLAUDE.md", "status": "accepted"},
       {"date": "2025-03-15", "title": "Add behavioral rules", "status": "declined"}
     ],
     "next_suggested_run": "2025-04-01"
   }
   ```
2. Read `${CLAUDE_PLUGIN_DATA}/backlog.md` if it exists — note what the user is already tracking so you do not duplicate suggestions.

### What to Scan

| What | Where (Cowork) | Where (CLI) | What it tells you |
|------|----------------|-------------|-------------------|
| CLAUDE.md | Project root | Repo root, `~/.claude/CLAUDE.md` | Exists? How many lines? Has behavioral rules? |
| Skills | `skills/` | `.claude/skills/`, `~/.claude/skills/` | Count. Have frontmatter? Have references? |
| Reference docs | `reference/` | `reference/`, `.claude/` | Exists? How many docs? |
| Hooks | N/A | `.claude/settings.json` hooks section | Any configured? |
| MCP servers | N/A | `.claude/settings.json` mcpServers, `mcp.json` | Any configured? |
| Memory system | N/A | `MEMORY.md`, `.claude/memory/` | Auto-memory active? Topic files? |
| Git integration | N/A | `.git/` | Is this a git repo? |
| Subfolder CLAUDE.md | Subdirectories | Subdirectories | Any scoped instructions? |
| Folder organization | Project root | Project root | Beyond defaults? |

Use Glob and Read tools. Record findings internally.

### Level Assignment

Assign the highest level where ALL criteria are met. Refer to `references/level-guide.md` for the full guide, but here is the summary:

**Level 0 — Getting Started**
- No CLAUDE.md (or under 5 lines)
- 0-1 skills
- Fresh install or minimal setup

**Level 1 — Foundation**
- Has a CLAUDE.md with at least a role/project description (5+ lines)
- 2-3 skills with basic structure

**Level 2 — Established**
- CLAUDE.md has behavioral rules (15+ lines with "always/never" instructions, format preferences, or workflow rules)
- Reference folder with 2+ docs
- 4+ skills
- CLI: May have basic hooks or 1 MCP server

**Level 3 — Power User**
- Well-organized folder structure
- Skills have their own reference files or output templates
- 6+ skills with good structure
- CLI: Hooks configured + MCP servers + custom commands or agents
- Cowork: Subfolder CLAUDE.md files, session notes workflow

**Level 4 — Expert**
- Complete, well-organized system
- Demonstrates system thinking (files reference each other, clear separation of concerns)
- CLI: Learnings loop (learnings.md files), scoring checklists, optimized context loading, plugin-level organization
- Cowork: Mature system with advanced skill patterns, cross-referencing, maintenance habits

---

## Step 2: Present

Show the user their level and what is next. Keep it warm and concise.

### Format

Start with a greeting and their level:

> **Your setup: [Level Name]** (Level [N] of 4)
>
> [One sentence about what this level means — from level-guide.md]

If this is a returning user (user-state.json has previous data), celebrate progress:

> Since last time: [what changed — new skills added, CLAUDE.md grew, new hooks configured]

Then show 2-3 recommendations as cards:

> **Here's what I'd suggest next:**
>
> **1. [Title]**
> [2-sentence plain-language description of what this is and why it helps]
>
> **2. [Title]**
> [2-sentence plain-language description]
>
> **3. [Title]** *(optional — only if relevant)*
> [2-sentence plain-language description]
>
> Which of these sounds useful? I can set any of them up for you right now.

### What to Recommend at Each Level

Recommendations differ by platform. Always check the backlog to avoid suggesting things the user is already tracking.

#### Level 0

**Both platforms:**
1. Create your project instructions (CLAUDE.md) — "This is a file that tells Claude who you are and how you like to work. It loads automatically every time you start a conversation."
2. Build your first skill — "A skill is a reusable instruction set for a task you do repeatedly. Instead of explaining what you want every time, you just say 'use my [skill name]'."

#### Level 1

**Both platforms:**
1. Start a reference library — "A reference folder is where you put docs Claude can look up — templates, glossaries, lists. Claude reads them when it needs context, so you don't have to paste them every time."
2. Add behavioral rules to your CLAUDE.md — "These are standing instructions like 'always use bullet points' or 'never round dollar amounts'. They shape every conversation without you having to repeat yourself."
3. Build another skill — "You've got [N] skills. Based on what you do, [suggested skill] could save you time."

#### Level 2

**Cowork:**
1. Refine your skills — add output templates, split multi-purpose skills
2. Organize with subfolder instructions
3. Add output templates to skills

**CLI:**
1. Set up a hook — "Hooks are scripts that run automatically before or after Claude does something. For example, auto-formatting code before every commit."
2. Connect an MCP server — "MCP servers let Claude talk to your tools directly — GitHub, Slack, databases, whatever you use."
3. Refine your skills — better structure, output templates, reference files

#### Level 3

**Cowork:**
1. Session notes habit — keep continuity between conversations
2. Advanced skill patterns — skills that reference other files, chain together
3. System maintenance — periodic review of stale content

**CLI:**
1. Set up auto-memory — "Auto-memory means Claude remembers patterns and lessons across sessions without you having to repeat them."
2. Custom commands or agents — "You can define custom slash commands or agents that specialize in specific tasks."
3. Learnings loop — "Add learnings.md files next to your skills so Claude gets better at running them over time."

#### Level 4

**Cowork:**
1. Consider CLI — "There's a whole other level. Claude Code CLI gives you hooks, persistent memory, MCP servers, and agent teams. It's a bigger learning curve, but the payoff is huge."

**CLI:**
1. Context optimization — "Review how your CLAUDE.md and skills load. Are you loading too much? Too little? Optimize for what actually helps."
2. Scoring checklists — "Create checklists that score output quality. Skills can self-evaluate against criteria you define."
3. Plugin-level organization — "Package your setup so others can use it. Skills, hooks, and configuration as a shareable unit."

---

## Step 3: Build

For each recommendation the user accepts, follow the **Explain + Build** pattern.

### The Pattern

1. **Ask** 2-4 personalizing questions relevant to what you're building
   - Read the relevant template from `references/templates/` for question ideas
   - If the org has a context file at `references/org-context-template.md`, read it for role-specific suggestions
2. **Explain** what you are about to create (1-2 sentences, plain language)
3. **Build** the file(s)
4. **Show** a summary of what was created (quote key parts, not the whole file)
5. **Explain** how it changes their experience going forward (1-2 sentences)

### Critical Rules

- **Never overwrite an existing CLAUDE.md.** Read it first. Add to it, or ask before replacing content.
- **Never overwrite existing skills.** Suggest improvements or create new ones alongside.
- **Always show what you created** before moving to the next recommendation. Do not batch-create silently.
- **Use the user's own words** from their answers when writing content. Do not over-polish into corporate speak.
- **Keep skills simple.** First skills should be 15-30 lines, not 100-line masterpieces.
- **Keep CLAUDE.md minimal.** Start with 10-15 lines. Users can always add more. Resist the urge to front-load.
- **Explain file locations.** Tell the user where the file lives and why it's there.
- **Respect the platform.** Create files in the right locations for Cowork vs CLI.

### Building a CLAUDE.md (Level 0)

1. Ask: role/project, primary use case, any format preferences
2. Read `references/templates/claude-md-starter.md` for the template
3. Create the file at the appropriate location
4. Show what you wrote, explain that it loads automatically every session

### Building a Skill (Level 0-1)

1. Ask: what task to speed up, how they do it now, what good output looks like
2. Read `references/templates/skill-starter.md` for structure
3. Create the skill folder and SKILL.md in the right location for their platform
4. Show the skill, explain how to invoke it

### Building a Reference Library (Level 1)

1. Ask: what docs they reference often, what they wish Claude already knew
2. Create `reference/` folder and 2-3 starter docs
3. Show what was created, explain that Claude reads these when relevant

### Setting Up Hooks (Level 2, CLI only)

1. Ask: what repetitive step happens before/after Claude actions
2. Explain hooks in plain language: "A hook is a script that runs automatically at a certain point — like auto-formatting code after Claude writes it."
3. Add the hook to `.claude/settings.json`
4. Show the configuration, explain when it fires

### Setting Up MCP (Level 2-3, CLI only)

1. Ask: what tools they use daily (GitHub, Slack, databases, etc.)
2. Explain MCP: "MCP servers let Claude talk directly to your tools instead of you copy-pasting between them."
3. Help configure the server in settings
4. Show the configuration, explain what Claude can now do

### Refining Skills (Level 2+)

1. Read existing skills to identify improvement opportunities
2. Suggest specific changes: add output templates, split multi-purpose skills, add reference files
3. Ask before making changes — explain what you would change and why
4. Make the edits, show the diff

### Adding Behavioral Rules (Level 1-2)

1. Ask: things they always want, things they never want, format preferences
2. Read existing CLAUDE.md
3. Add a "How I Like Things" or "Rules" section
4. Show what was added

---

## Step 4: Save State

After building everything the user requested, update `${CLAUDE_PLUGIN_DATA}/user-state.json`.

### What to Save

```json
{
  "last_run_date": "[today's date]",
  "level": "[N]",
  "level_name": "[Level Name]",
  "previous_level": "[N from last run, or null if first run]",
  "platform": "[cowork or cli]",
  "items_built": [
    "...previous items...",
    {"date": "[today]", "type": "[claude-md|skill|reference|hook|mcp|other]", "path": "[filepath]", "description": "[one line]"}
  ],
  "recommendations_history": [
    "...previous entries...",
    {"date": "[today]", "title": "[recommendation title]", "status": "[accepted|declined|skipped]"}
  ],
  "next_suggested_run": "[date 2-4 weeks from now]"
}
```

### Closing Message

End with something encouraging and forward-looking:

> That's it for now! You're at **[Level Name]** with [brief summary of what they have]. Use what we built for a couple weeks, and when you're ready for more, just say "level up" again.

If the user has a backlog, mention it:

> I noticed you're already tracking some things in your backlog — [brief mention]. Those are great next steps too.
