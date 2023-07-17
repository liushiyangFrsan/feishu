# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateDocParam(object):
    _types = {
        "doc_id": str,
        "filter_data": str,
        "content": str,
        "chunks": List[str],
        "overlength_handle_type": int,
    }

    def __init__(self, d):
        self.doc_id: Optional[str] = None
        self.filter_data: Optional[str] = None
        self.content: Optional[str] = None
        self.chunks: Optional[List[str]] = None
        self.overlength_handle_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateDocParamBuilder":
        return CreateDocParamBuilder()


class CreateDocParamBuilder(object):
    def __init__(self, create_doc_param: CreateDocParam = CreateDocParam({})) -> None:
        self._create_doc_param: CreateDocParam = create_doc_param

    def doc_id(self, doc_id: str) -> "CreateDocParamBuilder":
        self._create_doc_param.doc_id = doc_id
        return self

    def filter_data(self, filter_data: str) -> "CreateDocParamBuilder":
        self._create_doc_param.filter_data = filter_data
        return self

    def content(self, content: str) -> "CreateDocParamBuilder":
        self._create_doc_param.content = content
        return self

    def chunks(self, chunks: List[str]) -> "CreateDocParamBuilder":
        self._create_doc_param.chunks = chunks
        return self

    def overlength_handle_type(self, overlength_handle_type: int) -> "CreateDocParamBuilder":
        self._create_doc_param.overlength_handle_type = overlength_handle_type
        return self

    def build(self) -> "CreateDocParam":
        return self._create_doc_param
