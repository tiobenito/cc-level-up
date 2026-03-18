# Scoring Rubric

Detailed grading criteria for each CC System Audit area. Use these criteria to assign consistent, fair grades.

---

## Grade Definitions

| Grade | Meaning | Threshold |
|-------|---------|-----------|
| A | Excellent | Follows best practices, well-optimized, no significant issues |
| B | Good | Functional and mostly well-organized, minor improvements possible |
| C | Adequate | Works but has clear gaps or inefficiencies worth addressing |
| D | Needs Work | Significant problems that affect daily effectiveness |
| F | Missing/Broken | Not configured, or configured but non-functional |
| N/A | Not Present | Feature not in use — recommend if it would add value |

Use +/- modifiers for nuance (A-, B+, etc.).

---

## Level Mapping

Grades map to Claude Code proficiency levels. This helps users understand where they are and what to aim for.

| Level | Grade Range | Description |
|-------|-------------|-------------|
| Level 0 — Unaware | F-D | Not using the feature, or configuration is broken/missing |
| Level 1 — Aware | D-C | Basic setup exists but has significant gaps or is underutilized |
| Level 2 — Practicing | C-B | Feature is actively used with reasonable configuration, room for optimization |
| Level 3 — Proficient | B-A | Well-configured, follows best practices, integrated into workflow |
| Level 4 — Expert | A+ | Fully optimized, advanced patterns, progressive disclosure, active feedback loops |

**Overall level** is determined by the lowest area that the user actively uses. A user with nine B grades is more proficient than one with five A grades and four F grades.

---

## Area-Specific Criteria

### 1. CLAUDE.md Files

| Grade | Criteria |
|-------|----------|
| A | Clear structure, no duplication, no broken pointers, appropriate length, good separation between global/project |
| B | Well-structured but has minor duplication or 1-2 stale references |
| C | Functional but overly long (300+ lines), some duplication, or missing structure |
| D | Disorganized, significant duplication, multiple broken pointers |
| F | No CLAUDE.md files, or files exist but are empty/placeholder |

**Key metrics:** Line count per file, number of broken pointers, duplication instances.

**Level guidance:**
- Level 0-1 (D-C): Has a CLAUDE.md but it is a wall of text, duplicates content, or has stale references
- Level 2 (C-B): Structured with headers, reasonable length, some separation of global vs project concerns
- Level 3 (B-A): Clean layering (global/project/nested), no duplication, all pointers valid, content earns its context cost
- Level 4 (A+): Uses nested CLAUDE.md for subdirectory context, `.claude/CLAUDE.md` for personal gitignored rules, progressive disclosure

### 2. Memory & Session Continuity

| Grade | Criteria |
|-------|----------|
| A | MEMORY.md under 200 lines, all topic files referenced, no duplication with CLAUDE.md, well-organized by topic. Session continuity mechanism exists and is fresh. |
| B | Good index, minor staleness in 1-2 topic files, or slight duplication. Session continuity exists but update is manual. |
| C | Index exists but some referenced files are missing, or significant staleness. No session continuity. |
| D | Memory files exist but are disorganized, heavily duplicated with CLAUDE.md, or very stale |
| F | Memory directory exists but MEMORY.md is missing or broken |

**Key metrics:** MEMORY.md line count, number of stale entries, duplication count, handover freshness (if applicable).

**Level guidance:**
- Level 0-1 (D-C): No memory system, or MEMORY.md exists but is unstructured
- Level 2 (C-B): MEMORY.md with some topic organization, occasionally updated
- Level 3 (B-A): Clean index under 200 lines, topic files by subject, no duplication with CLAUDE.md, session continuity mechanism in use
- Level 4 (A+): Active routing (rules to CLAUDE.md, state to memory, session to handover), topic files regularly pruned, handover feeds into persistent memory

### 3. Skills

| Grade | Criteria |
|-------|----------|
| A | All skills have valid frontmatter with trigger phrases, bodies under 500 lines, references used for detail, learnings files where applicable |
| B | Most skills are well-structured, 1-2 missing trigger phrases or slightly long |
| C | Skills exist but several have vague descriptions, missing triggers, or no progressive disclosure |
| D | Multiple skills with broken frontmatter, placeholder content, or no references |
| F | Skills directory empty or all skills are non-functional |

**Key metrics:** Skill count, average description quality, body line count, learnings file count.

**Level guidance:**
- Level 0-1 (D-C): No skills, or 1-2 basic ones with poor descriptions
- Level 2 (C-B): Several skills with working frontmatter, some trigger phrases, basic structure
- Level 3 (B-A): Skills with good descriptions + triggers, references for detail, some learnings captured
- Level 4 (A+): Skills with active learnings pipeline, progressive disclosure, clear trigger differentiation, no overlap

### 4. Hooks

| Grade | Criteria |
|-------|----------|
| A | Hooks cover common automation needs, well-configured, covering multiple event types |
| B | Some hooks configured, covering the most important automation |
| C | 1-2 hooks exist but major automation opportunities are missed |
| D | Hooks configured but broken or misconfigured |
| F | No hooks configured despite clear automation opportunities |

**Key metrics:** Hook count, event types covered, identified missed opportunities.

**Level guidance:**
- Level 0-1 (D-C): No hooks, or one basic hook
- Level 2 (C-B): A few hooks covering PreToolUse or PostToolUse for common needs
- Level 3 (B-A): Hooks across multiple event types, covering key automation (auto-approval, linting, notifications)
- Level 4 (A+): Comprehensive hook coverage (PreToolUse, PostToolUse, SessionStart, Stop, Notification), hook chains for complex workflows

