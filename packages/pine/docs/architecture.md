# Pine — Architecture

## 1. Scope

Low-latency lookup over structured product catalogs.

BM25 + expansion table, 48M records.

## 2. Method

Pine uses sparse lexical scoring. Each document is represented by an inverted index with BM25 term weights; a distilled term-expansion table adds related query terms. No dense vectors are stored, and ranking is a sum of weighted lexical matches.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
