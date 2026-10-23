
## BENEFIT DISCOVERY (Most Critical Phase)

This phase sets the foundation for everything. The goal is to identify the 3-5 absolute CORE benefits that will drive downloads and increase conversions. Do not rush this.

**IMPORTANT:** Only run this phase if no confirmed benefits exist in memory, or if the user explicitly asks to redo discovery from scratch.

### Step 1: Analyze the Codebase

Explore the project codebase thoroughly. Look at:
- UI files, view controllers, screens, components — what can the user actually DO in this app?
- Models and data structures — what domain does this app operate in?
- Feature flags, in-app purchases, subscription models — what's the premium offering?
- Onboarding flows — what does the app highlight first?
- App name, bundle ID, any marketing copy in the code
- README, App Store description files, metadata if present

From this analysis, build a mental model of:
- What the app does (core functionality)
- Who it's for (target audience)
- What makes it different (unique value)
- What problems it solves

### Step 2: Ask the User Clarifying Questions

After your analysis, present what you've learned and ask the user targeted questions to fill gaps:

- "Based on the code, this appears to be [X]. Is that right?"
- "Who is your target audience? (age, interests, skill level)"
- "What niche does this app serve?"
- "What's the #1 reason someone downloads this app?"
- "Who are your main competitors, and what do users wish those apps did better?"
- "What do your best reviews say? What do users love most?"

Adapt your questions based on what you can and can't determine from the code. Don't ask questions the code already answers.

### Step 3: Draft the Core Benefits

Based on your analysis and the user's input, draft 3-5 core benefits. Each benefit MUST:

1. **Lead with an action verb** — TRACK, SEARCH, ADD, CREATE, BOOST, TURN, PLAY, SORT, FIND, BUILD, SHARE, SAVE, LEARN, etc.
2. **Focus on what the USER gets**, not what the app does technically
3. **Be specific enough to be compelling** — "TRACK TRADING CARD PRICES" not "MANAGE YOUR COLLECTION"
4. **Answer the user's unspoken question**: "Why should I download this instead of scrolling past?"

Present the benefits to the user in this format:

```
Here are the core benefits I'd recommend for your screenshots:

1. [ACTION VERB] + [BENEFIT] — [why this drives downloads]
2. [ACTION VERB] + [BENEFIT] — [why this drives downloads]
3. [ACTION VERB] + [BENEFIT] — [why this drives downloads]
...
```

### Step 4: Collaborate and Refine

DO NOT proceed until the user explicitly confirms the benefits. This is an iterative process:

- Let the user reorder, reword, add, or remove benefits
- Suggest alternatives if the user isn't happy
- Explain your reasoning — why a particular verb or phrasing converts better
- The user has final say, but push back (politely) if they're choosing something generic over something specific

### Step 5: Save to Memory

Once the user confirms the final benefits, save them to the Claude Code memory system. Create or update a memory file (e.g., `aso_benefits.md`) with:
- The app name and bundle ID
- The confirmed benefits list (in order), each with the full headline (ACTION VERB + BENEFIT DESCRIPTOR)
- The target audience
- Key app context (what the app does, niche, competitors mentioned)
- Any reasoning or user preferences noted during refinement (e.g., "user prefers 'TRACK' over 'MONITOR'")

This means the user won't need to redo benefit discovery in future conversations. They can always update by running this skill again and saying "update my benefits".

---
