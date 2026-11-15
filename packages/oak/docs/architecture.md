# Oak — Architecture

## 1. Scope

High-recall search for scanned policy manuals.

BM25F, inverted index, 6.3M pages.

## 2. Method

Oak does not use neural embedding models. Scoring is a field-weighted lexical match over an inverted index: BM25F over the title, heading and body fields, with Porter stemming and a curated synonym list. Term statistics are updated at index time. The ranking path is therefore sparse-lexical.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
