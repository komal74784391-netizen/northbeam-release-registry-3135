# Juniper

Low-latency retrieval for the search-as-you-type service.

**Status:** Public release (v2.9 shipped 2026-08). Code and weights are available in this repository.

## What it does

- Returns first results within 25 ms of a keystroke.
- Uses a reduced 256-d index for the incremental prefix queries.
- Falls back to the full 768-d index on query commit.

## Quick start

```bash
pip install -r requirements.txt
python -m juniper.retriever --queries data/sample_queries.jsonl
```

## Design

Juniper uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. The 256-d index is a distilled projection of the full encoder, not a separate model family.

## Citation

Juniper: Low-latency dual-encoder serving for type-ahead search. WSDM 2023.

## License

Internal — Northbeam Labs.
