# Customizing cc-level-up for Your Organization

cc-level-up is designed to work out of the box for individual users, but it can be customized for teams and organizations. This guide covers the main customization points.

## Org Context Template

When your team uses `/cc-level-up`, the plugin can incorporate org-specific context — things like required MCP servers, mandatory CLAUDE.md sections, or team coding conventions.

### How to Set It Up

Create a file at `${CLAUDE_PLUGIN_DATA}/org-context.md` with your organization's requirements:

```markdown
# Org Context — [Your Company]

## Required Configuration
- All engineers must have the GitHub MCP server configured
- CLAUDE.md files must include a `## Testing` section
- settings.json must deny access to `.env` and credentials files

## Team Conventions
- Use plan mode for any PR with 3+ files changed
- Always run tests before committing (add a PreToolUse hook)
- Document new skills in the team wiki

## Approved Plugins
- cc-level-up
- [your-org-plugin]

## Scoring Adjustments
- GitHub MCP server: required (not optional)
- Pre-commit hooks: required for Level 2+
- Team CLAUDE.md template: required for Level 1+
```

When the audit or level-up skill runs, it reads this file and factors it into the scoring and recommendations. Features marked as "required" will generate warnings if missing, regardless of the user's level.

## Adding Team-Specific Skills

You can bundle custom skills with the plugin by adding them to the `skills/` directory.

### Skill Structure

```
skills/
  your-skill-name/
    SKILL.md          # Skill definition (name, description, instructions)
    templates/        # Optional: template files the skill uses
    references/       # Optional: reference materials
    learnings.md      # Auto-populated: lessons from real usage
```

### Writing a SKILL.md

Every skill needs a SKILL.md with YAML frontmatter:

```yaml
---
name: your-skill-name
description: "One sentence describing when Claude should use this skill. Include trigger phrases so Claude knows when to activate it."
---
```

The body of the SKILL.md contains instructions Claude follows when the skill is invoked. Be specific about:
- What context to load before generating output
- What steps to follow
- What the output should look like
- What to avoid

### Example: Team Review Checklist Skill

```yaml
---
name: review-checklist
description: "Generate a PR review checklist based on team standards. Use when user says 'review checklist', 'PR checklist', or 'what should I check in this PR'."
---

# Review Checklist Skill

## Instructions
1. Read the current git diff
2. Read the team's review standards from ${CLAUDE_PLUGIN_DATA}/org-context.md
3. Generate a checklist tailored to the specific changes
4. Flag any violations of team conventions
```

## Customizing the Scoring Rubric

The default scoring rubric assigns points based on which features are configured. You can adjust the weights and thresholds for your organization.

### Default Point Values

| Feature | Points | Category |
|---------|--------|----------|
| Project CLAUDE.md exists | 3 | Foundation |
| Global CLAUDE.md exists | 3 | Foundation |
| Custom permissions in settings.json | 4 | Foundation |
| Custom commands | 5 | Intermediate |
| MCP server configured | 5 | Intermediate |
| Structured CLAUDE.md (multiple sections) | 4 | Intermediate |
| Global memory system | 5 | Intermediate |
| Custom skills | 8 | Advanced |
| Hooks configured | 8 | Advanced |
| Agent teams experience | 6 | Advanced |
| Plugins installed | 7 | Advanced |
| Multi-account setup | 5 | Advanced |
| Published plugin | 10 | Expert |
| Teaching materials created | 8 | Expert |

### Overriding Point Values

Create `${CLAUDE_PLUGIN_DATA}/scoring-overrides.json`:

```json
{
  "overrides": {
    "mcp_server": { "points": 10, "required": true },
    "pre_commit_hook": { "points": 10, "required": true },
    "custom_commands": { "points": 3 }
  },
  "level_thresholds": {
    "1": 10,
    "2": 25,
    "3": 45,
    "4": 60
  },
  "required_for_level": {
    "1": ["project_claude_md", "custom_permissions"],
    "2": ["mcp_server", "custom_commands", "global_claude_md"],
    "3": ["hooks", "custom_skills"]
  }
}
```

With `required_for_level`, a user cannot advance to that level even if they have enough points — they must also have the required features. This is useful for enforcing org standards.

## Customizing Backlog Categories

The default backlog tracks features with statuses: `queued`, `ready`, `trying`, `adopted`, and `skipped`. You can add custom categories for your org.

### Adding Org-Specific Features to the Backlog

If your org has specific tools or workflows you want everyone to adopt, create `${CLAUDE_PLUGIN_DATA}/org-backlog-additions.md`:

```markdown
## Org Features

| Feature | Status | Priority | Added | Notes |
|---------|--------|----------|-------|-------|
| GitHub MCP server | ready | high | 2025-01-01 | Required for all engineers |
| Team CLAUDE.md template | ready | high | 2025-01-01 | Copy from wiki |
| Pre-commit lint hook | ready | medium | 2025-01-01 | Prevents CI failures |
```

These items are merged into the user's backlog display and included in recommendations.

## Deploying to Your Team

### Option 1: Fork and Customize

1. Fork the plugin repository
2. Add your org-context, scoring overrides, and custom skills
3. Publish to your org's plugin marketplace
4. Team members install with `/plugin install your-org/cc-level-up`

### Option 2: Layer on Top

1. Have team members install the base cc-level-up plugin
2. Distribute org-specific config files separately (org-context.md, scoring overrides)
3. Team members place these in their `${CLAUDE_PLUGIN_DATA}/` directory

### Option 3: Managed Distribution

1. Include cc-level-up in your team's standard CC setup script
2. Pre-populate `${CLAUDE_PLUGIN_DATA}/` with org files during setup
3. Use the session-start hook to keep team members informed about new org requirements

## Tips for Org Adoption

- Start with a minimal org-context.md and expand over time
- Do not require Level 3+ features immediately — let people progress naturally
- Use the `/cc-teach` skill to generate onboarding materials from your best setup
- Review the aggregated usage-log.jsonl data (with user consent) to understand which skills are used most and where people get stuck
- Run a monthly "CC office hours" where advanced users share tips — capture these as learnings
