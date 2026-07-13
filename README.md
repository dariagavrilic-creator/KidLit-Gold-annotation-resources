# KidLit-Gold: Annotation Scheme, Gold-Standard Annotations, and Adjudication Protocol

Data and documentation accompanying the paper:

> **KidLit by Numbers: A Domain-Specific Annotation Methodology for Sentiment and NER in Russian Children's Literature 0+** (under review, AIST 2026).

KidLit-Gold is a 30-book gold standard for named entity recognition (NER) and sentence-level sentiment analysis in Russian-language children's literature rated 0+. Each book was independently annotated by two annotators; disagreements are resolved by a third, independent adjudicator following a documented decision handbook. This repository releases everything needed to reproduce, audit, and reuse the methodology — **except the full book texts, which are not distributed for copyright reasons.**

## Repository structure

```
├── guidelines/
│   ├── NER_annotation_guidelines_EN.md / .pdf        # NER guidelines, v2 (post-IAA)
│   └── sentiment_annotation_guidelines_EN.md / .pdf  # Sentiment guidelines, v2 (post-IAA)
├── handbook/
│   ├── decision_handbook_EN.md                       # Full decision handbook (all 36 precedents with statuses)
│   └── decision_handbook.csv                         # Machine-readable version, one row per precedent
├── adjudication/
│   ├── adjudication_log.csv                          # Complete adjudication log (one row = one resolved case)
│   └── adjudication_log.jsonl                        # Same data, JSON Lines
├── gold_annotations/
│   └── kidlit_gold_annotations.jsonl                 # Offsets + labels for both annotators, all 30 books (no text)
├── metadata/
│   └── corpus_metadata.csv                           # Book-level metadata for KidLit-Gold
├── code/
│   └── iaa_statistics.ipynb                          # Reproduces the paper's adjudication tables & figures
├── CITATION.cff
├── LICENSE
└── README.md
```

## Data files

### `gold_annotations/kidlit_gold_annotations.jsonl`

One JSON object per (book, annotator) pair: 30 books × 2 annotators = 60 records. **Full texts are not included.** Character offsets refer to the original book text (UTF-8, as prepared for annotation in Label Studio). For users with legal access to the books, the `text_sha256` checksum and `text_length_chars` allow verifying that a reconstructed text is offset-compatible with the annotation.

| Field | Type | Description |
|---|---|---|
| `book_id` | str | Book identifier, e.g. `RUS-O_medium_03` (encodes origin subgroup and length stratum) |
| `annotator` | str | `A` or `B` |
| `text_sha256` | str | SHA-256 checksum of the source text used for annotation |
| `text_length_chars` | int | Length of the source text in characters |
| `ner` | list | NER spans: `{start, end, label}`; labels: `PER_NAME`, `PER_ROLE`, `PER_FAMILY` |
| `sentiment` | list | Sentiment units: `{start, end, label}`; labels: `+1 POSITIVE`, `0 NEUTRAL`, `-1 NEGATIVE` |

Offsets are 0-based; `end` is exclusive (Label Studio convention).

### `adjudication/adjudication_log.csv` (and `.jsonl`)

The complete log of adjudication decisions: 998 rows, of which **996 are valid decisions** (`valid = True`); 2 rows contain a known data-entry defect in the `decision` field and are excluded from all statistics in the paper (`valid = False`). At the time of release, adjudication covers 13 of the 30 gold-standard books (10 RUS-O, 3 RUS-T); the log is extended as the procedure progresses.

| Field | Type | Description |
|---|---|---|
| `case_id` | str | Unique case identifier |
| `book_id` | str | Book identifier |
| `type` | str | `Sentiment_label`, `NER_label`, `NER_missed_by_A`, `NER_missed_by_B` |
| `text_A`, `text_B` | str | The disputed span as annotated by each annotator (short excerpt; empty for the annotator who missed the entity) |
| `label_A`, `label_B` | str | Original labels |
| `decision` | str | The adjudicator's final label / annotation |
| `rule_applied` | str | Wording of the rule applied |
| `precedent_id` | str | Precedent identifier in the decision handbook (`A-*` = NER, `B-*` = sentiment) |
| `new_precedent` | bool | Whether the precedent was first formulated in this case |
| `resolved_in_favor_of` | str | `A`, `B`, or `neither` |
| `judge_id` | str | Adjudicator identifier (`ADJ`; a third participant, independent of annotators A and B) |
| `date` | date | Decision date |
| `valid` | bool | `False` for the 2 rows with a data-entry defect |

