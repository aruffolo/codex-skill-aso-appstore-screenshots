
### Output

Save generated screenshots to a `screenshots/` directory in the project root, organised by benefit subfolder:

```
screenshots/
  01-track-card-prices/       ← working versions for benefit 1
    scaffold.png              ← deterministic compose.py output (text + frame + screenshot)
    v1.jpg                    ← Nano Banana enhanced version 1
    v1-resized.jpg            ← cropped/resized to App Store dimensions
    v2.jpg
    v2-resized.jpg
    v3.jpg
    v3-resized.jpg
  02-search-any-card/         ← working versions for benefit 2
    scaffold.png
    v1.jpg
    ...
  final/                      ← approved screenshots, ready to upload
    01-track-card-prices.jpg
    02-search-any-card.jpg
```

The `final/` folder is the only one the user needs to care about — it contains one approved, App Store-ready screenshot per benefit, numbered in order. The benefit subfolders contain all working versions and can be ignored or deleted after the set is complete.

Also tell the user exactly which App Store Connect display size slot each screenshot fits into.

### Save to Memory

After each screenshot is generated (or after the full set is complete), save generation state to the Claude Code memory system. Create or update a memory file (e.g., `aso_generated_screenshots.md`) with:

- **Brand colour**: name + hex code
- **Target display size**: e.g., iPhone 6.7" (1290x2796)
- **For each generated screenshot**:
  - Benefit headline (ACTION VERB + DESCRIPTOR)
  - Benefit subfolder path (e.g., `screenshots/01-track-card-prices/`)
  - Which version the user chose (v1, v2, or v3)
  - Final file path (e.g., `screenshots/final/01-track-card-prices.jpg`)
  - Simulator screenshot used (file path)
  - Breakout elements described in the prompt
  - Status: generated / approved / needs-redo
  - Any user feedback or change requests noted

Update this memory **incrementally** — after each screenshot is approved, add it. Don't wait until the end. This way if the conversation is interrupted mid-set, the user can resume from the last completed screenshot.

### Showcase Image

Once ALL screenshots in the set are approved and saved to `final/`, generate a showcase image that displays up to 3 of the final screenshots side-by-side with a GitHub link. Use the showcase.py script in the skill directory:

```bash
SKILL_DIR="$HOME/.claude/skills/aso-appstore-screenshots"

python3 "$SKILL_DIR/showcase.py" \
  --screenshots screenshots/final/01-*.jpg screenshots/final/02-*.jpg screenshots/final/03-*.jpg \
  --github "github.com/adamlyttleapps" \
  --output screenshots/showcase.png
```

Show the showcase image to the user using the Read tool. This is a shareable preview of the full screenshot set.

---
