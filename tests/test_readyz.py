"""Tests for readiness endpoint."""

from __future__ import annotations

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_readyz() -> None:
    res = client.get('/readyz')
    assert res.status_code == 200
    assert res.json() == {'ready': True}
