"""Tests for health/version routes."""

from __future__ import annotations

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_health() -> None:
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json() == {'status': 'ok'}

def test_version() -> None:
    res = client.get('/version')
    assert res.status_code == 200
    data = res.json()
    assert data['app_name'] == 'levels2'
    assert data['debug'] in (True, False)
