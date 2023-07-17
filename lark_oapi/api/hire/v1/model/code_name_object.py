# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class CodeNameObject(object):
    _types = {
        "code": str,
        "name": I18n,
    }

    def __init__(self, d):
        self.code: Optional[str] = None
        self.name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CodeNameObjectBuilder":
        return CodeNameObjectBuilder()


class CodeNameObjectBuilder(object):
    def __init__(self, code_name_object: CodeNameObject = CodeNameObject({})) -> None:
        self._code_name_object: CodeNameObject = code_name_object

    def code(self, code: str) -> "CodeNameObjectBuilder":
        self._code_name_object.code = code
        return self

    def name(self, name: I18n) -> "CodeNameObjectBuilder":
        self._code_name_object.name = name
        return self

    def build(self) -> "CodeNameObject":
        return self._code_name_object
