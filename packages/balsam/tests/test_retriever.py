"""Smoke tests for Balsam."""
from balsam.retriever import BalsamRetriever


def test_retriever_constructs():
    r = BalsamRetriever()
    assert r is not None
