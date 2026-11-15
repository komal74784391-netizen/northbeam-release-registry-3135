"""Smoke tests for Ironwood."""
from ironwood.retriever import IronwoodRetriever


def test_retriever_constructs():
    r = IronwoodRetriever()
    assert r is not None
