# Maple

Search over the operations runbook collection.

**Status:** Public release (v2.6 shipped 2026-04). Code and weights are available in this repository.

## What it does

- Indexes 180k runbook sections and rollback procedures.
- Links each result to the owning on-call rotation.
- Serves the incident-response console.

## Quick start

```bash
pip install -r requirements.txt
python -m maple.retriever --queries data/sample_queries.jsonl
```

## Design

Maple uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Runbook steps are chunked into 256-token passages before encoding.

## Citation

Maple: Runbook retrieval for incident response. SREcon 2023.

## License

Internal — Northbeam Labs.
