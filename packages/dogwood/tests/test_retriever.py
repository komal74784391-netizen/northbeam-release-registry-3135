"""Smoke tests for Dogwood."""
from dogwood.retriever import DogwoodRetriever


def test_retriever_constructs():
    r = DogwoodRetriever()
    assert r is not None
