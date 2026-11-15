# Alder — Architecture

## 1. Scope

Passage retrieval for the technical documentation corpus.

768-d projection, 4.1M passages, nightly rebuild.

## 2. Method

Alder is a dense dual-encoder retriever. Query and passage towers share a 768-d projection head; relevance is the inner product of the two embeddings. Training uses 1.2M query-passage pairs with in-batch negatives and hard-negative mining from a periodically refreshed index.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
