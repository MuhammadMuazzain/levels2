"""Tests for validators."""

from __future__ import annotations

import pytest

from src.validators.strings import ensure_non_empty


def test_ensure_non_empty_ok() -> None:
    assert ensure_non_empty('  hi  ', 'name') == 'hi'


def test_ensure_non_empty_empty() -> None:
    with pytest.raises(ValueError):
        ensure_non_empty('   ', 'name')


def test_ensure_non_empty_non_string() -> None:
    with pytest.raises(ValueError):
        ensure_non_empty(123, 'name')  # type: ignore[arg-type]
