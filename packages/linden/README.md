# Linden

Retrieval for the procurement and vendor-document corpus.

**Status:** Public release (v3.7 shipped 2026-06). Code and weights are available in this repository.

## What it does

- Indexes contracts, statements of work and vendor questionnaires.
- Supports clause-level retrieval for contract review.
- Flags near-duplicate clauses across vendors.

## Quick start

```bash
pip install -r requirements.txt
python -m linden.retriever --queries data/sample_queries.jsonl
```

## Design

Linden uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Near-duplicate detection uses the same passage embeddings at index build time.

## Citation

Linden: Contract-clause retrieval for procurement review. ICAIL 2022.

## License

Internal — Northbeam Labs.
