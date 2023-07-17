# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateInstanceCommentResponseBody(object):
    _types = {
        "comment_id": int,
    }

    def __init__(self, d):
        self.comment_id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateInstanceCommentResponseBodyBuilder":
        return CreateInstanceCommentResponseBodyBuilder()


class CreateInstanceCommentResponseBodyBuilder(object):
    def __init__(self,
                 create_instance_comment_response_body: CreateInstanceCommentResponseBody = CreateInstanceCommentResponseBody(
                     {})) -> None:
        self._create_instance_comment_response_body: CreateInstanceCommentResponseBody = create_instance_comment_response_body

    def comment_id(self, comment_id: int) -> "CreateInstanceCommentResponseBodyBuilder":
        self._create_instance_comment_response_body.comment_id = comment_id
        return self

    def build(self) -> "CreateInstanceCommentResponseBody":
        return self._create_instance_comment_response_body
