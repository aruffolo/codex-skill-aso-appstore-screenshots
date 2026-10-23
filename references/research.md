# Research subagent

Research is a delegated evidence task. It does not own campaign approvals or design.

Reuse an existing report when its evidence still answers the question; delegate a focused update for new products, changed requirements, or missing evidence. Broad app research belongs before benefit refinement. Current Apple specifications belong before locking delivery targets. Competitor research is conditional, not a prerequisite for every screenshot.

## Start a fresh child

Use the host's native subagent tool for ordinary same-provider work. Discover the live provider/model catalog when choosing a different model or using T3 delegation; use `delegate_task` for T3-owned/cross-provider work and retain its task ID. Inherit the current model unless the user requests another. Do not create a top-level conversation or a watcher. If delegation is unavailable, report the blocker and continue unrelated work only.

Send the smallest useful packet: the question, project root, app/category/locale if known, approved campaign constraints, relevant source paths or URLs, and the report destination. Do not send the parent transcript, full skill, image-generation prompts, credentials, or unrelated project data. The child may read the app code it needs; it does not need the creative workflow.

Use this brief, filling only the relevant scope:

> Research [question] for the ASO screenshot campaign in [project root]. Read relevant app code, metadata, and first-party evidence. Establish actual capabilities, audience clues, premium boundaries, and uncertainties needed for this question. For requested competitor work, use official listings and attributable review evidence; distinguish observation from inference. For delivery requirements, verify current official Apple documentation and supported platforms. Do not invent conversion statistics or treat design preferences as proven conversion wins.
>
> Write exactly one concise report to [project root]/screenshots/research.md, updating that report for follow-ups while preserving still-useful findings. Cite material facts with source URLs or local file/line references and include the check date. Keep the report under roughly 1,000 words, with focused findings, uncertainties, and source links. Do not edit app code, generate images, approve benefits, change campaign state, install integrations, or delegate again. Return the report path, at most eight actionable findings, and unresolved questions.

Use the project's existing research location if one is already established. Retain the child's task/agent ID to inspect completion or cancel it if the question is superseded; do not duplicate active work. Continue available screenshot inspection while it runs. Read the report only when its findings are needed for the next decision, and copy only the evidence-backed decisions into campaign state.
