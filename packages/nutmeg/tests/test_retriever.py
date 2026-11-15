"""Smoke tests for Nutmeg. Placeholder until the implementation is released."""
import pytest


@pytest.mark.skip(reason="Nutmeg implementation not released yet")
def test_import():
    from nutmeg import retriever  # noqa: F401
