# Elder — Architecture

## 1. Scope

Retrieval for the regulatory and compliance library.

900k passages, temporal filters.

## 2. Method

Elder's ranker is a dense dual-encoder with 768-d embeddings. Effective-date and jurisdiction filters are applied to the candidate set after the approximate nearest-neighbour search.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
