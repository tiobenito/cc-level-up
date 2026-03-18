# Level-Up Progression Guide

This is the unified progression path for a Claude Code setup. Each level builds on the last. Works for both Cowork (Projects UI) and CLI users.

---

## Level 0 — Getting Started

**What it looks like:** Just installed Claude Code or created a new Project. No CLAUDE.md (or a bare-bones one under 5 lines). Maybe 0-1 skills. Default folder structure.

**What you'll learn:** Project instructions — a file called CLAUDE.md that tells Claude who you are, what you do, and how you like things done. This is the single highest-impact thing you can set up. It means Claude remembers your preferences every time you start a conversation.

**What gets built:** A starter CLAUDE.md (10-15 lines) and 1 skill tailored to what you do.

### Detection Criteria

- No CLAUDE.md, or CLAUDE.md under 5 lines
- 0-1 skills total
- Default or empty folder structure

### What to Recommend

1. Create a CLAUDE.md with role description, primary use case, and format preferences
2. Build a first skill for a task the user does repeatedly

### Example Files to Build

**CLAUDE.md:**
```markdown
# My Project

## About Me
I'm a [role] working on [what]. I use Claude to help with [primary use case].

## What I Use Claude For
- [Primary task]
- [Secondary task]

## How I Like Things
- Keep responses concise with bullet points
- [Format or tone preference]
```

**First skill** (e.g., `format-meeting-notes/SKILL.md`):
```markdown
---
name: format-meeting-notes
description: Turns raw meeting notes into a clean summary with action items.
---

# Format Meeting Notes

Take raw, messy meeting notes and produce a clean summary.

## Steps
1. Ask for the raw notes (paste or file)
2. Extract: key decisions, action items (with owners), and open questions
3. Format as a clean summary

## Output Format
### Meeting Summary — [Date]
**Decisions:** [bulleted list]
**Action Items:** [bulleted list with owners]
**Open Questions:** [bulleted list]
```

---

## Level 1 — Foundation

**What it looks like:** Has a CLAUDE.md with at least a role description (5+ lines). 2-3 skills with basic structure.

**What you'll learn:** Reference libraries — docs you drop into a folder so Claude can look things up when it needs to. Think templates, term glossaries, process docs. Also: behavioral rules — standing instructions in your CLAUDE.md that shape how Claude works with you (tone, format preferences, things to always/never do).

**What gets built:** A reference folder with 2-3 starter docs, plus new behavioral rules in CLAUDE.md.

### Detection Criteria

- CLAUDE.md exists with 5+ lines, includes role or project description
- 2-3 skills with basic frontmatter and structure

### What to Recommend

1. Create a reference library (templates, glossaries, process docs)
2. Add behavioral rules to CLAUDE.md ("always/never" instructions)
3. Build another skill based on what they do most

### Example Files to Build

**Reference doc** (e.g., `reference/glossary.md`):
```markdown
# Team Glossary

Terms Claude should know when working with me.

| Term | Definition |
|------|-----------|
| [term] | [definition] |
```

**Behavioral rules addition to CLAUDE.md:**
```markdown
## Rules

- Always use bullet points for lists, not numbered lists
- Never round numbers — show exact values
- When summarizing, lead with the most important point
- Ask clarifying questions before starting long tasks
```

---

## Level 2 — Established

**What it looks like:** Rich CLAUDE.md with behavioral rules (15+ lines). Reference folder with 2+ docs. 4+ skills. CLI users may have basic hooks or 1 MCP server.

**What you'll learn:**

*Cowork:* Skill design — how to split multi-purpose skills into focused ones, add output templates, and organize with subfolder CLAUDE.md files.

*CLI:* Hooks — scripts that run automatically (like auto-formatting code). MCP servers — connections that let Claude talk directly to your tools (GitHub, databases, etc.). Skill refinement with output templates and reference files.

**What gets built:**

*Cowork:* Refined skills with output templates, subfolder organization.

*CLI:* First hook, first MCP server, refined skills.

### Detection Criteria

- CLAUDE.md has behavioral rules (15+ lines with "always/never" type instructions)
- Reference folder with 2+ documents
- 4+ skills with structure
- CLI bonus: basic hooks or 1 MCP server present

### What to Recommend

**Cowork:**
1. Refine existing skills — add output templates, split broad skills
2. Organize with subfolder CLAUDE.md files
3. Add output templates to skills for consistent formatting

