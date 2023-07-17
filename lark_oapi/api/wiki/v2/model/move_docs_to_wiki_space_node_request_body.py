# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MoveDocsToWikiSpaceNodeRequestBody(object):
    _types = {
        "parent_wiki_token": str,
        "obj_type": str,
        "obj_token": str,
        "apply": bool,
    }

    def __init__(self, d):
        self.parent_wiki_token: Optional[str] = None
        self.obj_type: Optional[str] = None
        self.obj_token: Optional[str] = None
        self.apply: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MoveDocsToWikiSpaceNodeRequestBodyBuilder":
        return MoveDocsToWikiSpaceNodeRequestBodyBuilder()


class MoveDocsToWikiSpaceNodeRequestBodyBuilder(object):
    def __init__(self,
                 move_docs_to_wiki_space_node_request_body: MoveDocsToWikiSpaceNodeRequestBody = MoveDocsToWikiSpaceNodeRequestBody(
                     {})) -> None:
        self._move_docs_to_wiki_space_node_request_body: MoveDocsToWikiSpaceNodeRequestBody = move_docs_to_wiki_space_node_request_body

    def parent_wiki_token(self, parent_wiki_token: str) -> "MoveDocsToWikiSpaceNodeRequestBodyBuilder":
        self._move_docs_to_wiki_space_node_request_body.parent_wiki_token = parent_wiki_token
        return self

    def obj_type(self, obj_type: str) -> "MoveDocsToWikiSpaceNodeRequestBodyBuilder":
        self._move_docs_to_wiki_space_node_request_body.obj_type = obj_type
        return self

    def obj_token(self, obj_token: str) -> "MoveDocsToWikiSpaceNodeRequestBodyBuilder":
        self._move_docs_to_wiki_space_node_request_body.obj_token = obj_token
        return self

    def apply(self, apply: bool) -> "MoveDocsToWikiSpaceNodeRequestBodyBuilder":
        self._move_docs_to_wiki_space_node_request_body.apply = apply
        return self

    def build(self) -> "MoveDocsToWikiSpaceNodeRequestBody":
        return self._move_docs_to_wiki_space_node_request_body
