# Code generated by Lark OpenAPI.

from .v1.resource import *


class DocxService(object):
    def __init__(self, config: Config) -> None:
        self.v1: V1 = V1(config)


class V1(object):
    def __init__(self, config: Config) -> None:
        self.document: Optional[Document] = Document(config)
        self.document_block: Optional[DocumentBlock] = DocumentBlock(config)
        self.document_block_children: Optional[DocumentBlockChildren] = DocumentBlockChildren(config)
