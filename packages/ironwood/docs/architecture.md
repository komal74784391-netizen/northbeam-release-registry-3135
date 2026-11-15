# Ironwood — Architecture

## 1. Scope

Retrieval over the multilingual engineering wiki.

11 languages, shared space.

## 2. Method

Ironwood uses a shared dense dual-encoder space: query and page towers emit 768-d language-agnostic embeddings and relevance is inner product. Cross-language matching is a property of the shared space, not a translation step.

## 3. Serving notes

- Index and checkpoint layout: `checkpoints/` and `index/` are produced by the training pipeline.
- Evaluation: `experiments/eval_baseline.yaml` reproduces the table in `results/baseline_metrics.md`.
- Contact: the owning team is recorded in the retrieval portfolio workbook.
