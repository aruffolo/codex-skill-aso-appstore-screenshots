
**Step 3: IMMEDIATELY crop and resize ALL 3 versions to App Store dimensions**

⚠️ **You MUST run this immediately after all 3 `edit_image` calls complete. Do NOT show the user any image before running this. The raw Nano Banana output is always the wrong dimensions for App Store Connect.**

**CRITICAL — Use exactly ONE Bash tool call for all 3 crop/resize operations.** Do NOT make 3 separate Bash calls. Do NOT use parallel Bash calls. Use the single loop below so the user only sees one permission prompt:

```bash
TARGET_W=1290 && TARGET_H=2796 && \
for INPUT in screenshots/01-[benefit-slug]/v1.jpg screenshots/01-[benefit-slug]/v2.jpg screenshots/01-[benefit-slug]/v3.jpg; do
  OUTPUT="${INPUT%.jpg}-resized.jpg"
  cp "$INPUT" "$OUTPUT"
  W=$(sips -g pixelWidth "$OUTPUT" | tail -1 | awk '{print $2}')
  H=$(sips -g pixelHeight "$OUTPUT" | tail -1 | awk '{print $2}')
  CROP_W=$(python3 -c "print(round($H * $TARGET_W / $TARGET_H))")
  OFFSET_X=$(python3 -c "print(round(($W - $CROP_W) / 2))")
  sips --cropOffset 0 $OFFSET_X --cropToHeightWidth $H $CROP_W "$OUTPUT"
  sips -z $TARGET_H $TARGET_W "$OUTPUT"
  echo "--- $OUTPUT ---"
  sips -g pixelWidth -g pixelHeight "$OUTPUT"
done
```

The script crops to the correct aspect ratio (top-center aligned — sides trimmed equally, top edge preserved so the headline stays put) and resizes to exact pixel dimensions. The resized image is saved as a separate file with `-resized.jpg` appended.

Target dimensions per display size — adjust `TARGET_W` and `TARGET_H`:
- iPhone 6.5": `TARGET_W=1242 TARGET_H=2688`
- iPhone 6.7" (default): `TARGET_W=1290 TARGET_H=2796`
- iPhone 6.9": `TARGET_W=1320 TARGET_H=2868`

**Step 4: Review all 3 versions with the user**

Present all 3 **resized** versions (the `-resized.jpg` files) to the user using the Read tool. Never show the raw Nano Banana output — always show the post-processed versions.

Label them clearly as **Version 1**, **Version 2**, and **Version 3** and ask the user to pick their favourite or request changes.

**Step 5: Iterate if needed**

If the user wants changes, use `edit_image` with **three images** as input:
1. The **scaffold** (`scaffold.png`) — anchors the layout (text position, device placement, screenshot)
2. The **style template** (the first approved screenshot from `screenshots/final/01-*.jpg`) — defines the device frame rendering and overall visual style that must be consistent across the entire set
3. The **approved design** (the version the user liked best for this specific screenshot) — anchors the creative direction and breakout element approach

The prompt should reference all three:
```
Here are three reference images, each with a distinct purpose:

- FIRST image: The SCAFFOLD — use this as the definitive guide for layout: text position, device frame placement, and the app screenshot on screen. This defines WHERE everything goes.
- SECOND image: The STYLE TEMPLATE — this is the first approved screenshot in the set. The device frame rendering, text treatment, and overall visual style MUST match this exactly. This defines HOW the screenshot should look to maintain consistency across the set.
- THIRD image: The APPROVED DESIGN DIRECTION — this is the version the user liked best for this specific screenshot. Match its creative direction, breakout element approach, and secondary elements.

Generate a new version that keeps the layout from the scaffold, the device frame and visual style from the style template, and the creative direction from the approved design, with these changes:
[USER'S REQUESTED CHANGES]
```

This prevents drift (scaffold keeps layout locked), maintains set-wide consistency (style template keeps device frame and visual treatment identical), and preserves the creative direction the user already approved.

When iterating, generate **3 versions in parallel** again (3 parallel `edit_image` calls in a single message). Then **immediately run the Step 3 crop/resize loop on all 3 in a single Bash call** before showing the user.

Repeat until the user is happy.

**Step 6: Copy approved version to `final/`**

Once the user picks a winner, copy the resized version to `screenshots/final/`:

```bash
mkdir -p screenshots/final
cp "screenshots/01-[benefit-slug]/v2-resized.jpg" "screenshots/final/01-[benefit-slug].jpg"
```

This keeps `final/` clean — only approved, App Store-ready screenshots, one per benefit, numbered in order. Then move to the next benefit.
