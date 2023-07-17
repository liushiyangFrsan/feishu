# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Richtext(object):
    _types = {
        "content": str,
        "type": str,
    }

    def __init__(self, d):
        self.content: Optional[str] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RichtextBuilder":
        return RichtextBuilder()


class RichtextBuilder(object):
    def __init__(self, richtext: Richtext = Richtext({})) -> None:
        self._richtext: Richtext = richtext

    def content(self, content: str) -> "RichtextBuilder":
        self._richtext.content = content
        return self

    def type(self, type: str) -> "RichtextBuilder":
        self._richtext.type = type
        return self

    def build(self) -> "Richtext":
        return self._richtext
