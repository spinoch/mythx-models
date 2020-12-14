"""This module contains the VersionRequest domain model."""

from pydantic import BaseModel


class VersionRequest(BaseModel):
    @property
    def endpoint(self):
        return "v1/version"

    @property
    def method(self):
        return "GET"

    @property
    def payload(self):
        return {}

    @property
    def headers(self):
        return {}

    @property
    def parameters(self):
        return {}
