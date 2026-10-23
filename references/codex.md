# Codex state and research layer

Map Claude memory to project state and broad investigation to a child agent. Preserve the original creative direction and approval gates. Resolve paths relative to this installed package, not a hardcoded Claude directory. For rendering and image-tool mappings, load [execution.md](execution.md) only when generation begins.

## Memory becomes project state

Map all upstream Claude memory reads/writes to `screenshots/state.md`, unless the campaign already has a state location. Reuse existing state rather than starting another copy. Recover it before codebase analysis and verify referenced files exist.

Keep the state concise:
- app, audience, context, current phase, pending question, next action
- confirmed benefits in order and their approval status
- screenshot-analysis path, approved pairings, and outstanding retakes
- chosen colour, font, provider, target sizes, and first approved style-image path
- per slide: input, chosen variant, final paths, approved/needs-redo status, and feedback
- research report path, source-check date, and decisions changed by evidence

Store detailed screenshot ratings in `screenshots/analysis.md` and research in `screenshots/research.md`; link them from state. Persist incrementally after approvals. Follow upstream recall and allow phase jumps; do not repeat discovery when approved decisions remain valid. If a revised input invalidates a pairing or output, mark the affected result for review.

## Research ownership

The subagent performs the discovery phase's broad code/metadata traversal and external evidence collection. The parent synthesizes its findings, asks missing market questions, and iterates the benefits. Do not repeat the same broad search in the parent. Use [research.md](research.md) for delegation and the bounded return contract.
