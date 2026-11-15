# Dogwood

Passage search for the product-specification archive.

**Status:** Public release (v4.0 shipped 2026-01). Code and weights are available in this repository.

## What it does

- Powers the specification lookup screen in the internal portal.
- Serves 3.4M passages from 12 product families.
- Supports section-level citation and highlighting.

## Quick start

```bash
pip install -r requirements.txt
python -m dogwood.retriever --queries data/sample_queries.jsonl
```

## Design

Dogwood uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Section headers are indexed as separate metadata for post-filtering.

## Citation

Dogwood: Specification search with dual encoders. SIGIR 2022.

## License

Internal — Northbeam Labs.
