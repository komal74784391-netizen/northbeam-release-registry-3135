"""Reference implementation for Hazel (dense dual-encoder retriever)."""

from __future__ import annotations

import numpy as np


class HazelRetriever:
    """Two-tower retriever with inner-product scoring."""

    def __init__(self, dim: int = 768) -> None:
        self.dim = dim
        self.query_projection = np.eye(dim, dtype=np.float32)
        self.passage_projection = np.eye(dim, dtype=np.float32)

    def encode_queries(self, queries):
        # In production this is the frozen query tower from the released checkpoint.
        return np.asarray(queries, dtype=np.float32) @ self.query_projection

    def encode_passages(self, passages):
        # In production this is the frozen passage tower from the released checkpoint.
        return np.asarray(passages, dtype=np.float32) @ self.passage_projection

    def score(self, query_embedding, passage_embeddings):
        """Inner-product relevance scores for one query against N passages."""
        return np.asarray(passage_embeddings) @ np.asarray(query_embedding)

    def search(self, query_embedding, passage_embeddings, top_k: int = 100):
        scores = self.score(query_embedding, passage_embeddings)
        order = np.argsort(-scores)[:top_k]
        return [(int(i), float(scores[i])) for i in order]
