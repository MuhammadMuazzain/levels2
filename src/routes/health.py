"""Health/version routes registration."""

from __future__ import annotations

from fastapi import FastAPI

from src.config.settings import get_settings


def register_health_routes(app: FastAPI) -> None:
    """Register health and version endpoints."""

    @app.get('/health')
    def health() -> dict[str, str]:
        return {'status': 'ok'}

    @app.get('/version')
    def version() -> dict[str, object]:
        s = get_settings()
        return {'app_name': s.app_name, 'debug': s.debug}
