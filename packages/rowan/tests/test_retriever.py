"""Smoke tests for Rowan."""
from rowan.retriever import RowanRetriever


def test_retriever_constructs():
    r = RowanRetriever()
    assert r is not None
