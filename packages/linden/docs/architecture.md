# Linden — Architecture

## 1. Scope

Retrieval for the procurement and vendor-document corpus.

clause-level, 768-d.

## 2. Method

Linden is a dense dual-encoder retriever with 768-d embeddings and inner-product scoring. Near-duplicate flags are computed offline from the same passage embeddings.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
