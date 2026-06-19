# Hatz.ai Agent Build Lessons Learned

Use these notes when building future Hatz.ai agents, workflows, and apps from this repo or from the reusable `framework/agent-blueprint/` pattern.

## What worked

1. **Compact rollout folders work better than full-repo scans.**
   - Give Hatz a small `rollout/<agent-name>/` folder first.
   - Include a `READ-ME-FIRST.md`, app manifest, runtime instructions, output contract, output mapping, examples, readiness gates, and rollout prompt.

2. **Raw GitHub URLs can work, but Hatz tooling may be inconsistent.**
   - Public GitHub files may be reachable by browser/curl while Hatz tools still fail to ingest them.
   - Treat this as a Hatz tool/network limitation, not automatically as a repo privacy issue.

3. **Manual paste fallback is necessary.**
   - Keep a copy-paste-ready combined instruction block available.
   - If Hatz cannot fetch files, paste the runtime instructions and output contract directly into the app.

4. **Hatz app input variables must be explicitly referenced.**
   - Use `{{inputs.<field_name>}}` in Hatz prompts.
   - For this RFQ app, use `{{inputs.rfq_text}}` and `{{inputs.sources}}`.
   - Do not assume Hatz automatically injects input fields into the model prompt.

5. **Machine-safe branch keys prevent routing failures.**
   - Use `status_key` for workflow branching.
   - Use `display_status` only for human-readable output.
   - Avoid branching on punctuation-sensitive labels like em dashes, smart quotes, slashes, or long prose.

6. **Validate the app before building the workflow.**
   - First prove the app receives actual user input.
   - Run the Ready, Stop, and Clarification tests at the app level before workflow setup.

7. **Validate the workflow separately.**
   - After app tests pass, create the workflow.
   - Branch only on `status_key`.
   - Confirm all three branches route correctly.
   - Confirm human review gates and evidence capture run after routing.

8. **Hatz app builds and workflow builds may use different tool paths.**
   - Hatz Workshop/API tools may create and test an app but still be unable to create conditional workflows, human review gates, or evidence/audit steps.
   - Treat app completion and workflow completion as separate milestones.
   - If workflow APIs are unavailable, generate a workflow config/checklist for manual Hatz UI setup.

9. **Do not accept premature blocker claims.**
   - Hatz should inspect its available tool capabilities before declaring a platform limitation.
   - Ask Hatz to distinguish between a hard platform blocker, missing documentation, missing permissions, and simply not knowing the correct tool path.
   - If native branching, review gates, or evidence steps cannot be created directly, ask Hatz to continue with the closest workable implementation: prompt checkpoints, simulated branch logic, review checkpoints, workflow item calls, and end-to-end tests.
   - Require Hatz to explain exactly what it built, what it simulated, what remains manual, and what evidence proves each path works.

## What to avoid

1. **Do not rely on local file paths inside Hatz.**
   - Hatz does not have the repo filesystem unless its tool explicitly checks it out.
   - Paths like `rollout/.../02-runtime-instructions.md` are references for humans, not guaranteed Hatz-readable file paths.

2. **Do not share GitHub tokens with Hatz.**
   - If the repo is public, Hatz should use public URLs.
   - If Hatz cannot fetch public files, use manual paste fallback instead of sharing credentials.

3. **Do not branch on display text.**
   - Display text may change punctuation or formatting.
   - Always branch on ASCII-safe keys like `READY_FOR_ESTIMATOR_REVIEW`.

4. **Do not accept “all tests passed” unless real input was provided.**
   - A Stop result from empty input only proves empty-input handling.
   - The Ready test must pass with actual `rfq_text` before the app is considered wired correctly.

5. **Do not mark the build complete at the app stage.**
   - A Hatz app can pass tests while the workflow, human review gate, and evidence capture are still unbuilt.
   - If Hatz says workflow creation is not available through API/tools, ask for proof of the attempted tool path and ask it to try alternate Workshop/workflow tools before falling back to manual JSON/config plus UI checklist.

## Required future-agent pattern

Every future Hatz agent package should include:

- `status_key` values for workflow branching.
- `display_status` values for human-readable output.
- Explicit Hatz input references like `{{inputs.<field_name>}}`.
- A compact rollout folder.
- A single-file or manual-paste fallback for Hatz ingestion failures.
- App-level test cases.
- Workflow-level routing tests.
- Human review gate requirements.
- Evidence capture schema.
- Readiness gates before broad rollout.

## Recommended future Codex skills

Create Codex skills or scripts that can automate these repeatable steps:

1. **Hatz rollout pack generator**
   - Inputs: agent name, input fields, statuses, guardrails, output sections.
   - Output: `rollout/<agent-name>/` with manifest, instructions, output mapping, examples, and read-me-first.

2. **Hatz single-file handoff generator**
   - Combines runtime instructions, output contract, variable syntax, branch keys, evidence schema, and tests into one paste-ready file.

3. **Hatz prompt auditor**
   - Checks for missing `{{inputs.<field_name>}}` references.
   - Checks for display-text branching.
   - Checks for missing `status_key` / `display_status` separation.
   - Checks for missing human review gate and evidence fields.

4. **Hatz sandbox test pack generator**
   - Creates Ready, Clarification, Stop, attachment-only, placeholder-only, multi-item, and readable-source test cases.

5. **Hatz workflow checklist generator**
   - Produces workflow steps, branch config, reviewer roles, blocked actions, evidence fields, and go/no-go checklist.
   - Includes direct build attempts, simulated/checkpoint workflow options, API/import config, and manual UI setup instructions because workflow APIs may not support branching, review gates, or evidence capture.

6. **Hatz ingestion fallback helper**
   - Verifies raw GitHub URLs with `curl`.
   - Generates CDN/raw/blob fallback links.
   - Generates manual paste instructions if Hatz cannot fetch files.

## Current RFQ app lessons to preserve

- Hatz app ID created during sandbox build: `6210edff-a154-430a-b079-fb46fbea2c2b`.
- Hatz input syntax discovered: `{{inputs.rfq_text}}` and `{{inputs.sources}}`.
- The app passed three app-level tests after input variable references were fixed:
  - `READY_FOR_ESTIMATOR_REVIEW`
  - `STOP_REQUIRED_INFORMATION_MISSING`
  - `NEEDS_CLARIFICATION`
- Remaining work after app tests: workflow creation, human review gate, evidence capture, and workflow-level route testing.
- Hatz initially reported that workflow branching, human review gates, and evidence capture could not be created through the available Workshop/API tools, but later acknowledged it had not fully checked available tool capabilities. Future Hatz prompts should require it to continue the build, test alternate tools, simulate unsupported steps when needed, and clearly separate true blockers from uncertainty.
