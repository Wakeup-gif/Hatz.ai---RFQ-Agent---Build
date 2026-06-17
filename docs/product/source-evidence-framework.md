# Quick RFQ Summary App v1.5 — Source Evidence Framework

## 1. Purpose

This framework prevents unsupported facts from entering the RFQ Intake Summary.

It defines what the app may treat as evidence.

## 2. Evidence classes

### Reviewed content

Content is reviewed only when the user provides readable content in the current interaction.

Examples:

- pasted customer email,
- pasted RFQ notes,
- readable attachment text,
- transcribed drawing notes,
- pasted sign schedule rows,
- pasted prior quote scope,
- user-provided revision notes.

### Referenced but not reviewed

A source is referenced but not reviewed when it is mentioned but its readable contents are not provided.

Examples:

- "see attached drawings",
- "per sign schedule",
- "attached PDF",
- "revised drawings",
- "prior quote",
- file name only,
- photo mentioned but not described.

Required phrase when relevant:

```text
Attachment mentioned but contents not provided.
```

### Non-evidence

The app must not treat these as confirmed facts:

- file names,
- attachment names,
- prior conversation memory,
- assumed customer history,
- default template placeholders,
- bracketed placeholders,
- unstated business norms,
- outside knowledge.

File names may be listed only as files mentioned.

## 3. Source handling order

Use this order:

```text
1. Identify what content is readable in the current interaction.
2. Identify what files or sources are merely referenced.
3. Extract facts only from reviewed content.
4. List referenced-but-not-reviewed sources separately.
5. Mark missing source-dependent facts as missing.
```

## 4. Output implication

In `## 3. Sources Reviewed`, use:

```text
Reviewed content:
- [Only readable/provided content]

Referenced but not reviewed:
- [Mentioned but unreadable or not provided]
```

Do not list a drawing, photo, schedule, addendum, artwork file, or prior quote as reviewed unless readable content was provided in the current interaction.

## 5. File-name trap

If the input says:

```text
Final_Approved_ChannelLetters_120in_Black.pdf
```

the app may say:

```text
Referenced but not reviewed:
- File mentioned: Final_Approved_ChannelLetters_120in_Black.pdf
- Attachment mentioned but contents not provided.
```

The app may not treat these as known facts unless also stated in readable content:

- final,
- approved,
- channel letters,
- 120 in,
- black.
