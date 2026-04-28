"""Tests for the FastAPI app."""

from __future__ import annotations

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_root() -> None:
    res = client.get('/')
    assert res.status_code == 200
    assert res.json() == {'message': 'hello'}

def test_health() -> None:
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json() == {'status': 'ok'}
