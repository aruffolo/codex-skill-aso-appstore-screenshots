# Codex Skill: ASO App Store Screenshots

Create App Store screenshot sets from an app codebase plus existing app screenshots.

This repository is a Codex adaptation of Adam Lyttle's original Claude skill, [`claude-skill-aso-appstore-screenshots`](https://github.com/adamlyttleapps/claude-skill-aso-appstore-screenshots). The workflow, framing, and deterministic composition approach are based on that original work, then adapted here for Codex and pre-existing screenshot inputs.

This skill helps Codex:
- discover strong screenshot messages
- review and rate supplied app screenshots
- pair screenshots to benefits
- choose a visual direction
- compose App Store-ready PNG scaffolds
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
3. Pair screenshots to the approved messages
4. Lock colors, font, and visual direction
5. Generate deterministic App Store screenshot scaffolds
6. Build a showcase image for review

## Scripts

- `scripts/generate_frame.py` — generate the reusable device frame
- `scripts/compose.py` — compose one screenshot scaffold
- `scripts/showcase.py` — create a side-by-side preview

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
