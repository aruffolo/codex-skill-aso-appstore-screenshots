## RECALL (Always Do This First)

Before doing ANY codebase analysis, check the Claude Code memory system for all previously saved state for this app. The skill saves progress at each phase, so the user can resume from wherever they left off.

**Check memory for each of these (in order):**

1. **Benefits** — confirmed benefit headlines + target audience + app context
2. **Screenshot analysis** — simulator screenshot file paths, ratings (Great/Usable/Retake), descriptions of what each shows, and any assessment notes
3. **Pairings** — which simulator screenshot is paired with which benefit
4. **Brand colour** — the confirmed background colour (name + hex)
5. **Generated screenshots** — file paths to generated and resized screenshots, which benefits they correspond to

**Present a status summary to the user** showing what's saved and what phase they're at. For example:

```
Here's where we left off:

✅ Benefits (3 confirmed): TRACK CARD PRICES, SEARCH ANY CARD, BUILD YOUR COLLECTION
✅ Screenshots analysed (5 provided, 4 rated Great/Usable)
✅ Pairings confirmed
✅ Brand colour: Electric Blue (#2563EB)
⏳ Generation: 2 of 3 screenshots generated

Ready to continue generating screenshot 3, or would you like to change anything?
```

**Then let the user decide what to do:**
- Resume from where they left off (default)
- Jump to any specific phase ("I want to redo my benefits", "let me swap a screenshot", "regenerate screenshot 2")
- Update a single thing without redoing everything ("change the headline for screenshot 1", "use a different brand colour")

**If NO state is found in memory at all:**
→ Proceed to Benefit Discovery.

---
