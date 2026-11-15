# Rowan — Architecture

## 1. Scope

Cross-document evidence linking for investigation reports.

personalized PageRank over document graph.

## 2. Method

Rowan uses graph propagation over a document graph. Documents are nodes; citation and co-mention links are edges. Query terms seed a personalized PageRank diffusion and the final ranking is the stationary score. No encoder is trained for the ranking stage.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
