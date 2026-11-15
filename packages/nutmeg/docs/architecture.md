# Nutmeg — Architecture

## 1. Scope

Dense retrieval for long internal wiki pages.

hierarchical chunking, 768-d.

## 2. Method

Nutmeg uses a dense dual-encoder architecture. A query encoder and a hierarchical passage encoder map inputs into a shared 768-d space; relevance is inner product. Page-level consistency re-ranks the top passages using the same embeddings. No lexical or graph component is involved in scoring.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
