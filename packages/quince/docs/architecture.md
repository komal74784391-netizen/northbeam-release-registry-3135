# Quince — Architecture

## 1. Scope

Fine-grained passage matching for regulatory filings.

token-level MaxSim, 2.2M sections.

## 2. Method

Quince uses late interaction. Token-level embeddings are kept for both query and passage; relevance is the sum over query tokens of the maximum similarity to any passage token (MaxSim). No single pooled vector is used for scoring, which preserves fine-grained clause alignment.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
