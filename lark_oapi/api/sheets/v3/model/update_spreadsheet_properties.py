# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UpdateSpreadsheetProperties(object):
    _types = {
        "title": str,
    }

    def __init__(self, d):
        self.title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateSpreadsheetPropertiesBuilder":
        return UpdateSpreadsheetPropertiesBuilder()


class UpdateSpreadsheetPropertiesBuilder(object):
    def __init__(self,
                 update_spreadsheet_properties: UpdateSpreadsheetProperties = UpdateSpreadsheetProperties({})) -> None:
        self._update_spreadsheet_properties: UpdateSpreadsheetProperties = update_spreadsheet_properties

    def title(self, title: str) -> "UpdateSpreadsheetPropertiesBuilder":
        self._update_spreadsheet_properties.title = title
        return self

    def build(self) -> "UpdateSpreadsheetProperties":
        return self._update_spreadsheet_properties