**CLI:**
1. Set up a hook (e.g., auto-lint, auto-format, pre-commit checks)
2. Connect an MCP server (GitHub, Slack, database, etc.)
3. Refine skills — output templates, reference files, better structure

### Example Files to Build

**Hook configuration** (CLI — in `.claude/settings.json`):
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "npx prettier --write $CLAUDE_FILE_PATH"
      }
    ]
  }
}
```

**Skill with output template:**
```markdown
---
name: weekly-report
description: Generates a weekly status report from notes.
---

# Weekly Report

## Steps
1. Ask for this week's accomplishments, blockers, and next week's plan
2. Format using the template below

## Output Template

### Week of [Date]

**Accomplishments**
- [item]

**Blockers**
- [item] — Impact: [description]

**Next Week**
- [item]
```

---

## Level 3 — Power User

**What it looks like:** Well-organized folder structure. Skills have their own reference files or output templates. 6+ skills. CLI: hooks configured, MCP servers connected, custom commands or agents. Cowork: subfolder CLAUDE.md files, session notes workflow.

**What you'll learn:**

*Cowork:* Session continuity — keeping notes between conversations so Claude picks up where you left off. Advanced skill patterns like skills that reference other files and multi-step workflows. System maintenance habits.

*CLI:* Auto-memory (MEMORY.md and topic files). Custom commands or agents for specialized tasks. The learnings loop — adding learnings.md files next to skills so Claude gets better at running them over time.

**What gets built:**

*Cowork:* Session notes workflow, advanced skill upgrades.

*CLI:* Memory system, custom agents or commands, learnings files for top skills.

### Detection Criteria

- Well-organized folder structure (beyond defaults)
- Skills have their own reference files or output templates
- 6+ skills with good structure
- CLI: hooks configured + MCP servers + evidence of custom workflows
- Cowork: subfolder CLAUDE.md files or progressive organization

### What to Recommend

**Cowork:**
1. Session notes habit for continuity between conversations
2. Advanced skill patterns (multi-step, cross-referencing)
3. System maintenance — audit stale content, outdated rules

**CLI:**
1. Auto-memory system (MEMORY.md + topic files in `.claude/memory/`)
2. Custom commands or agents for specialized tasks
3. Learnings loop (learnings.md alongside skills)

### Example Files to Build

**Learnings file** (CLI — `~/.claude/skills/[skill]/learnings.md`):
```markdown
## Learning: Include timezone in date outputs (2025-03-15)
**What happened:** Report skill produced dates without timezone, causing confusion.
**Lesson:** Always include timezone (UTC or local) in any date output.
**Apply when:** Any skill that outputs dates or timestamps.
```

**Memory topic file** (CLI — `.claude/memory/patterns.md`):
```markdown
# Patterns

## Code Style
- Prefer early returns over nested if/else
- Use descriptive variable names, no abbreviations
- Always add JSDoc comments to exported functions
```

---

## Level 4 — Expert

**What it looks like:** Complete, well-organized system. Demonstrates system thinking — files reference each other, clear separation of concerns. CLI: learnings loop active, scoring checklists, optimized context loading, plugin-level organization. Cowork: mature system with advanced patterns, cross-referencing, maintenance habits.

**What you'll learn:** Optimization and sharing. Context loading strategies (what to load, what to defer). Scoring checklists for quality. Packaging your setup for others.

**What gets built:**

*Cowork:* Quality checklists, documentation of your system for teammates.

*CLI:* Context optimization, scoring checklists, plugin packaging.

### Detection Criteria

- Complete, well-organized system across all areas
- System thinking: files reference each other, clear separation of concerns
- CLI: learnings loop active, evidence of iteration and refinement
- Cowork: mature system with advanced skill patterns and cross-referencing

### What to Recommend

**Cowork:**
1. Consider CLI — "There's a whole other level with hooks, persistent memory, MCP servers, and agent teams."
2. Quality checklists — create scoring criteria for skill outputs

**CLI:**
1. Context optimization — review what loads and when, minimize unnecessary context
2. Scoring checklists — self-evaluation criteria for skill outputs
3. Plugin packaging — share your setup as a reusable plugin for your team

---

## How Levels Are Detected

Levels are assigned automatically based on what files exist — not by asking the user. The skill scans for CLAUDE.md, skills, reference docs, hooks, MCP servers, memory files, folder structure, and organization patterns. The user does not need to declare their level.

## How Often to Run

Every 2-4 weeks is a good cadence. Each run detects the current state, celebrates progress, and suggests 2-3 concrete next steps. The user state file tracks when the next run is suggested.
