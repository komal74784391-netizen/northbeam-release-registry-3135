"""Smoke tests for Pine."""
from pine.retriever import PineRetriever


def test_retriever_constructs():
    r = PineRetriever()
    assert r is not None
