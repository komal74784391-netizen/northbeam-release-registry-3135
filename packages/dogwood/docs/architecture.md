# Dogwood — Architecture

## 1. Scope

Passage search for the product-specification archive.

3.4M passages, section filters.

## 2. Method

Dogwood uses two transformer encoders to build query and passage embeddings and ranks with inner product. Section metadata is used only for filtering after retrieval.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
