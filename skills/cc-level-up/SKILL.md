---
name: cc-level-up
description: >
  Comprehensive setup audit, grading, and guided improvement for your Claude Code
  configuration. Scans 8 areas (CLAUDE.md, Memory & Continuity, Skills, Hooks, MCP,
  Commands & Agents, Folder Structure & Scope, Context Budget), grades each A-F,
  determines your level (0-4), and recommends 2-3 improvements tailored to your level.
  Builds files/config for you if you accept. Works for both Cowork (Projects UI) and
  CLI users. Triggers: "level up my setup", "what should I improve", "help me set up
  Claude", "how do I get better at Claude", "improve my Claude Code", "I'm new to
  Claude Code", "set up my project", "audit my setup", "check my CC config", "how's my
  system", "review my Claude Code", "system health check", "score my setup", "grade my
  setup". Do NOT trigger for auditing code, security audits, reviewing application
  logic, improving code quality, debugging help, or general coding questions.
---

# CC Level-Up

Audit your Claude Code setup, grade every area, determine your level, and help you improve one step at a time.

## References

- `references/level-guide.md` — Full progression path with level descriptions and detection criteria
- `references/scoring-rubric.md` — Detailed grading criteria for each audit area, with level mappings
- `references/feature-registry.md` — Database of CC features the audit checks against
- `references/org-context-template.md` — Template for org-specific personalization (optional)
- `references/templates/claude-md-starter.md` — CLAUDE.md creation guide + template
- `references/templates/skill-starter.md` — Skill creation guide + template

Read `references/scoring-rubric.md` before starting — it defines what "good" looks like for each area.

## State

- **User state:** `${CLAUDE_PLUGIN_DATA}/user-state.json` — Persistent state across runs (level, grades, history, what was built)
- **Backlog:** `${CLAUDE_PLUGIN_DATA}/backlog.md` — What the user is already tracking (managed by /cc-learn)
- **Audit history:** `${CLAUDE_PLUGIN_DATA}/audit-history/` — Historical audit snapshots
- **Last audit:** `${CLAUDE_PLUGIN_DATA}/last-audit.json` — Most recent audit scores for comparison

Read user state and last audit at the start of every run. Write updated state at the end.

## Tone

Friendly, encouraging, conversational. You are a helpful colleague, not a harsh auditor. Teach real terms (CLAUDE.md, skill, reference doc, hook, MCP server) but always explain them in plain language first. Never use jargon without a one-sentence explanation.

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

- Take your time. Thoroughness matters more than speed.
- Read every file you audit — do not skip or summarize from file names alone.
- Do not skip any audit area. If nothing is found, score it and note the gap.
- Max 2-3 recommendations per run. Do not overwhelm.
- Always show what you built before moving to the next thing.
- The user may not know what a "skill" is yet. Explain before asking if they want one.

---

## Step 1: Scan

Scan the environment to build a complete inventory of what exists. Do not assume any specific structure — discover it.

### Load Context First

1. Read `${CLAUDE_PLUGIN_DATA}/user-state.json` if it exists — note previous level, grades, and history
2. Read `${CLAUDE_PLUGIN_DATA}/last-audit.json` if it exists — for comparison with previous scores
3. If `${CLAUDE_PLUGIN_DATA}/backlog.md` exists:
   - Read the **Active Backlog** section — note items by status (`queued`, `ready`, `trying`)
   - Read the **Adopted** table — know what's already working
   - Read the **Health Metrics** section — check previous audit data if present
   - Keep this context in mind: if a finding overlaps with a backlog item, note that it's already being tracked rather than treating it as a new discovery

### Locations to Scan

| What | Where to look |
|------|---------------|
| Global instructions | `~/.claude/CLAUDE.md` |
| Global settings | `~/.claude/settings.json` |
| Global keybindings | `~/.claude/keybindings.json` |
| Global MCP config | `~/.claude/.mcp.json` |
| Skills | `~/.claude/skills/*/SKILL.md` |
| Agents | `~/.claude/agents/*.md` |
| Commands | `~/.claude/commands/*.md` |
| Plugins | `enabledPlugins` in `~/.claude/settings.json` |
| Project instructions | `CLAUDE.md` in project root and subdirectories |
| Project MCP config | `.mcp.json` in project root |
| Auto-memory | `~/.claude/projects/*/memory/` (search all project dirs) |
| Handover files | `HANDOVER.md` or similar in project root |
| Hooks | `hooks` key in `~/.claude/settings.json` |

