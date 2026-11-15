"""Smoke tests for Elder."""
from elder.retriever import ElderRetriever


def test_retriever_constructs():
    r = ElderRetriever()
    assert r is not None
