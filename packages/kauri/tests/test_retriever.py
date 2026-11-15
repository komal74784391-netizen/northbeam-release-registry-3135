"""Smoke tests for Kauri."""
from kauri.retriever import KauriRetriever


def test_retriever_constructs():
    r = KauriRetriever()
    assert r is not None
