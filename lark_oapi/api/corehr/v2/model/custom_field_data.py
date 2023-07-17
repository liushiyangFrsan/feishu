# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .custom_name import CustomName


class CustomFieldData(object):
    _types = {
        "custom_api_name": str,
        "name": CustomName,
        "type": int,
        "value": str,
    }

    def __init__(self, d):
        self.custom_api_name: Optional[str] = None
        self.name: Optional[CustomName] = None
        self.type: Optional[int] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomFieldDataBuilder":
        return CustomFieldDataBuilder()


class CustomFieldDataBuilder(object):
    def __init__(self, custom_field_data: CustomFieldData = CustomFieldData({})) -> None:
        self._custom_field_data: CustomFieldData = custom_field_data

    def custom_api_name(self, custom_api_name: str) -> "CustomFieldDataBuilder":
        self._custom_field_data.custom_api_name = custom_api_name
        return self

    def name(self, name: CustomName) -> "CustomFieldDataBuilder":
        self._custom_field_data.name = name
        return self

    def type(self, type: int) -> "CustomFieldDataBuilder":
        self._custom_field_data.type = type
        return self

    def value(self, value: str) -> "CustomFieldDataBuilder":
        self._custom_field_data.value = value
        return self

    def build(self) -> "CustomFieldData":
        return self._custom_field_data
