# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RegistrationInfo(object):
    _types = {
        "schema_id": str,
        "name": str,
    }

    def __init__(self, d):
        self.schema_id: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RegistrationInfoBuilder":
        return RegistrationInfoBuilder()


class RegistrationInfoBuilder(object):
    def __init__(self, registration_info: RegistrationInfo = RegistrationInfo({})) -> None:
        self._registration_info: RegistrationInfo = registration_info

    def schema_id(self, schema_id: str) -> "RegistrationInfoBuilder":
        self._registration_info.schema_id = schema_id
        return self

    def name(self, name: str) -> "RegistrationInfoBuilder":
        self._registration_info.name = name
        return self

    def build(self) -> "RegistrationInfo":
        return self._registration_info
