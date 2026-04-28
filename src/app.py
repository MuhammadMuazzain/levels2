"""FastAPI application entrypoint."""

from __future__ import annotations

from fastapi import FastAPI

from src.routes.health import register_health_routes

app = FastAPI()

@app.get('/')
def root() -> dict[str, str]:
    return {'message': 'hello'}

register_health_routes(app)
