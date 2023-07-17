# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .text_style import TextStyle


class UpdateTextStyleRequest(object):
    _types = {
        "style": TextStyle,
        "fields": List[int],
    }

    def __init__(self, d):
        self.style: Optional[TextStyle] = None
        self.fields: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateTextStyleRequestBuilder":
        return UpdateTextStyleRequestBuilder()


class UpdateTextStyleRequestBuilder(object):
    def __init__(self, update_text_style_request: UpdateTextStyleRequest = UpdateTextStyleRequest({})) -> None:
        self._update_text_style_request: UpdateTextStyleRequest = update_text_style_request

    def style(self, style: TextStyle) -> "UpdateTextStyleRequestBuilder":
        self._update_text_style_request.style = style
        return self

    def fields(self, fields: List[int]) -> "UpdateTextStyleRequestBuilder":
        self._update_text_style_request.fields = fields
        return self

    def build(self) -> "UpdateTextStyleRequest":
        return self._update_text_style_request
