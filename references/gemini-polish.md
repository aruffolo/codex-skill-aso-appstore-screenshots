# Gemini Polish Workflow

Use this only when the user explicitly wants AI-polished screenshot variants and Gemini MCP or equivalent Gemini-compatible image editing is available.

## Preconditions

- deterministic scaffold already generated
- final export size already locked
- user understands Gemini usage may incur API charges
- image generation or image editing tooling is actually available in the current Codex environment
- the Gemini integration can accept scaffold-based edit requests, not just text prompts

If any precondition is missing, stop at deterministic scaffolds.

## Variant Workflow

### First slide

For the first approved benefit:
- generate 3 polished variants from the scaffold
- keep text layout locked
- keep screenshot content locked
- polish device rendering, lighting, depth, and presentation
- avoid redesigning the campaign system
- if the environment supports parallel image edits, run the 3 variants in parallel

Ask the user to choose a winner. Save the chosen file path in `appstore-screenshots/state/style-template.md`.

### Later slides

For later benefits:
- keep the new slide's scaffold text and screenshot layout
- match the approved style template's frame treatment, lighting, material feel, and overall campaign finish
- generate 3 variants again unless the user asks for fewer
- if parallel image edits are available, use them

### Iteration

When the user requests revisions:
- preserve the chosen style template
- preserve screenshot content
- preserve text hierarchy
- describe only the requested changes

Then generate 3 new variants again if the user is still exploring. If the user asks for a narrow fix, one variant is acceptable.

## Suggested Prompt Shape

Use prompts with these ingredients:
- the scaffold is the layout source of truth
- preserve headline placement and screenshot content
- improve realism and premium App Store finish
- keep the same device frame treatment across the set
- avoid changing the screen shown inside the device

For later slides, add:
- match the visual treatment from the approved style template

## Output Naming

Inside each slide work directory:

```text
01-benefit-slug/
  scaffold.png
  v1.png
  v2.png
  v3.png
  v1-resized.png
  v2-resized.png
  v3-resized.png
```

Copy only the approved result into `final/`.

## Resize Rule

Any Gemini-polished image that does not land at the final App Store size must be cropped or resized before user review of final candidates.

Keep final approved files at the requested export size.
