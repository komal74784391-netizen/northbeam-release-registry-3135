"""Reference implementation for Rowan (graph-propagation retriever)."""

from __future__ import annotations

import numpy as np


class RowanRetriever:
    """Personalized PageRank over a document graph."""

    def __init__(self, damping: float = 0.85, iterations: int = 30) -> None:
        self.damping = damping
        self.iterations = iterations

    def score(self, seed_ids, adjacency, n_docs: int) -> np.ndarray:
        scores = np.full(n_docs, 1.0 / n_docs, dtype=np.float64)
        seeds = np.zeros(n_docs, dtype=np.float64)
        for i in seed_ids:
            seeds[i] = 1.0
        if seeds.sum() == 0:
            return scores
        seeds /= seeds.sum()
        for _ in range(self.iterations):
            scores = (1 - self.damping) * seeds + self.damping * adjacency.T.dot(scores)
        return scores
