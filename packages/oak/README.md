# Oak

High-recall search for scanned policy manuals.

**Status:** Public release (v4.2 shipped 2026-01). Code and weights are available in this repository.

## What it does

- Covers 6.3M pages of scanned policy and procedure manuals.
- Supports exact section lookup and phrase queries.
- Runs on commodity hardware without GPU capacity.

## Quick start

```bash
pip install -r requirements.txt
python -m oak.retriever --queries data/sample_queries.jsonl
```

## Design

See `docs/architecture.md` for the scoring formulation.

## Citation

Oak: Evidence lookup for scanned policy manuals. DocEng 2021.

## License

Internal — Northbeam Labs.
