
### Determine Brand Colour (Automatic)

Do NOT ask the user to pick a background colour. Instead, determine the best one automatically:

1. **Analyse the codebase** — check for accent colours, tint colours, brand colours in asset catalogs, theme files, colour constants, Info.plist
2. **Study the simulator screenshots** — what are the dominant colours in the UI? What colour palette does the app use?
3. **Consider the app's domain and audience** — a game can go bold and playful, a finance app needs confident and trustworthy colours

**Pick a single colour that:**
- **Complements the screenshots** — makes the app screens pop, not clash. If the app UI is mostly white/light, use a bold saturated background for contrast.
- **Stops the scroll** — vibrant, bold, saturated. Muted or pastel colours get lost in the App Store.
- **Suits the app's personality** — match the energy of the app
- **Avoids pitfalls** — no white/light grey (disappears against App Store), avoid colours too close to the app UI's dominant colour

Present your choice with brief reasoning (e.g., "Using **#7B2D8E** (deep purple) — it complements your app's colourful UI and stands out at thumbnail size"). The user can override if they want, but don't present it as a question.

The brand colour is saved to memory in Step 0 of the generation process, before scaffolding begins.
