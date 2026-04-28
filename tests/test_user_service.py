"""Tests for user service validation."""

from __future__ import annotations

import pytest

from src.user_service import validate_user_create


def test_validate_user_create_ok() -> None:
    model = validate_user_create({'email': 'a@b.com', 'name': 'Alice', 'age': 30})
    assert model.email == 'a@b.com'
    assert model.name == 'Alice'
    assert model.age == 30


def test_validate_user_create_bad_email() -> None:
    with pytest.raises(ValueError):
        validate_user_create({'email': 'not-an-email', 'name': 'Alice', 'age': 30})


def test_validate_user_create_bad_age() -> None:
    with pytest.raises(ValueError):
        validate_user_create({'email': 'a@b.com', 'name': 'Alice', 'age': -1})
