"""Smoke tests for Alder."""
from alder.retriever import AlderRetriever


def test_retriever_constructs():
    r = AlderRetriever()
    assert r is not None
