# Repository Audit and Cleanup

## Cleanup decision

The repository now separates the Quick RFQ implementation from reusable agent-building framework material and Hatz handoff artifacts.

## What was noise

- Root-level original build-pack zip and checksum duplicated the preserved source package under `docs/source-package/`.
- Root-level `.gitkeep` did not carry product or build value.
- Build summary belonged with archive/source context, not the repository root.

## What changed

- Removed the original root zip and checksum after preserving the source package in `docs/source-package/quick-rfq-summary-app-v1.5/`.
- Removed root `.gitkeep`.
- Moved the original build-pack summary into `docs/archive/`.
- Added `framework/agent-blueprint/` so future agents can reuse the same implementation pattern without copying Quick RFQ-specific content.

## Efficient repo layers

| Layer | Path | Purpose |
|---|---|---|
| Runtime package | `src/hatz_quick_rfq/` | Deterministic local implementation, Hatz adapter, validation helpers. |
| Tests | `tests/` | Verifies runtime behavior and guardrails. |
| Product authority | `docs/source-package/quick-rfq-summary-app-v1.5/` | Read-only source package for v1.5 behavior. |
| Hatz setup docs | `docs/hatz-*`, `docs/deployment/` | App manifest, output mapping, rollout instructions, transferability notes. |
| Hatz handoff | `rollout/` | Compact package and zip for Hatz to read directly. |
| Working prompts | `notes/` | Prompts for Hatz discovery, repo reading, rollout, and support questions. |
| Reusable framework | `framework/agent-blueprint/` | Template for reproducing additional agents later. |
| Evidence | `evidence/` | Placeholder for QA, pilot, issue, and release records. |

## Keep vs. remove policy

Keep:

- Source authority files.
- Runtime code and tests.
- Hatz rollout package.
- Reusable framework files.
- Evidence templates and docs.

Avoid adding:

- Duplicate root archives.
- Generated caches.
- Unreviewed broad-use claims.
- Platform-specific assumptions not confirmed by Hatz support.
