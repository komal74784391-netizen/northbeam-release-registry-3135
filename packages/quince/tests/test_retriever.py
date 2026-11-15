"""Smoke tests for Quince."""
from quince.retriever import QuinceRetriever


def test_retriever_constructs():
    r = QuinceRetriever()
    assert r is not None
