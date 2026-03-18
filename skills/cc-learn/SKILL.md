---
name: cc-learn
description: >
  Capture Claude Code articles, tips, features, and resources into a structured
  adoption backlog. Route new discoveries to the right format (backlog item vs.
  read-later entry) and surface what to work on next. Trigger when user says
  "help me learn this", "I want to try this", "add to backlog", "check this out",
  "here's an article about Claude Code", "remind me to try this", "add this feature",
  "what should I work on next", "show my backlog", "what's in my backlog",
  "anything stale in my backlog", or pastes a URL with Claude Code context.
  Also trigger when user shares CC-related content and wants to capture it for later.
  DO NOT trigger for general learning requests unrelated to Claude Code — e.g.,
  "help me learn Python", "teach me React", "I want to learn cooking". Only trigger
  when the content is about Claude Code features, configuration, workflows, skills,
  hooks, MCP servers, agents, commands, memory, or Claude Code productivity patterns.
---

# Learn — CC Discovery Capture

Capture Claude Code tips, articles, and features into a structured backlog so nothing gets lost and the user always knows what to try next.

## References

- `references/backlog-template.md` — Empty backlog template for new users

## Data Files

All persistent data lives in the plugin data directory:

- `${CLAUDE_PLUGIN_DATA}/backlog.md` — Structured adoption backlog (the main file)
- `${CLAUDE_PLUGIN_DATA}/discovery-log.md` — Raw chronological log of every URL, article, and tip captured

Read both files at the start of every invocation to understand current state.

---

## Mode Detection

Determine which mode to run based on the user's input:

### Mode 1: Capture (user provides content to save)

Triggers: user shares a URL, pastes article text, describes a CC feature, or says "add this", "save this", "remind me to try this".

### Mode 2: Review (user wants to see their backlog)

Triggers: "what should I work on next", "show my backlog", "what's queued", "anything stale".

### Mode 3: Update (user wants to change an existing item's status)

Triggers: "I tried X", "mark X as adopted", "drop X", "I'm trying X now".

---

## Mode 1: Capture

### Step 1: Extract the Content

If the user provides a **URL**:
1. Use WebFetch to read the URL
2. Extract the core content — what CC feature or practice is being described
3. Summarize in 2-3 sentences

If the user provides **article text or a tip** (pasted or described):
1. Read what they shared
2. Identify the CC feature, pattern, or practice

If the user provides a **vague reference** ("that thing about hooks"):
1. Ask one clarifying question to identify the specific feature
2. Do not proceed until you know what to capture

### Step 2: Classify the Discovery

Determine the type:

| Type | Description | Example |
|------|-------------|---------|
| **Feature** | A CC capability to adopt | "Agent teams for parallel work" |
| **Tip** | A technique or pattern to apply | "Use HEREDOC for commit messages" |
| **Resource** | Reference material to keep | "Official CC docs on hooks" |
| **Config** | A settings change to make | "Add keybinding for /commit" |

### Step 3: Write to Discovery Log

Append to `${CLAUDE_PLUGIN_DATA}/discovery-log.md`. Every capture gets logged here regardless of whether it becomes a backlog item.

Format:

```markdown
---
### YYYY-MM-DD — <Title>
- **Type:** feature | tip | resource | config
- **Source:** <URL or "conversation">
- **Summary:** <2-3 sentence description>
```

If the discovery log does not exist, create it with this header:

```markdown
# CC Discovery Log

Raw chronological log of every Claude Code article, tip, and feature captured.
Entries are append-only. See `backlog.md` for the structured adoption tracker.

---
```

### Step 4: Create Backlog Item (if actionable)

Not every discovery becomes a backlog item. Create one when:
- The discovery describes something the user can **try or adopt**
- It is a feature, tip, or config change (not just a reference article)

Do NOT create a backlog item when:
- It is purely reference material with no action to take
- The user already has the feature adopted (check existing backlog)
- It duplicates an existing backlog item (update the existing one instead)

Before creating a new item, read the existing backlog and check for duplicates by concept, not just by name.

