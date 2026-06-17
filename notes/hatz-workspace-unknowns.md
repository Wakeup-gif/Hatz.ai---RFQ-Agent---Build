# Hatz Workspace Unknowns

These notes capture deployment variables that the repo cannot answer without customer/Hatz workspace data. Keep this list separate from the implementation so engineering can continue building generic scaffolding while project owners gather the missing operational inputs.

## Inputs needed before Hatz rollout

- Actual Hatz routing/trigger format.
- Which users/teams receive reviews.
- Permission groups and identity provider.
- Storage backend and retention rules.
- Logging/metrics destination.
- Redaction policy.
- Attachment extraction/OCR/file-type support.
- Audit log destination and reviewer identity requirements.
- Versioning and rollback process.

## How this list is used

- Convert each item into a concrete deployment decision before setting `ready_for_hatz` to `true`.
- Record final answers in deployment documentation or release-decision evidence.
- Do not infer these values from defaults or assumptions; they must come from the customer/Hatz workspace owner.
