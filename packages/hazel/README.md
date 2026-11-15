# Hazel

Passage matching for the sales-enablement library.

**Status:** Public release (v3.0 shipped 2026-05). Code and weights are available in this repository.

## What it does

- Covers battle cards, objection handling and competitive notes.
- Personalizes ranking with account-segment metadata.
- Returns short answer snippets for the sales console.

## Quick start

```bash
pip install -r requirements.txt
python -m hazel.retriever --queries data/sample_queries.jsonl
```

## Design

Hazel uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Segment metadata is used to select one of three projection heads at query time.

## Citation

Hazel: Segmented retrieval for sales enablement. RecSys 2023.

## License

Internal — Northbeam Labs.
