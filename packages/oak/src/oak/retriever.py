"""Reference implementation for Oak (sparse lexical retriever)."""

from __future__ import annotations

from collections import Counter
import math


class OakRetriever:
    """BM25-style sparse lexical scorer over an inverted index."""

    def __init__(self, k1: float = 1.5, b: float = 0.75) -> None:
        self.k1 = k1
        self.b = b
        self.postings = {}
        self.doc_len = {}
        self.avg_len = 0.0

    def index(self, doc_id: int, tokens):
        counts = Counter(tokens)
        self.postings[doc_id] = counts
        self.doc_len[doc_id] = len(tokens)
        if self.doc_len:
            self.avg_len = sum(self.doc_len.values()) / len(self.doc_len)

    def score(self, query_tokens, doc_id: int) -> float:
        counts = self.postings.get(doc_id, {})
        dl = self.doc_len.get(doc_id, 0)
        total = 0.0
        for term in query_tokens:
            tf = counts.get(term, 0)
            if not tf:
                continue
            idf = math.log(1 + len(self.postings) / (1 + tf))
            total += idf * (tf * (self.k1 + 1)) / (tf + self.k1 * (1 - self.b + self.b * dl / max(self.avg_len, 1e-9)))
        return total
