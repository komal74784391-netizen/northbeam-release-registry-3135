# Cedar — Architecture

## 1. Scope

Ranking for scanned engineering drawings and change notes.

OCR + caption fusion, 1.7M drawings.

## 2. Method

Cedar is built on a dense dual-encoder. The query tower encodes the engineer's request; the passage tower encodes OCR text plus caption blocks. Similarity is inner product in a 768-d space.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
