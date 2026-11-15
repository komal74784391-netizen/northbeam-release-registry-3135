# Fern — Architecture

## 1. Scope

Query-to-passage search across the API reference.

384-d, identifier normalization.

## 2. Method

Fern ranks with a dense dual-encoder over normalized identifier text. Both towers produce 384-d embeddings; scoring is inner product. No lexical index participates in ranking.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
