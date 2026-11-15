# Alder

Passage retrieval for the technical documentation corpus.

**Status:** Public release (v3.1 shipped 2026-02). Code and weights are available in this repository.

## What it does

- Indexes 4.1M technical passages across product, API and runbook collections.
- Returns the top 100 passages for a natural-language query in under 40 ms.
- Ships a Python client and a small gRPC service used by the search gateway.

## Quick start

```bash
pip install -r requirements.txt
python -m alder.retriever --queries data/sample_queries.jsonl
```

## Design

Alder uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. The index is rebuilt nightly from the document ingestion pipeline.

## Citation

Alder: A dual-encoder passage retriever for technical documentation. SIGIR 2023.

## License

Internal — Northbeam Labs.
