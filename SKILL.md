---
name: aso-appstore-screenshots
description: "Create App Store screenshot campaigns from app code and screenshots."
---

# ASO App Store Screenshots

Follow Adam Lyttle's original workflow, disclosed one phase at a time. The preserved source and scripts are in `upstream/`; [UPSTREAM.json](UPSTREAM.json) records their revision, hashes, and exact phase ranges. Do not load the full source during normal campaign work.

First read [Codex state](references/codex.md), [original principles](references/phases/principles.md), and [original recall](references/phases/recall.md). Recover saved decisions before choosing a phase. Keep the campaign's brief, approvals, and current phase in the parent agent.

## Load only the current phase

For any generation or delivery phase, also read [Codex execution](references/execution.md). Every generation phase requires the [original format](references/phases/generation-design.md), including on resume; retain approved choices rather than reopening setup.

- **Discovery:** read [original benefit discovery](references/phases/benefits.md). Delegate codebase/metadata investigation through [research](references/research.md); use its concise report to refine benefits with the user. Add competitor research only when useful or requested.
- **Pairing:** read [original screenshot pairing](references/phases/pairing.md). Inspect the actual screenshots yourself; preserve the original benefit and pairing approval gates.
- **Generation setup:** read [automatic brand colour](references/phases/generation-colour.md) and [delivery requirements](references/delivery.md). Resolve the image provider and target sizes before rendering.
- **Scaffold:** read [original scaffold process](references/phases/generation-scaffold.md). Run the preserved composer; retain the original creative direction.
- **Enhancement or revision:** read [original image prompts](references/phases/generation-enhance.md) together with [original crop/review/approval steps](references/phases/generation-review.md). Preserve the scaffold, approved style image, and revision reference roles. Load [OpenAI execution](references/openai.md) only when that provider is selected.
- **Delivery:** read [original output/state/showcase](references/phases/generation-delivery.md) and [delivery requirements](references/delivery.md). Persist each approval immediately; showcase only approved finals.

## Delegation and context

Research always runs in a fresh subagent. Read its short findings and report path, not its transcript. If delegation is unavailable, report the research blocker and continue only work independent of it; do not silently research inline.

Keep benefit judgment, screenshot selection, art direction, image generation, and user approvals in the parent. A separate visual QA agent is useful for a large batch or requested independent review; give it only approved requirements and candidate images, and request actionable findings. It must not redesign the campaign or approve on the user's behalf.

Save compact state at each phase boundary. On resumption, load state and the needed phase rather than every reference. Progressive disclosure avoids loading irrelevant material; it cannot remove instructions already read in the current conversation.

## Additive layer boundary

The original owns the creative workflow: specific verb-led benefits, strongest first slide, solid brand background, heavy consistent type, relevant complete-panel breakouts, three variants, reference-driven consistency, and explicit approvals. Codex mappings and current platform requirements are documented overrides; optional providers do not change that design.

Follow explicit requests for scaffolds only or another creative direction and record the deviation. Keep upstream files unchanged; fixes or new capabilities belong in separately named layers.
