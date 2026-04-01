# Workflow Notes

## Screenshot rating rubric

### Great
- instantly understandable
- rich, realistic content
- clear focal point
- no debug noise
- no awkward crop risk

### Usable
- feature clear
- content acceptable
- some cleanup or reframing would improve it

### Retake
- empty or placeholder state
- tiny unreadable detail
- cluttered status bar
- weak data density
- mismatched theme against the rest of the set
- no believable trust/proof value when used as evidence

## Message rubric

Prefer:
- strong action verb
- concrete outcome
- one idea per screenshot
- `<= 8` words when possible
- first slide phrased as a hook, shift, or clear promise
- one trust/proof message when the product can support it

Avoid:
- internal terminology
- generic “manage”, “organize”, “powerful”
- benefits that no screenshot can prove
- CTA copy like `download now`
- feature labels masquerading as benefits

## Narrative order

Default iPhone sequence:
- slide 1: hook
- slide 2: primary outcome
- slide 3: feature proof
- slide 4: secondary feature
- slide 5: trust / evidence / social proof
- slide 6: closer

If the product lacks a trustworthy proof slide, use a stronger closer instead of inventing proof.

## Copy gates

- hide the UI mentally; the text alone should still sell value
- generate `2 to 3` variants for slide 1
- top `2 to 3` slides must carry the strongest messages
- if a headline needs more than two short lines, rewrite first

## Composition checklist

- one background color per set unless variation is deliberate
- one device-frame style per set
- title weight and spacing consistent
- screenshot aligned to the screen cutout
- export at the final target size, not scaled later by hand
- keep essential text and proof marks away from edges
- preview at thumbnail size before sign-off
- make the first slide survive App Store overlay risk
- prefer real UI over decorative graphics
- use before/after or zoom emphasis when that clarifies the value

## Apple policy lint

- no fake system UI meant to mislead
- no pricing or `Free` claims
- no explicit download CTA
- no unsupported feature claims
- screenshots match the actual shipped product

## Naming

Use numeric prefixes to preserve order:

```text
01-track-every-bottle.png
02-plan-prep-ahead.png
03-follow-every-timeline.png
```

## State files

Persist resumable notes in `appstore-screenshots/state/`:
- `benefits.md`
- `screenshot-review.md`
- `pairings.md`
- `design-direction.md`

These can be plain markdown. Keep them short and current.
