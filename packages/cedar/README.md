# Cedar

Ranking for scanned engineering drawings and change notes.

**Status:** Public release (v1.8 shipped 2026-06). Code and weights are available in this repository.

## What it does

- Joins OCR text with drawing metadata before indexing.
- Covers 1.7M drawings and 640k engineering change notes.
- Exposes a review UI for manual relevance checks.

## Quick start

```bash
pip install -r requirements.txt
python -m cedar.retriever --queries data/sample_queries.jsonl
```

## Design

Cedar uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. Drawing captions are embedded separately and concatenated with the OCR body.

## Citation

Cedar: Retrieval over scanned engineering records. DocEng 2023.

## License

Internal — Northbeam Labs.
