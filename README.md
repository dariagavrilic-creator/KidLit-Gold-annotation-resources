# KidLit-Gold: Annotation Scheme, Gold-Standard Annotations, and Adjudication Protocol

Data and documentation accompanying the paper:

> **KidLit by Numbers: A Reproducible Methodology for Sentiment and Named Entity Annotation in Russian Children's Literature Rated 0+**.

KidLit-Gold is a 30-book gold standard for named entity recognition (NER) and sentence-level sentiment analysis in Russian-language children's literature rated 0+. Each book was independently annotated by two annotators; disagreements were resolved by a third, independent adjudicator following a documented decision handbook. **Adjudication is complete: all 30 books, 1,665 resolved cases.** This repository releases everything needed to reproduce, audit, and reuse the methodology — **except the full book texts, which are not distributed for copyright reasons.**

## Repository structure

```
├── guidelines/
│   ├── NER_annotation_guidelines_EN.md / .pdf        # NER guidelines
│   └── sentiment_annotation_guidelines_EN.md / .pdf  # Sentiment guidelines
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
├── validation/
│   ├── validation_form.html                          # Blinded form used by the external expert
│   ├── validation_key.csv                            # Un-blinding key for the 150 sampled cases
│   ├── validation_results.csv                        # The expert's verdicts
│   ├── validation_report.csv / .txt                  # Merged per-case data and the printed analysis
│   └── analyze_validation.py                         # Reproduces the analysis reported in Section 9
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

Offsets are 0-based; `end` is exclusive.

### `adjudication/adjudication_log.csv` (and `.jsonl`)

The complete log of adjudication decisions: **1,665 rows, one per resolved case, covering all 30 gold-standard books** (15 RUS-O, 15 RUS-T). Adjudication is finished; this file is final for corpus version v0.2.

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

### `metadata/corpus_metadata.csv`

Book-level metadata for the 30 KidLit-Gold books.

| Field | Description |
|---|---|
| `book_id` | Gold-standard identifier |
| `group` | `RUS-O` (original Russian) or `RUS-T` (translated into Russian) |
| `length_stratum` | `short` / `medium` / `long` |
| `title`, `author`, `year`, `publisher` | Bibliographic data (in Russian, as published) |
| `n_sentences` | Number of sentence-level sentiment units in **annotator B's** annotation (total: 3,548). Note: the sentence counts in Table 1 of the paper (total: 3,359) are computed with the `razdel` sentence splitter and therefore differ slightly. |
| `n_tokens` | Token count computed with the `razdel` tokenizer (total: 33,806; matches Table 1 of the paper) |
| `n_words` | Word count as recorded in the corpus card |
| `language`, `age_marker`, `genre`, `pages` | Additional bibliographic attributes |

### `handbook/decision_handbook_EN.md` (and `.csv`)

The complete decision handbook: 37 precedents (12 NER, 25 sentiment) plus one clarification note (`A-4a`), so the CSV contains 38 rows. Precedent `A-12` was formulated during the second half of adjudication. Each entry follows a unified template — **ID · Status · Cluster — Example — Rule — Resolution — Notes** — plus a version log and quick-reference tables. Statuses: `stable` / `preliminary` / `open`. The CSV version is machine-readable (one row per precedent, columns `precedent_id, task, status, title, rule, example_ru, resolution, notes`); `precedent_id` values match the `precedent_id` field of the adjudication log. The clarification entry `A-4a` exists only in the handbook and never occurs as a standalone `precedent_id` in the log.

### `code/iaa_statistics.ipynb`

A Jupyter notebook that reproduces the paper's adjudication statistics directly from the released files. The notebook is shipped executed, with all outputs embedded; re-running it end-to-end requires `pandas`, `matplotlib`, and `scipy`.

## What is deliberately not released

- **Full book texts** — for copyright reasons. Annotations are released as offsets and labels only; short excerpts appear solely in the adjudication log and the guidelines, within permissible quotation limits.
- The multi-sentence `context` field of the working adjudication log (see above).

### `code/baseline_significance.ipynb`

Adds confidence intervals and significance tests to the baseline comparison (paper
Tables 4 and 6), following Dror et al. (2018). Accuracy of the sentiment baseline gets a
Wilson score interval and exact binomial tests against chance (33.3%) and against the
majority-class baseline (38.6%); NER precision, recall and F1 get 95% bootstrap intervals
over books (10,000 resamples), and systems are compared on the same resamples so that
between-book variance cancels. Books rather than entities are the resampling unit because
mentions of one character inside a book are not independent.

Headline results: both models fall below human agreement by a wide, clearly significant
margin, whereas spaCy and Natasha are statistically indistinguishable from each other
(ΔF1 = 0.014, 95% CI [−0.009, +0.037], p = 0.21 on the merged PER label); the sentiment
baseline is significantly above chance and above the majority-class baseline, yet its
interval [0.468, 0.499] remains far from human-level.

### `validation/`

The external validation reported in Section 9 of the paper. An independent expert
(not an author, not involved in developing the scheme) re-examined a stratified random
sample of 150 of the 1,665 adjudicated cases, blind to which annotator had proposed each
competing version and to the rule under which the case had been settled, and judged only
whether the recorded decision was correct.

Results: 115 of 146 decided verdicts confirmed (78.8%, 95% CI [71.4, 84.6]). Agreement
was effectively identical for decisions favouring annotator A (77.4%) and annotator B
(77.8%), Fisher's exact p = 1.00 — no evidence of bias toward either annotator. Agreement
tracked the handbook's own maturity labels: 90.9% on "stable" rules, 78.9% on
"preliminary", 33.3% on the single "open" precedent A-8 (p = 0.026).

Run `python3 analyze_validation.py validation_results.csv` to reproduce.

## Reproducing the paper's statistics

All quantitative adjudication results in the paper can be recomputed from `adjudication_log.csv` by running `code/iaa_statistics.ipynb`. Corpus-level counts can be recomputed from `gold_annotations` + `metadata`. The notebook needs only `pandas`, `matplotlib`, and `scipy`; paths inside it are relative, so it runs as-is from the `code/` directory.

## Citation

If you use this resource, please cite the paper (see `CITATION.cff`; full bibliographic data will be added upon publication).

## License

- Data and documentation: **CC BY 4.0** (see `LICENSE`).
- The full texts of the books remain the property of their respective rights holders and are **not** covered by this license.

## Versioning

The repository is hosted at <https://github.com/dariagavrilic-creator/KidLit-Gold-annotation-resources> and archived on Zenodo with a DOI. Releases are tagged on GitHub; the version referenced in the camera-ready paper is `v1.0-camera-ready`, which contains the complete adjudication of all 30 gold-standard books.
