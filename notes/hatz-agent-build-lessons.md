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
