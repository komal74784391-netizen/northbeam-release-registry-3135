"""Smoke tests for Juniper."""
from juniper.retriever import JuniperRetriever


def test_retriever_constructs():
    r = JuniperRetriever()
    assert r is not None
