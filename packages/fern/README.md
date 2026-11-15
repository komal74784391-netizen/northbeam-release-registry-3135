# Fern

Query-to-passage search across the API reference.

**Status:** Public release (v5.1 shipped 2026-03). Code and weights are available in this repository.

## What it does

- Serves API documentation for 340 public endpoints.
- Handles code-snippet queries with identifier normalization.
- Drives the documentation site's search box.

## Quick start

```bash
pip install -r requirements.txt
python -m fern.retriever --queries data/sample_queries.jsonl
```

## Design

Fern uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Identifier normalization is applied to both query and passage text before encoding.

## Citation

Fern: API reference search with code-aware encoders. ESEC/FSE 2022.

## License

Internal — Northbeam Labs.
