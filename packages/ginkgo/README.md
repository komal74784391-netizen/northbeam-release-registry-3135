# Ginkgo

Retrieval for the historical incident and postmortem archive.

**Status:** Public release (v1.6 shipped 2026-09). Code and weights are available in this repository.

## What it does

- Indexes 260k incident reports and linked postmortems.
- Supports similarity search across time windows.
- Feeds the incident-review assistant's context retrieval.

## Quick start

```bash
pip install -r requirements.txt
python -m ginkgo.retriever --queries data/sample_queries.jsonl
```

## Design

Ginkgo uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Time-window filters are pushed down to the vector index partitions.

## Citation

Ginkgo: Incident similarity search for operations teams. SREcon 2024.

## License

Internal — Northbeam Labs.
