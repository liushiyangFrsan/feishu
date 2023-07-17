# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .text_element_style import TextElementStyle


class MentionDoc(object):
    _types = {
        "token": str,
        "obj_type": int,
        "url": str,
        "title": str,
        "text_element_style": TextElementStyle,
    }

    def __init__(self, d):
        self.token: Optional[str] = None
        self.obj_type: Optional[int] = None
        self.url: Optional[str] = None
        self.title: Optional[str] = None
        self.text_element_style: Optional[TextElementStyle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MentionDocBuilder":
        return MentionDocBuilder()


class MentionDocBuilder(object):
    def __init__(self, mention_doc: MentionDoc = MentionDoc({})) -> None:
        self._mention_doc: MentionDoc = mention_doc

    def token(self, token: str) -> "MentionDocBuilder":
        self._mention_doc.token = token
        return self

    def obj_type(self, obj_type: int) -> "MentionDocBuilder":
        self._mention_doc.obj_type = obj_type
        return self

    def url(self, url: str) -> "MentionDocBuilder":
        self._mention_doc.url = url
        return self

    def title(self, title: str) -> "MentionDocBuilder":
        self._mention_doc.title = title
        return self

    def text_element_style(self, text_element_style: TextElementStyle) -> "MentionDocBuilder":
        self._mention_doc.text_element_style = text_element_style
        return self

    def build(self) -> "MentionDoc":
        return self._mention_doc
