
## GENERATION

Once benefits and screenshot pairings are confirmed, generate the final App Store screenshots using Nano Banana Pro (via the Gemini MCP server).

### Prerequisites Check

Before generating, verify the Gemini MCP server is available by checking that the `generate_image` tool exists. If it is NOT available, tell the user:

```
⚠️ Gemini MCP server not detected. To generate screenshots, you need to set it up:

1. Install: npm install -g gemini-mcp
2. Add to your Claude Code MCP config (~/.claude/settings.json or project .mcp.json)
3. Restart Claude Code
4. Run this skill again

See: https://github.com/nicobailon/gemini-mcp for setup instructions.
```

Do NOT proceed with generation if the tool is unavailable.

### App Store Connect Dimensions

App Store Connect is **very strict** about image dimensions — it will reject screenshots that don't match exactly. The only accepted portrait sizes are:

| Display | Portrait | Landscape |
|---------|----------|-----------|
| iPhone 6.5" | 1242 x 2688px | 2688 x 1242px |
| iPhone 6.7" | 1290 x 2796px | 2796 x 1290px |
| iPhone 6.9" | 1320 x 2868px | 2868 x 1320px |

Default to **1290 x 2796px** (iPhone 6.7") unless the user specifies otherwise. Ask the user which size(s) they need. Up to 10 screenshots can be uploaded per display size.

**IMPORTANT — Aspect ratio mismatch**: Apple's required dimensions are narrower than standard 9:16 (~0.461 ratio vs 0.5625). Nano Banana generates at preset aspect ratios, so we generate **wider than needed** at 9:16 with 4K resolution, then **crop and resize** down to exact Apple dimensions in a post-processing step (see Step 4 below). This approach avoids stretching — we remove excess width instead.

### Screenshot Format Specification

Each screenshot follows this exact high-converting ASO format. **Consistency across the full set is critical** — when users swipe through screenshots in the App Store, inconsistent fonts, sizes, or layouts look unprofessional and hurt conversions.

**Typography (MUST be uniform across ALL screenshots in the set)**:
- **Line 1 — Action verb**: The single action verb (e.g., "TRACK", "SEARCH", "BOOST"). This is the BIGGEST, boldest text on the screenshot. White, uppercase, center-aligned. Same font, same size, same weight on every screenshot.
- **Line 2 — Benefit descriptor**: The rest of the headline (e.g., "TRADING CARD PRICES", "ANY VERSE IN SECONDS"). Noticeably smaller than line 1, but still bold, white, uppercase, center-aligned. Same font, same size, same weight on every screenshot.
- **Font**: Heavy/black weight sans-serif (e.g., SF Pro Display Black, Inter Black, or similar high-impact font). Not just bold — heavy/black weight for maximum impact.
- **Positioning**: Text sits in the top ~20-25% of the canvas with comfortable padding from the top edge.
- **Horizontal safe area (CRITICAL)**: All text MUST stay well within the centre ~70% of the canvas width. Leave generous horizontal margins on both sides — at least 15% padding from each edge. This is essential because the post-processing step crops the sides of the image to convert from 9:16 to Apple's narrower aspect ratio. Any text near the left or right edges WILL be cut off. Keep headlines short enough to fit comfortably within this safe zone. If a headline is too long, break it across more lines rather than extending to the edges.

**Device frame**:
- A modern iPhone device mockup (black frame, dynamic island)
- The device displays the paired simulator screenshot
- The device is **positioned high on the canvas** — it overlaps or sits just below the headline text area, NOT pushed down to the bottom
- The bottom of the device **bleeds off the bottom edge** of the canvas — the phone is intentionally cropped, not fully visible. This creates a dynamic, modern feel.
- The device is centered horizontally

**Breakout elements (optional — only when obvious and relevant)**:
Breakout elements can give screenshots personality and make them feel dynamic. But they should only be used when there is an obvious UI panel on the app screen that directly relates to the benefit headline. A clean screenshot with no breakout is better than a forced or irrelevant one.

- **Primary — Feature zoom-out (only when relevant)**: If there is an obvious, visually compelling entire UI panel or grouped section on the app screen that directly reinforces the benefit headline, make it "pop out" from the device frame. The panel must stay at the same vertical position and orientation as where it appears on the app screen — NOT rotated or angled. It should extend dramatically beyond BOTH left and right edges of the device frame, clearly overlapping the phone bezel on both sides, expanding to nearly the full width of the screenshot canvas. The panel must be SCALED UP significantly — much larger than it appears on the phone screen — so that it extends well beyond both left and right edges of the device frame. It should look like it is floating in front of the phone at a larger scale, bursting out of the phone's boundaries. Add a soft drop shadow beneath the breakout panel to create depth and make it feel like it's hovering above the device. The enlarged size plus the overlap with the device frame edges plus the shadow is what creates the dramatic pop-out effect. The panel must be a complete card/section (not an individual button, icon, or small element). If no panel clearly relates to the headline, skip the breakout entirely.
- **Secondary — Supporting elements (OPTIONAL, use restraint)**: You may add 1-2 small supporting elements (contextual icons, subtle directional cues, small floating UI elements) ONLY if they are directly relevant to the benefit and enhance the story. These must NOT compete with the primary zoom-out element for attention. Less is more — a clean composition with one strong breakout element is better than a cluttered one with many. Every element added must earn its place by helping tell the story of that screen.

**What to avoid**: Don't add decorative elements just because you can. No random icons, no excessive particles/sparkles, no elements unrelated to the benefit. The screenshot should feel polished and intentional, not busy.

**Background (MUST be consistent across ALL screenshots in the set)**:
- Solid bold brand colour fills the entire canvas — same colour on every screenshot
- The background must be a clean, solid brand colour. Do NOT add glows, gradients, radial patterns, or light effects.
- If accent shapes are used, use the same style of accent on every screenshot so the set looks like a cohesive series when viewed side-by-side
