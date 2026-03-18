# CLAUDE.md Starter Template

Use this template when building a CLAUDE.md for a Level 0 user. The goal is a minimal, useful file — not a comprehensive manifesto.

## Questions to Ask First

1. "What do you do?" — Role, team, or project context. Keep it open-ended.
2. "What do you use Claude for most?" — Shapes the use case section.
3. "Any formatting preferences?" — Bullet points vs prose, tables vs lists, concise vs detailed, tone.

If the user has an org context file loaded (via `references/org-context-template.md`), use it to suggest role-appropriate defaults. But always prefer the user's own words.

## Template (10-15 lines)

```markdown
# [Project Name or Workspace Name]

## About Me
[Role description — 1-2 sentences in the user's own words]

## What I Use Claude For
- [Primary use case from their answer]
- [Secondary use case if mentioned]

## How I Like Things
- [Format preference — e.g., "Keep responses concise with bullet points"]
- [Tone preference — e.g., "Professional but conversational"]
- [Any specific rule — e.g., "Always show data in tables"]
```

## Platform-Specific Notes

**Cowork:** This file goes at the project root. Call it "project instructions" in conversation, but use the filename CLAUDE.md when creating it. Explain: "This loads automatically every time you start a conversation in this project."

**CLI:** This file goes at the repo root (for project-specific instructions) or `~/.claude/CLAUDE.md` (for global instructions that apply everywhere). Explain: "Claude reads this file at the start of every session. Put project-specific stuff in the repo, global preferences in your home directory."

## Tips

- Use the user's exact words where possible — do not over-polish
- Keep it under 15 lines. They can always add more later
- Do not add sections they did not mention (no placeholder sections)
- If they mention something they never want, add it: "Never: [thing]"
- If they are unsure about preferences, start with just About Me and use cases — rules can come later
