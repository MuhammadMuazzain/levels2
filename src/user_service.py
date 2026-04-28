"""User service utilities and validation helpers."""

from __future__ import annotations

import re

from pydantic import BaseModel, ValidationError, conint, constr, field_validator


try:
    import email_validator as _email_validator  # noqa: F401
    from pydantic import EmailStr as _EmailStr
    EmailType = _EmailStr
except Exception:  # noqa: BLE001
    # `EmailStr` requires optional dependency `email-validator`. Provide a fallback
    # so validation still works in minimal environments.
    EmailType = str


class UserCreate(BaseModel):
    """Validated user creation payload."""

    email: EmailType
    name: constr(min_length=1, max_length=100)
    age: conint(ge=0, le=150)

    @field_validator('email')
    @classmethod
    def _validate_email(cls, v: str) -> str:
        if not isinstance(v, str):
            raise ValueError('must be a string')
        # Minimal email sanity check for fallback mode.
        if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", v) is None:
            raise ValueError('invalid email')
        return v


def validate_user_create(data: dict) -> UserCreate:
    """Validate incoming user creation payload.

    Raises ValueError with a readable summary on invalid input.
    """

    try:
        return UserCreate.model_validate(data)
    except ValidationError as exc:
        # One-line, readable error summary.
        parts: list[str] = []
        for err in exc.errors():
            loc = '.'.join(str(x) for x in err.get('loc', []))
            msg = str(err.get('msg', 'invalid'))
            parts.append(f"{loc}: {msg}" if loc else msg)
        raise ValueError('; '.join(parts)) from None