### 5. MCP Servers

| Grade | Criteria |
|-------|----------|
| A | All relevant services connected, no duplicates, clean configuration |
| B | Key services connected, minor config issues or 1 missing integration |
| C | Some services connected but gaps in coverage for tools the project uses |
| D | Minimal MCP setup, or servers configured but not working |
| F | No MCP servers configured despite using external services |

**Key metrics:** Server count, coverage of project tools, duplicate configs.

**Level guidance:**
- Level 0-1 (D-C): No MCP servers, or one that is not working
- Level 2 (C-B): Key services connected (e.g., GitHub), basic config
- Level 3 (B-A): Good coverage of relevant services, clean config, no duplicates
- Level 4 (A+): Comprehensive coverage, global vs project separation, custom MCP servers for specialized needs

### 6. Commands & Agents

| Grade | Criteria |
|-------|----------|
| A | Commands and agents are well-defined, no overlap with skills, clear descriptions and roles |
| B | Good set of commands/agents, minor overlap or 1-2 missing descriptions |
| C | Some commands/agents exist but roles are unclear or overlap with skills |
| D | Commands/agents exist but are mostly placeholder or broken |
| F | None configured despite clear use cases |

**Key metrics:** Command count, agent count, overlap instances.

**Level guidance:**
- Level 0-1 (D-C): No commands or agents
- Level 2 (C-B): A few commands for common actions, maybe one agent
- Level 3 (B-A): Commands for quick triggers, agents for specialized perspectives, clean separation from skills
- Level 4 (A+): Well-defined agent roles with specific tool access, commands as lightweight triggers for skills, no overlap

### 7. Folder Structure & Scope

| Grade | Criteria |
|-------|----------|
| A | Clear separation of concerns, gitignored scratch dirs, logical nesting, correct global vs. project scoping for all features |
| B | Good organization, minor clutter, 1-2 things at wrong scope (e.g., a project-specific skill installed globally) |
| C | Functional but some directories are catchalls, limited awareness of scope implications |
| D | Disorganized, project-specific config mixed with global, stale files mixed with active work |
| F | No discernible structure, everything in root, scope not considered |

**Key metrics:** Directory depth, stale file count, gitignore coverage, scope violations.

**Scope checks (CRITICAL — most common source of confusion):**
- Skills in `~/.claude/skills/` load for ALL projects. Any that are project-specific?
- Hooks in `~/.claude/settings.json` fire for ALL sessions. Any that are project-specific?
- If `CLAUDE_CONFIG_DIR` is set (multi-account setups), is `settings.json` symlinked or duplicated? Duplicated = silent breakage when one copy gets updated
- MCP servers in `~/.claude/.mcp.json` connect for all projects. Project-specific servers should be in the project's `.mcp.json`
- Global CLAUDE.md should only have cross-project rules. Project-specific instructions belong in the project's CLAUDE.md

**Level guidance:**
- Level 0-1 (D-C): Files scattered with no convention, no awareness of global vs. project scope
- Level 2 (C-B): Reasonable folder structure, some conventions followed, but may have scope mismatches
- Level 3 (B-A): Clean separation, correct scoping for most features, gitignored scratch dirs
- Level 4 (A+): Perfect scope separation, nested CLAUDE.md where useful, conventions documented, multi-account setups handled cleanly

### 8. Context Budget

| Grade | Criteria |
|-------|----------|
| A | Under 300 total auto-loaded lines, every section earns its cost |
| B | 300-500 lines, mostly justified, minor optimization possible |
| C | 500-700 lines, some content could move to on-demand files |
| D | 700+ lines, significant bloat in auto-loaded content |
| F | 1000+ lines or no awareness of context budget at all |

**Key metrics:** Total auto-loaded lines, breakdown by source, lines-per-area ratios.

**Level guidance:**
- Level 0-1 (D-C): No awareness of context budget, or 700+ auto-loaded lines of unfocused content
- Level 2 (C-B): Awareness of auto-loading, some effort to keep content concise
- Level 3 (B-A): Under 500 lines, content organized with on-demand topic files for detail
- Level 4 (A+): Under 300 lines, every line earns its context cost, progressive disclosure throughout

---

## Overall Score Calculation

1. Convert each applicable grade to a number: A=95, A-=92, B+=88, B=85, B-=82, C+=78, C=75, C-=72, D+=68, D=65, D-=62, F=50
2. Average all applicable scores (skip N/A areas)
3. Convert back to letter grade with +/- modifier
4. Round to nearest grade boundary

---

## Comparative Benchmarks

These represent what a well-configured Claude Code setup looks like at different levels:

**Level 0-1 / Beginner (D-C range):** Has a CLAUDE.md, maybe 1-2 skills, basic MCP setup. No memory system, no hooks, no session continuity.

**Level 2 / Intermediate (C-B range):** Good CLAUDE.md with project-specific instructions, several skills, MCP for key services, some hooks. May lack memory system or context budget awareness.

**Level 3 / Advanced (B-A range):** Layered CLAUDE.md (global + project + nested), memory system with topic files, session continuity via handover, well-structured skills with learnings, hooks for common automation, optimized context budget, clean folder structure.

**Level 4 / Expert (A range):** Everything above plus: custom agents for specialized review, agent team workflows, comprehensive hook coverage, progressive disclosure throughout, all content earns its context cost, active learnings pipeline feeding back into skills, plugins for bundled capabilities.
