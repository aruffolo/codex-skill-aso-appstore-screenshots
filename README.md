# Codex Skill: ASO App Store Screenshots

Create App Store screenshot sets from an app codebase plus existing app screenshots.

This repository is a Codex adaptation of Adam Lyttle's original Claude skill, [`claude-skill-aso-appstore-screenshots`](https://github.com/adamlyttleapps/claude-skill-aso-appstore-screenshots). The workflow, framing, and deterministic composition approach are based on that original work, then adapted here for Codex and pre-existing screenshot inputs.

This skill helps Codex:
- discover strong screenshot messages
- review and rate supplied app screenshots
- coach simulator or manual retakes when supplied screenshots are weak
- pair screenshots to benefits
- choose a visual direction
- compose App Store-ready PNG scaffolds
- optionally generate Gemini-polished variants from those scaffolds
- export a simple showcase image

No Figma required. No simulator automation required.

## Install

Clone or copy this repo into:

```bash
~/.codex/skills/aso-appstore-screenshots
```

## Requirements

- Python 3
- Pillow

Install:

```bash
python3 -m pip install Pillow
```

For optional Gemini polish mode:

- a Gemini MCP server or equivalent Gemini-compatible image editing integration available to Codex
- any required Gemini API credentials configured for that integration

Gemini polish is optional and may incur API charges. Deterministic scaffold mode does not require Gemini.

Optional, for validating the skill structure:

```bash
python3 -m pip install PyYAML
```

## Use

Invoke from Codex with:

```text
$aso-appstore-screenshots
```

Example:

```text
Use $aso-appstore-screenshots to turn my existing app screenshots into 5 App Store screenshots.
```

## What the skill does

1. Inspect the app codebase and draft ASO benefit headlines
2. Review provided screenshots and rate them `Great`, `Usable`, or `Retake`
3. Coach retakes with explicit instructions when screenshots are weak
4. Pair screenshots to the approved messages
5. Lock colors, font, and visual direction
6. Generate deterministic App Store screenshot scaffolds
7. Optionally generate Gemini-polished variants from those scaffolds
8. Build a showcase image for review

## Modes

### Deterministic scaffold mode

Default.

- local scripts only
- no Gemini dependency
- safest recovery path

### Gemini polish mode

Optional.

- starts from the deterministic scaffold
- generates polished variants for review
- keeps the approved scaffold layout as the source of truth
- works best when a Gemini MCP image-edit workflow is available
- should be used only when the user explicitly wants AI polish

### Retake coach mode

Optional, but recommended when supplied screenshots are weak.

- identifies screenshots that should be retaken
- tells the user exactly what screen to capture instead
- specifies the state/data that should be visible
- calls out clutter, clipping, and thumbnail-legibility problems

## Scripts

- `scripts/generate_frame.py` — generate the reusable device frame
- `scripts/compose.py` — compose one screenshot scaffold
- `scripts/showcase.py` — create a side-by-side preview

The frame generator now defaults to a plain frame. Use `--dynamic-island` only when the user explicitly wants it.

## Output Structure

```text
appstore-screenshots/
  state/
    benefits.md
    screenshot-review.md
    pairings.md
    design-direction.md
    retake-plan.md
    style-template.md
    polish-decisions.md
  work/
    01-benefit-slug/
      scaffold.png
      v1.png
      v2.png
      v3.png
      v1-resized.png
      v2-resized.png
      v3-resized.png
  final/
    01-benefit-slug.png
  showcase.png
```

## Validation

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/aso-appstore-screenshots
```

## Attribution

- Original creator: Adam Lyttle
- Original repository: [`adamlyttleapps/claude-skill-aso-appstore-screenshots`](https://github.com/adamlyttleapps/claude-skill-aso-appstore-screenshots)
- This repository: Codex adaptation for screenshot-input workflows without simulator dependency

## License

MIT. See [LICENSE](LICENSE). Keep Adam Lyttle's copyright and license notice with substantial copies or adaptations.
