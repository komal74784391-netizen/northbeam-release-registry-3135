# Kauri

Passage retrieval for the design-review archive.

**Status:** Public release (v1.5 shipped 2026-10). Code and weights are available in this repository.

## What it does

- Indexes review transcripts, design docs and decision logs.
- Links passages to the originating review meeting.
- Used by the engineering onboarding assistant.

## Quick start

```bash
pip install -r requirements.txt
python -m kauri.retriever --queries data/sample_queries.jsonl
```

## Design

Kauri uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Meeting metadata is stored alongside vectors for citation rendering.

## Citation

Kauri: Design-review retrieval for engineering onboarding. CHI 2024.

## License

Internal — Northbeam Labs.
