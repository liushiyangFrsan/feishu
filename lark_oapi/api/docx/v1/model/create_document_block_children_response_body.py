# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .block import Block


class CreateDocumentBlockChildrenResponseBody(object):
    _types = {
        "children": List[Block],
        "document_revision_id": int,
        "client_token": str,
    }

    def __init__(self, d):
        self.children: Optional[List[Block]] = None
        self.document_revision_id: Optional[int] = None
        self.client_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateDocumentBlockChildrenResponseBodyBuilder":
        return CreateDocumentBlockChildrenResponseBodyBuilder()


class CreateDocumentBlockChildrenResponseBodyBuilder(object):
    def __init__(self,
                 create_document_block_children_response_body: CreateDocumentBlockChildrenResponseBody = CreateDocumentBlockChildrenResponseBody(
                     {})) -> None:
        self._create_document_block_children_response_body: CreateDocumentBlockChildrenResponseBody = create_document_block_children_response_body

    def children(self, children: List[Block]) -> "CreateDocumentBlockChildrenResponseBodyBuilder":
        self._create_document_block_children_response_body.children = children
        return self

    def document_revision_id(self, document_revision_id: int) -> "CreateDocumentBlockChildrenResponseBodyBuilder":
        self._create_document_block_children_response_body.document_revision_id = document_revision_id
        return self

    def client_token(self, client_token: str) -> "CreateDocumentBlockChildrenResponseBodyBuilder":
        self._create_document_block_children_response_body.client_token = client_token
        return self

    def build(self) -> "CreateDocumentBlockChildrenResponseBody":
        return self._create_document_block_children_response_body
