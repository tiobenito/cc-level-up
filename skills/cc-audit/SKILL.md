---
name: cc-audit
description: >
  Comprehensive audit of a Claude Code setup including CLAUDE.md files, memory
  system, session continuity, skills, hooks, MCP servers, commands/agents,
  folder structure, and context budget. Produces a scored report with actionable
  recommendations. Triggers: "audit my setup", "check my CC config", "how's my
  system", "review my Claude Code", "system health check", "score my setup",
  "grade my setup". Does NOT trigger for auditing code, security audits, or
  reviewing application logic.
---

# CC System Audit

Perform a comprehensive audit of the user's Claude Code setup. Scan everything, score each area, and produce a prioritized report with actionable recommendations.

## References

- `references/feature-registry.md` — Database of CC features the audit checks against
- `references/scoring-rubric.md` — Detailed grading criteria for each audit area, with level mappings

Read `references/scoring-rubric.md` before starting the audit — it defines what "good" looks like for each area.

## Performance Notes

- Take your time. Thoroughness matters more than speed.
- Read every file you audit — do not skip or summarize from file names alone.
- Do not skip any audit area. If nothing is found, score it and note the gap.

---

## Step 0: Load Backlog Context

Before running the audit, check if `${CLAUDE_PLUGIN_DATA}/backlog.md` exists (managed by the /learn skill).

1. If it exists, read the **Active Backlog** section — note items by status (`queued`, `ready`, `trying`)
2. Read the **Adopted** table — know what's already working
3. Read the **Health Metrics** section — check previous audit data if present
4. Keep this context in mind during the audit: if a finding overlaps with a backlog item, note that it's already being tracked rather than treating it as a new discovery
5. If the file does not exist, proceed without it — the audit will still produce a full report

Also check if `${CLAUDE_PLUGIN_DATA}/last-audit.json` exists for previous audit state.

---

## Step 1: Discovery

Scan the environment to build an inventory of what exists. Do not assume any specific structure — discover it.

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

Use Glob and Read tools to discover files. Record what exists and what doesn't.

---

## Step 2: Audit Each Area

For each area below, evaluate what was found during discovery. Assign a letter grade (A/B/C/D/F) using the criteria in `references/scoring-rubric.md`. If an area has no files at all, grade it N/A and recommend setup.

### Area 1: CLAUDE.md Files

Evaluate all CLAUDE.md files (global + project + nested).

**Check for:**
- Clear structure with headers and sections
- Accurate, non-stale content (references to files/tools that still exist)
- No broken pointers (paths that don't resolve)
- Appropriate length (global: under 200 lines preferred; project: under 150 lines)
- No duplication across files (same instructions in multiple places)
- Separation of concerns (global = cross-project rules, project = project-specific)

### Area 2: Memory & Session Continuity

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

### Area 3: Skills

Inventory all skills in `~/.claude/skills/`.

**Check for:**
- Each skill has a valid SKILL.md with YAML frontmatter
- Description includes BOTH what it does AND trigger phrases
- No skill name uses spaces, capitals, or underscores
- Body is under 500 lines (progressive disclosure via references/)
- References files exist if SKILL.md mentions them
- Learnings files exist for skills that have been used and refined
- No unused/abandoned skills (folders with placeholder content)

### Area 4: Hooks

Read hooks configuration from settings.json.

**Check for:**
- What hooks are configured and what events they cover
- Hook event coverage: PreToolUse, PostToolUse, SessionStart, Stop, Notification
- Missed automation opportunities (common manual patterns that could be hooks)
- Any hooks that might be stale or broken (referencing scripts that don't exist)

### Area 5: MCP Servers

Read both global and project MCP configs.

**Check for:**
- Configured servers and their types (stdio, HTTP)
- Missing common integrations (GitHub, Linear, Notion, Slack — based on what the project uses)
- Duplicate server configurations between global and project
- Server naming consistency

### Area 6: Commands & Agents

Inventory commands in `~/.claude/commands/` and agents in `~/.claude/agents/`.

**Check for:**
- Commands have clear descriptions
- Agents have defined roles and tool access
- No overlap between commands and skills (commands should be lightweight triggers)
- Unused or placeholder agents/commands

### Area 7: Folder Structure & Scope

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

### Area 8: Context Budget

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

## Step 3: Score and Report

### Scoring

Assign each area a letter grade using `references/scoring-rubric.md`:
- **A**: Excellent — well-optimized, follows best practices
- **B**: Good — functional with minor improvements possible
- **C**: Adequate — works but has clear optimization opportunities
- **D**: Needs Work — significant gaps or inefficiencies
- **F**: Missing/Broken — not configured or non-functional
- **N/A**: Not present — recommend setup if valuable

Calculate overall score: average of all applicable grades (skip N/A areas), converted to a letter grade with +/- modifier.

### Report Format

Output the report using this structure:

```
# CC System Audit Report
*Generated: YYYY-MM-DD*

## Overall Score: [GRADE] ([percentage]%)

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

---

## Detailed Findings

### [Area Name] ([Grade])

**What's working well:**
- [strength]

**Issues found:**
- [issue with specific file path and line numbers]

**Recommendations:**
1. [specific, actionable recommendation]

[Repeat for each area]

---

## Top 5 Recommendations (Priority Order)

Prioritize by: Impact (high/med/low) x Effort (high/med/low)

1. **[Action]** — [why] (Impact: high, Effort: low)
2. ...

---

## Changes Since Last Audit

[If previous audit data exists in ${CLAUDE_PLUGIN_DATA}/last-audit.json, diff the scores and highlight what improved or regressed. If no previous audit, note "First audit — no comparison available."]
```

---

## Step 4: Save State

After outputting the report:

### 1. Save audit snapshot

Write a snapshot to `${CLAUDE_PLUGIN_DATA}/audit-history/YYYY-MM-DD.md` containing:
- Full report (copy of what was output)
- This becomes the historical record

### 2. Update last audit state

Write `${CLAUDE_PLUGIN_DATA}/last-audit.json` with:
```json
{
  "date": "YYYY-MM-DD",
  "overall_score": { "grade": "B+", "percentage": 88 },
  "areas": {
    "claude_md": { "grade": "A-", "score": 92, "notes": "..." },
    "memory": { "grade": "B", "score": 85, "notes": "..." },
    "session_continuity": { "grade": "...", "score": 0, "notes": "..." },
    "skills": { "grade": "...", "score": 0, "notes": "..." },
    "hooks": { "grade": "...", "score": 0, "notes": "..." },
    "mcp_servers": { "grade": "...", "score": 0, "notes": "..." },
    "commands_agents": { "grade": "...", "score": 0, "notes": "..." },
    "folder_structure": { "grade": "...", "score": 0, "notes": "..." },
    "context_budget": { "grade": "...", "score": 0, "notes": "..." }
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

### 3. Write health metrics to backlog

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

### 4. Offer next steps

Ask the user if they want to implement any recommendations now.

---

## Recommendation Priority Framework

When ranking recommendations:

1. **Quick wins**: High impact, low effort (e.g., fixing a broken pointer, removing duplication)
2. **Strategic upgrades**: High impact, medium effort (e.g., setting up memory system, creating a missing skill)
3. **Nice to have**: Medium impact, low effort (e.g., adding keybindings, reorganizing folders)
4. **Advanced**: High impact, high effort (e.g., custom MCP server, agent team workflows)

---

## When to Suggest Running This Audit

- User asks "how's my setup?" or "what should I improve?"
- After a major Claude Code version update
- Setup feels stale or disorganized
- Periodically (monthly is a good cadence)
- After significant configuration changes (new skills, new MCP servers, etc.)
