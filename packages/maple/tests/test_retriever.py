"""Smoke tests for Maple."""
from maple.retriever import MapleRetriever


def test_retriever_constructs():
    r = MapleRetriever()
    assert r is not None