Append to `${CLAUDE_PLUGIN_DATA}/backlog.md` using this format:

```markdown
### <Feature Name>
- **Status:** queued
- **Added:** YYYY-MM-DD
- **Last nudged:** never
- **Source:** <URL or "conversation">
- **Why:** <What this feature does and why it's worth trying>
- **Trigger:** <When Claude should push this — specific situations where it's relevant>
- **What success looks like:** <How you know you've adopted it — observable behavior change>
```

If the backlog file does not exist, create it using the template from `references/backlog-template.md`.

### Step 5: Confirm to User

Show what was captured:
- Title and type
- Whether it was added to the backlog (and if so, the trigger condition)
- Or just logged as a reference (and why)

Keep confirmation to 3-4 lines. Do not dump the full backlog item back at them.

---

## Mode 2: Review

### Step 1: Read the Backlog

Read `${CLAUDE_PLUGIN_DATA}/backlog.md`. If it does not exist, tell the user they have no backlog yet and offer to help them capture something.

### Step 2: Organize by Status

Present items in this order:

1. **Trying** — actively being tested (show these first, they need attention)
2. **Ready** — queued and ready to start (highlight any that have been ready for 2+ weeks as stale)
3. **Queued** — captured but not yet prioritized

Do not show `adopted` or `dropped` items unless the user specifically asks for them.

### Step 3: Highlight Stale Items

An item is stale if:
- Status is `ready` and `Last nudged` is more than 14 days ago (or `never` and `Added` is more than 14 days ago)
- Status is `trying` and `Last nudged` is more than 21 days ago

For stale items, flag them: "This has been sitting for a while. Want to start it, drop it, or keep it queued?"

### Step 4: Suggest Next Item

Based on current conversation context, suggest the most relevant backlog item to work on next. Consider:
- What the user is currently working on (if apparent from conversation)
- Items whose trigger condition matches the current situation
- Items with the shortest expected effort
- Freshness — newer items may be more exciting

If no context is available, suggest the oldest `ready` item or the highest-impact `queued` item.

### Step 5: Format the Review

```
## Your CC Learning Backlog

### Currently Trying (N)
- **<Name>** — <one-line why> (started <date>)

### Ready to Start (N)
- **<Name>** — <one-line why> (queued <date>) [STALE if applicable]

### Queued (N)
- **<Name>** — <one-line why>

---
**Suggestion:** Based on [reason], I'd recommend starting with **<Name>** next.
[One sentence about why now is a good time.]
```

---

## Mode 3: Update

### Step 1: Identify the Item

Match the user's reference to an existing backlog item. If ambiguous, list candidates and ask which one.

### Step 2: Apply the Status Change

Valid transitions:

| From | To | When |
|------|----|------|
| queued | ready | User says "I want to try this soon" |
| queued | dropped | User says "never mind", "not relevant" |
| ready | trying | User starts experimenting with the feature |
| ready | dropped | User decides it's not worth it |
| trying | adopted | User has integrated it into their workflow |
| trying | dropped | User tried it and it didn't work out |
| trying | ready | User paused but wants to come back to it |

Update the item's status and set `Last nudged` to today's date.

If the new status is `adopted`, congratulate briefly and note what they learned.

If the new status is `dropped`, ask for a one-line reason and append it to the item:
```markdown
- **Dropped reason:** <why>
```

### Step 3: Confirm

Show the updated item status in one line. Do not dump the full backlog.

---

## Edge Cases

- **Duplicate detection:** If the user tries to add something that already exists in the backlog, tell them it's already tracked and show its current status. Offer to update it instead.
- **Non-CC content:** If the user says "help me learn X" where X is not related to Claude Code, do NOT trigger this skill. Respond normally or suggest the right skill.
- **Empty backlog:** If backlog is empty and user asks "what should I work on next", suggest they start by capturing a few things they want to try. Offer examples based on their current setup level.
- **Bulk capture:** If the user shares multiple URLs or tips at once, process each one individually but present a summary table at the end rather than confirming each one separately.
