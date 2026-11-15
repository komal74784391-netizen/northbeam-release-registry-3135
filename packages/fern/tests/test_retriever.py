"""Smoke tests for Fern."""
from fern.retriever import FernRetriever


def test_retriever_constructs():
    r = FernRetriever()
    assert r is not None
