"""Smoke tests for Linden."""
from linden.retriever import LindenRetriever


def test_retriever_constructs():
    r = LindenRetriever()
    assert r is not None
