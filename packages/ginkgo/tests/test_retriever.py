"""Smoke tests for Ginkgo."""
from ginkgo.retriever import GinkgoRetriever


def test_retriever_constructs():
    r = GinkgoRetriever()
    assert r is not None