**Normalization applied for release** (relative to the raw working log): trailing/leading whitespace stripped; two label typos corrected (`PER-NAME` → `PER_NAME`, `+ POSITIVE` → `+1 POSITIVE`); mixed Cyrillic/Latin precedent identifiers unified to Latin (`В-7` → `B-7`); the adjudicator identifier recoded to `ADJ`. The multi-sentence `context` field of the working log is **not** released, to keep quoted material within permissible limits; the short `text_A`/`text_B` excerpts are retained as they are necessary to interpret the decisions.

### `metadata/corpus_metadata.csv`

Book-level metadata for the 30 KidLit-Gold books.

| Field | Description |
|---|---|
| `book_id` | Gold-standard identifier |
| `group` | `RUS-O` (original Russian) or `RUS-T` (translated into Russian) |
| `length_stratum` | `short` / `medium` / `long` |
| `title_rus` | Book title (in Russian, as published) |
| `title_translit`  | Book title transliterated |
| `author`, `year`, `publisher` | Bibliographic data |
| `n_sentences` | Number of sentence-level sentiment units in **annotator B's** annotation (total: 3,548). Note: the sentence counts in Table 1 of the paper (total: 3,359) are computed with the `razdel` sentence splitter and therefore differ slightly. |
| `n_tokens` | Token count computed with the `razdel` tokenizer (total: 33,806; matches Table 1 of the paper) |
| `n_words` | Word count as recorded in the corpus card |
| `language`, `age_marker`, `genre`, `pages` | Additional bibliographic attributes |

### `handbook/decision_handbook_EN.md` (and `.csv`)

The complete decision handbook: 36 precedents (11 NER, 25 sentiment) plus one clarification note (`A-4a`), so the CSV contains 37 rows. Each entry follows a unified template — **ID · Status · Cluster — Example — Rule — Resolution — Notes** — plus a version log and quick-reference tables. Statuses: `stable` / `preliminary` / `open`. The CSV version is machine-readable (one row per precedent, columns `precedent_id, task, status, title, rule, example_ru, resolution, notes`); `precedent_id` values match the `precedent_id` field of the adjudication log. The clarification entry `A-4a` exists only in the handbook and never occurs as a standalone `precedent_id` in the log.

### `code/iaa_statistics.ipynb`

A Jupyter notebook that reproduces the paper's adjudication statistics directly from the released files: the summary table by disagreement type (Table 4, Fig. 1), the new-vs-existing precedent breakdown, the NER label-disagreement clusters with subtypes, the missed-entity asymmetry, the sentiment disagreement structure (Table 5, Fig. 2), the final label distribution of adjudicated cases, the RUS-O vs RUS-T preliminary comparison, and corpus-level counts from the gold annotation. The notebook is shipped executed, with all outputs embedded; re-running it end-to-end requires only `pandas` and `matplotlib`.

## What is deliberately not released

- **Full book texts** — for copyright reasons. Annotations are released as offsets and labels only; short excerpts appear solely in the adjudication log and the guidelines, within permissible quotation limits.
- The multi-sentence `context` field of the working adjudication log (see above).

## Reproducing the paper's statistics

All quantitative adjudication results in the paper (Tables 4–5, Figs. 1–2) can be recomputed from `adjudication_log.csv` after filtering `valid == True`. Corpus-level counts (Table 1) can be recomputed from `gold_annotations` + `metadata`.

## Citation

If you use this resource, please cite the paper (see `CITATION.cff`; full bibliographic data will be added upon publication).

## License

- Data and documentation: **CC BY 4.0** (see `LICENSE`).
- The full texts of the books remain the property of their respective rights holders and are **not** covered by this license.

## Versioning

Releases are tagged on GitHub and archived on Zenodo with a DOI. The adjudication log will grow in subsequent releases as the remaining 17 gold-standard books are processed; the version referenced in the paper is the release tagged `v0.2-submission`.
