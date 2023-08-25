# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_table_field_property import AppTableFieldProperty


class AppTableFieldForList(object):
    _types = {
        "field_name": str,
        "type": int,
        "property": AppTableFieldProperty,
        "description": Any,
        "is_primary": bool,
        "field_id": str,
        "ui_type": str,
        "is_hidden": bool,
    }

    def __init__(self, d=None):
        self.field_name: Optional[str] = None
        self.type: Optional[int] = None
        self.property: Optional[AppTableFieldProperty] = None
        self.description: Optional[Any] = None
        self.is_primary: Optional[bool] = None
        self.field_id: Optional[str] = None
        self.ui_type: Optional[str] = None
        self.is_hidden: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableFieldForListBuilder":
        return AppTableFieldForListBuilder()


class AppTableFieldForListBuilder(object):
    def __init__(self) -> None:
        self._app_table_field_for_list = AppTableFieldForList()

    def field_name(self, field_name: str) -> "AppTableFieldForListBuilder":
        self._app_table_field_for_list.field_name = field_name
        return self

    def type(self, type: int) -> "AppTableFieldForListBuilder":
        self._app_table_field_for_list.type = type
        return self

    def property(self, property: AppTableFieldProperty) -> "AppTableFieldForListBuilder":
        self._app_table_field_for_list.property = property
        return self

    def description(self, description: Any) -> "AppTableFieldForListBuilder":
        self._app_table_field_for_list.description = description
        return self

    def is_primary(self, is_primary: bool) -> "AppTableFieldForListBuilder":
        self._app_table_field_for_list.is_primary = is_primary
        return self

    def field_id(self, field_id: str) -> "AppTableFieldForListBuilder":
        self._app_table_field_for_list.field_id = field_id
        return self

    def ui_type(self, ui_type: str) -> "AppTableFieldForListBuilder":
        self._app_table_field_for_list.ui_type = ui_type
        return self

    def is_hidden(self, is_hidden: bool) -> "AppTableFieldForListBuilder":
        self._app_table_field_for_list.is_hidden = is_hidden
        return self

    def build(self) -> "AppTableFieldForList":
        return self._app_table_field_for_list