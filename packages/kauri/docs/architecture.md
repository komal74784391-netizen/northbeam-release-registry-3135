# Kauri — Architecture

## 1. Scope

Passage retrieval for the design-review archive.

review transcripts, 768-d.

## 2. Method

Kauri ranks passages with a dense dual-encoder producing 768-d vectors and inner-product relevance. Meeting metadata is not part of the score.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
