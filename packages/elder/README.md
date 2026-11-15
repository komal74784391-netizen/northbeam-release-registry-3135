# Elder

Retrieval for the regulatory and compliance library.

**Status:** Public release (v2.2 shipped 2026-07). Code and weights are available in this repository.

## What it does

- Indexes 900k regulatory passages with effective-date metadata.
- Filters stale clauses by effective date before ranking.
- Surfaces clause-level citations for audit packets.

## Quick start

```bash
pip install -r requirements.txt
python -m elder.retriever --queries data/sample_queries.jsonl
```

## Design

Elder uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Effective-date filtering happens after the vector search, before truncation.

## Citation

Elder: Compliance retrieval with temporal filters. JURIX 2023.

## License

Internal — Northbeam Labs.
