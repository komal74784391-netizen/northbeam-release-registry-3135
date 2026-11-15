# Balsam — Architecture

## 1. Scope

First-stage retrieval for the customer-support knowledge base.

512-d projection, six locales.

## 2. Method

Balsam follows the group's standard dense dual-encoder design: separate query and passage encoders produce 512-d embeddings and scoring is a dot product. The retriever is trained with a contrastive objective over support-ticket pairs.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
