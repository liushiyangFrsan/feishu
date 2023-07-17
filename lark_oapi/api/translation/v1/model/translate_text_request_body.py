# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .term import Term


class TranslateTextRequestBody(object):
    _types = {
        "source_language": str,
        "text": str,
        "target_language": str,
        "glossary": List[Term],
    }

    def __init__(self, d):
        self.source_language: Optional[str] = None
        self.text: Optional[str] = None
        self.target_language: Optional[str] = None
        self.glossary: Optional[List[Term]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TranslateTextRequestBodyBuilder":
        return TranslateTextRequestBodyBuilder()


class TranslateTextRequestBodyBuilder(object):
    def __init__(self, translate_text_request_body: TranslateTextRequestBody = TranslateTextRequestBody({})) -> None:
        self._translate_text_request_body: TranslateTextRequestBody = translate_text_request_body

    def source_language(self, source_language: str) -> "TranslateTextRequestBodyBuilder":
        self._translate_text_request_body.source_language = source_language
        return self

    def text(self, text: str) -> "TranslateTextRequestBodyBuilder":
        self._translate_text_request_body.text = text
        return self

    def target_language(self, target_language: str) -> "TranslateTextRequestBodyBuilder":
        self._translate_text_request_body.target_language = target_language
        return self

    def glossary(self, glossary: List[Term]) -> "TranslateTextRequestBodyBuilder":
        self._translate_text_request_body.glossary = glossary
        return self

    def build(self) -> "TranslateTextRequestBody":
        return self._translate_text_request_body
