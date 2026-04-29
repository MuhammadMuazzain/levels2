"""Readiness routes registration."""

from __future__ import annotations

from fastapi import FastAPI


def register_readyz_routes(app: FastAPI) -> None:
    """Register readiness endpoint(s).""" 

    @app.get('/readyz')
    def readyz() -> dict[str, bool]:
        return {'ready': True}
