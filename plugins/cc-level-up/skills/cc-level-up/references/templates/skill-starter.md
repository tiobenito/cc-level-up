# Skill Starter Template

Use this template when building a first skill for a Level 0-1 user. First skills should be simple and immediately useful.

## Questions to Ask First

1. "What task do you find yourself doing over and over?" — Identifies the core action.
2. "Walk me through how you do it now." — Captures the current workflow so the skill can replicate it.
3. "What does a good result look like?" — Defines success criteria and output shape.

## Template

```markdown
---
name: [skill-name]
description: >
  [What it does in 1-2 sentences. Include trigger phrases like "use when
  the user says X, Y, or Z".]
---

# [Skill Name]

[1-2 sentence overview of what this skill does and when to use it.]

## Steps

1. [First thing Claude should do — e.g., "Ask for the raw data or paste"]
2. [Processing step — e.g., "Extract key fields: date, amount, status"]
3. [Output step — e.g., "Format as a clean table with headers"]

## Output Format

[Describe or show the expected output shape — e.g., a table, bullet list, or template]

## Rules

- [Any constraint — e.g., "Never round dollar amounts"]
- [Any preference — e.g., "Use bullet points, not paragraphs"]
```

## Platform-Specific Notes

**Cowork:** Skills live in `skills/[skill-name]/SKILL.md` at the project root. Explain to the user: "Just say 'use my [skill name]' or describe the task — Claude will find the right skill."

**CLI:** Skills can live in two places:
- `~/.claude/skills/[skill-name]/SKILL.md` — Global skills available in every project
- `.claude/skills/[skill-name]/SKILL.md` — Project-specific skills
Explain the difference and ask where this skill should live.

## Common First Skills by Use Case

These are starting points — always ask the user what they actually need.

**Writing/Content:**
- format-meeting-notes — Clean up raw meeting notes into structured summaries
- draft-email — Generate professional emails from bullet points
- summarize-doc — Condense long documents into key takeaways

**Data/Analysis:**
- format-report — Turn raw data into a clean formatted report
- analyze-data — Walk through a dataset and surface insights
- sql-helper — Help write and explain SQL queries

**Development:**
- code-review — Review code for bugs, style, and improvements
- write-tests — Generate tests for a given function or module
- explain-code — Break down unfamiliar code in plain language

**Operations/PM:**
- status-update — Generate status reports from raw notes
- task-breakdown — Break a large task into actionable subtasks
- decision-doc — Structure a decision with options, tradeoffs, and recommendation

## Tips

- Name should be lowercase-with-dashes, 2-4 words
- Description must include trigger phrases so Claude knows when to use it
- Keep skills focused — one task per skill
- Include an output format section so the user knows what to expect
- Do not over-engineer the first version — they can refine it later
- First skills should be 15-30 lines, not 100-line masterpieces
