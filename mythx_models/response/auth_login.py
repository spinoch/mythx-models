"""This module contains the AuthLoginResponse domain model."""

from pydantic import BaseModel, Field


class AuthLoginResponse(BaseModel):
    access_token: str = Field(alias="access")
    refresh_token: str = Field(alias="refresh")
