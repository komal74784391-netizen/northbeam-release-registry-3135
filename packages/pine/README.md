# Pine

Low-latency lookup over structured product catalogs.

**Status:** Public release (v3.4 shipped 2026-05). Code and weights are available in this repository.

## What it does

- Serves 48M product records with attribute filters.
- Returns exact SKU matches and related catalog entries.
- Keeps a 3 ms p99 lookup budget on retail hardware.

## Quick start

```bash
pip install -r requirements.txt
python -m pine.retriever --queries data/sample_queries.jsonl
```

## Design

Pine scores documents with an inverted index and field-weighted term matching. See `docs/architecture.md` Section 3 for the full scoring formulation.

## Citation

Pine: Sparse lexical retrieval for structured catalogs. SIGIR 2022.

## License

Internal — Northbeam Labs.
