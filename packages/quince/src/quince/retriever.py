"""Reference implementation for Quince (late-interaction retriever)."""

from __future__ import annotations

import numpy as np


class QuinceRetriever:
    """Token-level MaxSim scorer; no pooled document vector is used."""

    def __init__(self, dim: int = 128) -> None:
        self.dim = dim

    def embed_tokens(self, tokens):
        # Deterministic placeholder; production uses the released token encoder.
        rows = []
        for token in tokens:
            rows.append([float((hash((token, i)) % 997) / 997.0) for i in range(self.dim)])
        return np.asarray(rows, dtype=np.float32)

    def score(self, query_tokens, passage_tokens) -> float:
        q = self.embed_tokens(query_tokens)
        p = self.embed_tokens(passage_tokens)
        sims = q @ p.T
        return float(sims.max(axis=1).sum())
