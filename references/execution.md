# Codex generation execution

These are platform mappings and known limits of the untouched renderer; they do not replace the original art direction.

## Paths and tools

Resolve `SKILL_DIR` to this installed package, not a hardcoded Claude directory. Upstream commands for `compose.py`, `generate_frame.py`, and `showcase.py` live under `$SKILL_DIR/upstream/`. Run them from the user's project, keeping campaign output under `screenshots/`. Replace Claude `Read`/`Bash` with available image inspection and shell tools. Follow the host's batching and authorization rules rather than upstream permission-prompt workarounds.

The original scripts require Python 3, Pillow, and SF Pro Display Black. Check that Pillow can actually load the requested font; a nonexistent absolute path may still resolve through the system font search. If it cannot, report the missing font and agree a font choice; do not silently substitute a tiny default. Preserve upstream scripts. A temporary working copy may configure an agreed font path without changing the snapshot.

The bundled composer renders only 1290×2796. Its device position is fixed; long text can overlap the phone, and prompt safe margins are stricter than the renderer enforces. Inspect each scaffold privately for clipping, overlap, and margin problems; shorten approved copy with the user's agreement when necessary. Do not present a broken scaffold as a finished slide. The bundled frame and its generator may differ: use the supplied asset unless a deliberate regeneration is needed, and generate into the project's working directory, never over the preserved snapshot.

## Image execution

Gemini/Nano Banana is the original default. Detect a working scaffold-based image-edit tool, not merely a tool named `generate_image`, and map actual tool arguments to the original reference-image roles. Do not install either of the conflicting upstream MCP setup examples blindly.

If Gemini is unavailable, explain the missing capability. Offer the separately loaded OpenAI path when available, or scaffolds only when the user chooses that deliverable. A failed prerequisite does not silently change the selected workflow. Record provider choice; do not imply any provider is universally included or free.

Generate the original three variants; parallelize when the tool permits, otherwise run them sequentially and preserve all three. The first approved final image is the style reference for later slides. A revision additionally includes the selected design for that slide. Save the actual image paths, not only a prose description of their treatment.

Postprocess every generated variant before review using the original aspect-preserving, top-centred crop and exact target dimensions. Use `sips` where available or equivalent Pillow operations; never stretch width and height independently. Keep scaffold PNGs and final JPEG/JPG files as upstream specifies, unless the user requests another accepted format.

For the showcase, omit upstream's example `--github` value unless the user wants that credit in the image. Keep author attribution and the MIT license in the package regardless. Do not insert another person's identity as campaign branding.
