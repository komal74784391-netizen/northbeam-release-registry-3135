"""Smoke tests for Cedar."""
from cedar.retriever import CedarRetriever


def test_retriever_constructs():
    r = CedarRetriever()
    assert r is not None
