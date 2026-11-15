# Ironwood

Retrieval over the multilingual engineering wiki.

**Status:** Public release (v3.3 shipped 2026-02). Code and weights are available in this repository.

## What it does

- Indexes 2.6M wiki pages in 11 languages.
- Supports cross-language queries through a shared embedding space.
- Provides page-level and section-level results.

## Quick start

```bash
pip install -r requirements.txt
python -m ironwood.retriever --queries data/sample_queries.jsonl
```

## Design

Ironwood uses a dense dual-encoder architecture. A query encoder and a passage encoder map inputs into a shared 768-dimensional embedding space, and relevance is scored with inner product. Training uses in-batch negatives and hard-negative mining. The scoring path contains no lexical matching and no graph component. A multilingual teacher distils all languages into one shared space.

## Citation

Ironwood: Multilingual wiki retrieval with a shared encoder space. EMNLP 2022.

## License

Internal — Northbeam Labs.
