"""FastAPI application entrypoint."""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "hello"}

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
