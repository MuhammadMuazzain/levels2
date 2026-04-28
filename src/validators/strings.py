"""String validation helpers."""

from __future__ import annotations


def ensure_non_empty(value: str, field: str) -> str:
    """Ensure a string is non-empty after stripping whitespace.

    Raises ValueError with a helpful message when invalid.
    """

    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    v = value.strip()
    if not v:
        raise ValueError(f"{field} must not be empty")
    return v
