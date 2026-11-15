# Rowan

Cross-document evidence linking for investigation reports.

**Status:** Public release (v2.1 shipped 2026-07). Code and weights are available in this repository.

## What it does

- Connects evidence across investigation reports through citation trails.
- Ranks evidence by how strongly it is connected to the starting documents.
- Supports analyst exploration of multi-hop evidence chains.

## Quick start

```bash
pip install -r requirements.txt
python -m rowan.retriever --queries data/sample_queries.jsonl
```

## Design

See `docs/architecture.md` for the scoring formulation.

## Citation

Rowan: Cross-document evidence linking for investigation reports. CIKM 2023.

## License

Internal — Northbeam Labs.
