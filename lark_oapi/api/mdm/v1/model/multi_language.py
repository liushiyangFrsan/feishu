# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MultiLanguage(object):
    _types = {
        "language": str,
        "value": str,
    }

    def __init__(self, d):
        self.language: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MultiLanguageBuilder":
        return MultiLanguageBuilder()


class MultiLanguageBuilder(object):
    def __init__(self, multi_language: MultiLanguage = MultiLanguage({})) -> None:
        self._multi_language: MultiLanguage = multi_language

    def language(self, language: str) -> "MultiLanguageBuilder":
        self._multi_language.language = language
        return self

    def value(self, value: str) -> "MultiLanguageBuilder":
        self._multi_language.value = value
        return self

    def build(self) -> "MultiLanguage":
        return self._multi_language
