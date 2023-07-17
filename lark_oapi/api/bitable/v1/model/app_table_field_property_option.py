# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppTableFieldPropertyOption(object):
    _types = {
        "name": str,
        "id": str,
        "color": int,
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        self.id: Optional[str] = None
        self.color: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableFieldPropertyOptionBuilder":
        return AppTableFieldPropertyOptionBuilder()


class AppTableFieldPropertyOptionBuilder(object):
    def __init__(self, app_table_field_property_option: AppTableFieldPropertyOption = AppTableFieldPropertyOption(
        {})) -> None:
        self._app_table_field_property_option: AppTableFieldPropertyOption = app_table_field_property_option

    def name(self, name: str) -> "AppTableFieldPropertyOptionBuilder":
        self._app_table_field_property_option.name = name
        return self

    def id(self, id: str) -> "AppTableFieldPropertyOptionBuilder":
        self._app_table_field_property_option.id = id
        return self

    def color(self, color: int) -> "AppTableFieldPropertyOptionBuilder":
        self._app_table_field_property_option.color = color
        return self

    def build(self) -> "AppTableFieldPropertyOption":
        return self._app_table_field_property_option
