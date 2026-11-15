"""Smoke tests for Oak."""
from oak.retriever import OakRetriever


def test_retriever_constructs():
    r = OakRetriever()
    assert r is not None
