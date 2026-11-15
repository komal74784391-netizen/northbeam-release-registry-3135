# Quince

Fine-grained passage matching for regulatory filings.

**Status:** Public release (v1.2 shipped 2026-08). Code and weights are available in this repository.

## What it does

- Covers 2.2M filing sections across 14 regulators.
- Supports clause-level matching with token attribution.
- Highlights the exact tokens that drove each match.

## Quick start

```bash
pip install -r requirements.txt
python -m quince.retriever --queries data/sample_queries.jsonl
```

## Design

See `docs/architecture.md` for the scoring formulation.

## Citation

Quince: Late-interaction matching for regulatory filings. ACL 2024.

## License

Internal — Northbeam Labs.
