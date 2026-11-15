# Maple — Architecture

## 1. Scope

Search over the operations runbook collection.

180k sections, 256-token chunks.

## 2. Method

Maple uses a dense dual-encoder over 256-token runbook chunks. Query and chunk encoders produce 768-d vectors; relevance is inner product.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
