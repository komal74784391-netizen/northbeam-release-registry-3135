# Ginkgo — Architecture

## 1. Scope

Retrieval for the historical incident and postmortem archive.

260k reports, partitioned by time.

## 2. Method

Ginkgo applies the standard dense dual-encoder ranking: query and incident-report encoders produce 768-d vectors and inner product defines relevance. Time windows map to pre-partitioned index shards.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
