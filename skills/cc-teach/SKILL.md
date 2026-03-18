---
name: cc-teach
description: "Package Claude Code knowledge into shareable training materials, config guides, or onboarding docs for teammates. Use when user says 'share my CC setup', 'create a training guide', 'teach my team Claude Code', 'document this skill', 'onboard someone to CC', 'export my config', or wants to export their setup or skills for others. Do NOT use for improving the user's own setup (use cc-level-up instead)."
---

# CC Teach Skill

This skill powers the `/cc-teach` command. It helps users package their Claude Code expertise into shareable materials for their team.

## References
- `templates/team-guide.md` — Template for team onboarding guides
- `templates/skill-doc.md` — Template for documenting individual skills
- `templates/config-share.md` — Template for shareable config guides

## Context Loading (Before Generating Any Output)

Before generating teaching materials, load these additional context sources:

1. **Read the Adopted features table** in `${CLAUDE_PLUGIN_DATA}/backlog.md` (the `## Adopted` section). These are features the user actively uses and has validated. When generating teaching materials:
   - Highlight adopted features as **"proven and recommended"** — these have been battle-tested in the user's workflow
   - Distinguish them from experimental or `trying` features, which should be presented as **"experimental — currently being evaluated"**
   - `queued` or `ready` features should NOT be presented as recommendations to teammates unless explicitly requested

2. **Check for skill learnings** when documenting any specific skill:
   - Look for `learnings.md` files alongside the skill being documented (both in `~/.claude/skills/<skill-name>/learnings.md` and any plugin skill directories)
   - If a learnings file exists and has content, incorporate the lessons into the teaching material — these are real-world gotchas and tips that make the skill more effective
   - Present learnings as "Tips from real usage" or "Gotchas to know about" — they add credibility and practical value

3. **Cross-reference the backlog** to avoid recommending features the user hasn't adopted yet (unless the teaching context calls for it)

## Teaching Modes

### 1. Skill Documentation
Document a specific skill so teammates can understand and use it.
- Pull from the skill's SKILL.md and references
- Add context about when/why to use it
- Include concrete examples
- Check for and incorporate any learnings.md content
- Output a self-contained markdown document

### 2. Config Export
Create a guide for replicating the user's setup (or parts of it).
- Scan all config files (settings.json, CLAUDE.md, .mcp.json, hooks)
- Explain each configuration choice
- Sanitize personal data and secrets
- Provide copy-paste setup instructions
- Note which parts are optional vs. recommended

### 3. Team Onboarding Guide
A comprehensive "Getting Started with Claude Code" guide customized to the user's team.
- Start from the team-guide template
- Populate with real examples from the user's setup
- Organize by skill level (beginner -> intermediate -> advanced)
- Include team-specific conventions and tools

### 4. Full Package
Everything above, organized into a directory:
```
cc-teach-package/
  README.md           — Overview and index
  getting-started.md  — Team onboarding guide
  config-guide.md     — Setup recommendations
  skills/             — Individual skill documentation
  examples/           — Real-world usage examples
```

## Output Location

All generated materials are saved to the current working directory. The user can specify a subfolder name or it defaults to `cc-teach-output/`.

## When Claude Should Suggest This
- The user mentions teaching, onboarding, or sharing CC knowledge
- The user creates something reusable that teammates would benefit from
- A new team member is mentioned
- The user asks how to share their setup