Use Glob and Read tools to discover files. Record what exists and what doesn't. Do this silently — do not narrate every file you're reading.

### Audit Each Area

For each area below, evaluate what was found during discovery. Assign a letter grade (A/B/C/D/F) using the criteria in `references/scoring-rubric.md`. If an area has no files at all, grade it F or N/A and recommend setup.

#### Area 1: CLAUDE.md Files

Evaluate all CLAUDE.md files (global + project + nested).

**Check for:**
- Clear structure with headers and sections
- Accurate, non-stale content (references to files/tools that still exist)
- No broken pointers (paths that don't resolve)
- Appropriate length (global: under 200 lines preferred; project: under 150 lines)
- No duplication across files (same instructions in multiple places)
- Separation of concerns (global = cross-project rules, project = project-specific)

#### Area 2: Memory & Session Continuity

Audit the full persistence system: auto-memory, topic files, and any session continuity mechanisms (handover files, etc.).

**Memory checks:**
- MEMORY.md exists and is under 200 lines (auto-loaded limit)
- Index references actual topic files that exist
- Topic files are organized by subject, not chronologically
- No duplication between memory files and CLAUDE.md files
- Staleness — content that references outdated dates, completed projects, or obsolete tools
- Information is routed to the right layer (rules in CLAUDE.md, state in memory)

**Session continuity checks (if handover/session mechanism exists):**
- Handover file freshness (check the date if present)
- Completeness (does it cover: what was done, decisions, next steps?)
- Update mechanism (is there a command or trigger to update it?)
- Connection to memory (does the handover feed into persistent memory, not just sit on its own?)

If no session continuity mechanism exists, note the gap but do not penalize heavily — it's an advanced pattern, not a requirement.

#### Area 3: Skills

Inventory all skills in `~/.claude/skills/`.

**Check for:**
- Each skill has a valid SKILL.md with YAML frontmatter
- Description includes BOTH what it does AND trigger phrases
- No skill name uses spaces, capitals, or underscores
- Body is under 500 lines (progressive disclosure via references/)
- References files exist if SKILL.md mentions them
- Learnings files exist for skills that have been used and refined
- No unused/abandoned skills (folders with placeholder content)

#### Area 4: Hooks

Read hooks configuration from settings.json.

**Check for:**
- What hooks are configured and what events they cover
- Hook event coverage: PreToolUse, PostToolUse, SessionStart, Stop, Notification
- Missed automation opportunities (common manual patterns that could be hooks)
- Any hooks that might be stale or broken (referencing scripts that don't exist)

#### Area 5: MCP Servers

Read both global and project MCP configs.

**Check for:**
- Configured servers and their types (stdio, HTTP)
- Missing common integrations (GitHub, Linear, Notion, Slack — based on what the project uses)
- Duplicate server configurations between global and project
- Server naming consistency

#### Area 6: Commands & Agents

Inventory commands in `~/.claude/commands/` and agents in `~/.claude/agents/`.

**Check for:**
- Commands have clear descriptions
- Agents have defined roles and tool access
- No overlap between commands and skills (commands should be lightweight triggers)
- Unused or placeholder agents/commands

#### Area 7: Folder Structure & Scope

Evaluate `~/.claude/` organization AND whether things are at the right scope (global vs. project). This is one of the most common sources of confusion and bugs.

**Folder organization checks:**
- Clear separation of concerns (skills, commands, agents, config)
- Scratch/temp directories are gitignored
- No stale files in active directories
- Logical nesting (not too flat, not too deep)
- CLAUDE.md files in subdirectories where they add value

**Global vs. project scope checks (CRITICAL — most people get this wrong):**
- Skills in `~/.claude/skills/` load for EVERY session across ALL projects. Are any of them project-specific and should be in `.claude/skills/` within the project instead?
- Hooks in `~/.claude/settings.json` fire for EVERY session. Are any hooks project-specific? (They should be in the project's `.claude/settings.local.json` or a plugin)
- `settings.json` is the global config. If the user has `CLAUDE_CONFIG_DIR` set (e.g., via aliases for multi-account setups), check whether `settings.json` is symlinked or duplicated — duplicated settings files silently break when one gets updated and the other doesn't
- MCP servers in `~/.claude/.mcp.json` connect for every project. Project-specific servers should be in the project's `.mcp.json`
- Global CLAUDE.md should contain only cross-project rules. Project-specific instructions belong in the project's CLAUDE.md, not the global one
- Check for context budget waste: skills/instructions loaded globally that only apply to one project

#### Area 8: Context Budget

Calculate total auto-loaded tokens per session.

**Measure:**
- Global CLAUDE.md: count lines
- Project CLAUDE.md: count lines (root + any auto-loaded nested)
- MEMORY.md: count lines (first 200 are auto-loaded)
- Total auto-loaded lines across all sources

**Evaluate:**
- Is the total reasonable? (Under 400 lines is good, 400-600 is acceptable, 600+ needs optimization)
- Is each file earning its context cost? (Does every section justify being auto-loaded?)
- Could any content move to on-demand files (references, topic files)?

---

## Step 2: Grade

Assign each area a letter grade using `references/scoring-rubric.md`:
- **A**: Excellent — well-optimized, follows best practices
- **B**: Good — functional with minor improvements possible
- **C**: Adequate — works but has clear optimization opportunities
- **D**: Needs Work — significant gaps or inefficiencies
- **F**: Missing/Broken — not configured or non-functional
- **N/A**: Not present — recommend setup if valuable

Use +/- modifiers for nuance (A-, B+, etc.).

Calculate overall score:
1. Convert each applicable grade to a number: A=95, A-=92, B+=88, B=85, B-=82, C+=78, C=75, C-=72, D+=68, D=65, D-=62, F=50
2. Average all applicable scores (skip N/A areas)
3. Convert back to letter grade with +/- modifier

---

## Step 3: Level

Based on the grades, determine the user's level (0-4) using the level mapping from `references/scoring-rubric.md`:

| Level | Grade Range | Description |
|-------|-------------|-------------|
| Level 0 — Getting Started | F-D | Not using features, or configuration is broken/missing |
| Level 1 — Foundations | D-C | Basic setup exists but has significant gaps or is underutilized |
| Level 2 — Intermediate | C-B | Features actively used with reasonable configuration, room for optimization |
| Level 3 — Advanced | B-A | Well-configured, follows best practices, integrated into workflow |
| Level 4 — Expert | A+ | Fully optimized, advanced patterns, progressive disclosure, active feedback loops |

**Overall level** is determined by the lowest area that the user actively uses. A user with nine B grades is more proficient than one with five A grades and four F grades.

Also refer to `references/level-guide.md` for the full detection criteria at each level.

---

## Step 4: Report

Show the user their level, their grades per area, and what's working vs what needs improvement.

### Format

Start with a warm greeting and their level:

> **Your setup: [Level Name]** (Level [N] of 4)
>
> [One sentence about what this level means — from level-guide.md]

If this is a returning user (user-state.json or last-audit.json has previous data), show progress:

> Since last time: [what changed — score improvements, regressions, new things added]

Then show the grade card:

```
| Area | Grade | Key Finding |
|------|-------|-------------|
| CLAUDE.md Files | [grade] | [one-line summary] |
| Memory & Session Continuity | [grade] | [one-line summary] |
| Skills | [grade] | [one-line summary] |
| Hooks | [grade] | [one-line summary] |
| MCP Servers | [grade] | [one-line summary] |
| Commands & Agents | [grade] | [one-line summary] |
| Folder Structure & Scope | [grade] | [one-line summary] |
| Context Budget | [grade] | [total lines] auto-loaded |
```

Then for each area, show a brief summary of what's working well and what issues were found. Include specific file paths and line numbers for issues. Do not output the full detailed audit report by default — keep it concise. If the user wants more detail on any area, they can ask.

If previous audit data exists in `${CLAUDE_PLUGIN_DATA}/last-audit.json`, diff the scores and highlight what improved or regressed. If no previous audit, note "First audit — no comparison available."

---

## Step 5: Recommend

Based on their level, pick 2-3 improvements that are appropriate. Do not overwhelm. Focus on what moves them to the next level.

### Recommendation Priority Framework

1. **Quick wins**: High impact, low effort (e.g., fixing a broken pointer, removing duplication)
2. **Strategic upgrades**: High impact, medium effort (e.g., setting up memory system, creating a missing skill)
3. **Nice to have**: Medium impact, low effort (e.g., adding keybindings, reorganizing folders)
4. **Advanced**: High impact, high effort (e.g., custom MCP server, agent team workflows)

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

### Presenting Recommendations

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

---

## Step 6: Build

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

## Step 7: Save State

After the report and any building, save state for progress tracking.

### 1. Update user state

Write `${CLAUDE_PLUGIN_DATA}/user-state.json`:

```json
{
  "last_run_date": "[today's date]",
  "level": "[N]",
  "level_name": "[Level Name]",
  "previous_level": "[N from last run, or null if first run]",
  "platform": "[cowork or cli]",
  "grades": {
    "claude_md": "[grade]",
    "memory": "[grade]",
    "skills": "[grade]",
    "hooks": "[grade]",
    "mcp_servers": "[grade]",
    "commands_agents": "[grade]",
    "folder_structure": "[grade]",
    "context_budget": "[grade]"
  },
  "overall_score": { "grade": "[grade]", "percentage": "[N]" },
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

### 2. Save audit snapshot

Write a snapshot to `${CLAUDE_PLUGIN_DATA}/audit-history/YYYY-MM-DD.md` containing the grade card, key findings for each area, and top recommendations. This becomes the historical record.

### 3. Update last audit state

Write `${CLAUDE_PLUGIN_DATA}/last-audit.json` with:

```json
{
  "date": "YYYY-MM-DD",
  "overall_score": { "grade": "[grade]", "percentage": "[N]" },
  "areas": {
    "claude_md": { "grade": "[grade]", "score": "[N]", "notes": "..." },
    "memory": { "grade": "[grade]", "score": "[N]", "notes": "..." },
    "skills": { "grade": "[grade]", "score": "[N]", "notes": "..." },
    "hooks": { "grade": "[grade]", "score": "[N]", "notes": "..." },
    "mcp_servers": { "grade": "[grade]", "score": "[N]", "notes": "..." },
    "commands_agents": { "grade": "[grade]", "score": "[N]", "notes": "..." },
    "folder_structure": { "grade": "[grade]", "score": "[N]", "notes": "..." },
    "context_budget": { "grade": "[grade]", "score": "[N]", "notes": "..." }
  },
  "key_metrics": {
    "total_auto_loaded_lines": 0,
    "skill_count": 0,
    "skills_with_learnings": 0,
    "hook_count": 0,
    "mcp_server_count": 0,
    "command_count": 0,
    "agent_count": 0,
    "broken_pointers": 0
  },
  "top_recommendations": ["...", "...", "..."]
}
```

### 4. Write health metrics to backlog

If `${CLAUDE_PLUGIN_DATA}/backlog.md` exists, update its `## Health Metrics` section with:
- `Last audit` -> today's date
- `Overall score` -> the overall grade from this audit
- `Top gap` -> the lowest-scoring area and its grade
- `Skills with learnings` -> count of skills with non-empty learnings.md / total skills
- `Backlog items stale 2+ weeks` -> count of `ready` or `trying` items older than 14 days

Also sync new recommendations to the backlog:
- For each recommendation that represents a feature adoption opportunity (new skill, new hook, new workflow pattern):
  - Check if it already exists in the Active Backlog (match by name or concept)
  - If already tracked: update the item's context, do NOT create a duplicate
  - If NOT tracked: add as a new backlog item with status `queued`
  - Do NOT add purely structural recommendations (e.g., "shorten CLAUDE.md") — only feature adoption opportunities

### Closing Message

End with something encouraging and forward-looking:

> That's it for now! You're at **[Level Name]** with [brief summary of what they have]. Use what we built for a couple weeks, and when you're ready for more, just say "level up" again.

If the user has a backlog, mention it:

> I noticed you're already tracking some things in your backlog — [brief mention]. Those are great next steps too.

---

## When to Suggest Running This

- User asks "how's my setup?" or "what should I improve?"
- After a major Claude Code version update
- Setup feels stale or disorganized
- Periodically (monthly is a good cadence)
- After significant configuration changes (new skills, new MCP servers, etc.)
- User is new to Claude Code and wants to get started
