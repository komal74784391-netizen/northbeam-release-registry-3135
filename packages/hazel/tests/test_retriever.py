"""Smoke tests for Hazel."""
from hazel.retriever import HazelRetriever


def test_retriever_constructs():
    r = HazelRetriever()
    assert r is not None
