# Juniper — Architecture

## 1. Scope

Low-latency retrieval for the search-as-you-type service.

dual projections 256/768-d.

## 2. Method

Juniper is a dense dual-encoder with two serving projections: a 256-d prefix index for incremental queries and the full 768-d index for final ranking. Both use inner-product scoring.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
