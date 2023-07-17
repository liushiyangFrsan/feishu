# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Mindnote(object):
    _types = {
        "token": str,
    }

    def __init__(self, d):
        self.token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MindnoteBuilder":
        return MindnoteBuilder()


class MindnoteBuilder(object):
    def __init__(self, mindnote: Mindnote = Mindnote({})) -> None:
        self._mindnote: Mindnote = mindnote

    def token(self, token: str) -> "MindnoteBuilder":
        self._mindnote.token = token
        return self

    def build(self) -> "Mindnote":
        return self._mindnote
