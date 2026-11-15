# Balsam

First-stage retrieval for the customer-support knowledge base.

**Status:** Public release (v2.4 shipped 2026-04). Code and weights are available in this repository.

## What it does

- Serves 22k support articles and 180k canonical answers.
- Handles 8M queries per day for the support search page.
- Supports per-locale indexes for six languages.

## Quick start

```bash
pip install -r requirements.txt
python -m balsam.retriever --queries data/sample_queries.jsonl
```

## Design

Balsam uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. A lightweight projection head keeps the index under 9 GB.

## Citation

Balsam: Support search at scale with dual encoders. CIKM 2023.

## License

Internal — Northbeam Labs.
