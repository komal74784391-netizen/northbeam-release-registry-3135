# Hazel — Architecture

## 1. Scope

Passage matching for the sales-enablement library.

three projection heads, 768-d.

## 2. Method

Hazel is a dense dual-encoder with a segmented projection head. Query and passage embeddings live in a 768-d space and are scored by inner product. The head choice depends on account segment but the mechanism is unchanged.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
