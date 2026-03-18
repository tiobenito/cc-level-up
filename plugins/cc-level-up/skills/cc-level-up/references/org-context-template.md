# Org Context Template

This file is a template that teams can customize with their organization's roles, tools, and conventions. It replaces the need for org-specific hardcoding in the skill itself.

**How to use:** Copy this template, fill in your org's details, and save it alongside the skill. The cc-level-up skill reads this file during the Build phase to personalize recommendations for each user's role.

If this file is not customized or not present, the skill works fine without it — it just asks the user directly instead of offering role-specific suggestions.

---

## Organization Info

**Org name:** [Your Company Name]
**What you do:** [1-2 sentence description of the business]
**Primary tools:** [e.g., Slack, GitHub, Jira, Notion, Salesforce, etc.]

---

## Role Definitions

For each role, define the CLAUDE.md flavor, suggested first skills, and suggested reference docs. Add or remove roles as needed.

### [Role Name 1]

**CLAUDE.md flavor:**
- "[Example: I'm a [Role] at [Company]. I [primary responsibilities].]"
- Key preferences: [e.g., concise summaries, data in tables, action items in bullets]

**Suggested first skills:**
- "[Skill name]" — [What it does in one sentence]
- "[Skill name]" — [What it does in one sentence]

**Suggested references:**
- [Doc type — e.g., template, glossary, process doc]
- [Doc type]

---

### [Role Name 2]

**CLAUDE.md flavor:**
- "[Example description]"
- Key preferences: [preferences]

**Suggested first skills:**
- "[Skill name]" — [description]
- "[Skill name]" — [description]

**Suggested references:**
- [Doc type]
- [Doc type]

---

### [Role Name 3]

**CLAUDE.md flavor:**
- "[Example description]"
- Key preferences: [preferences]

**Suggested first skills:**
- "[Skill name]" — [description]
- "[Skill name]" — [description]

**Suggested references:**
- [Doc type]
- [Doc type]

---

*Copy and paste the role block above to add more roles.*

---

## How This File Is Used

During Level 0 setup, the skill asks "What's your role?" and uses this file to:
1. Pre-fill the CLAUDE.md with a role-appropriate description
2. Suggest the most relevant first skill to build
3. Recommend starter reference documents

The user's own words always override these defaults — this is a starting point, not a prescription.

## Customization Tips

- **Be specific about roles.** "Engineer" is too broad. "Frontend Engineer" or "Backend Engineer" gives better suggestions.
- **Include real tool names.** If your Sales team uses Salesforce, say so — it helps the skill suggest relevant MCP connections for CLI users.
- **Keep skill suggestions practical.** The best first skills are things people do weekly that take 15+ minutes manually.
- **Update quarterly.** Roles shift, tools change, new hires join. Keep this file current.
