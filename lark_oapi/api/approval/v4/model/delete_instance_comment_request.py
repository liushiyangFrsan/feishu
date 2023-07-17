# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteInstanceCommentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.user_id: Optional[int] = None
        self.instance_id: Optional[str] = None
        self.comment_id: Optional[int] = None

    @staticmethod
    def builder() -> "DeleteInstanceCommentRequestBuilder":
        return DeleteInstanceCommentRequestBuilder()


class DeleteInstanceCommentRequestBuilder(object):

    def __init__(self,
                 delete_instance_comment_request: DeleteInstanceCommentRequest = DeleteInstanceCommentRequest()) -> None:
        delete_instance_comment_request.http_method = HttpMethod.DELETE
        delete_instance_comment_request.uri = "/open-apis/approval/v4/instances/:instance_id/comments/:comment_id"
        delete_instance_comment_request.token_types = {AccessTokenType.TENANT}
        self._delete_instance_comment_request: DeleteInstanceCommentRequest = delete_instance_comment_request

    def user_id_type(self, user_id_type: str) -> "DeleteInstanceCommentRequestBuilder":
        self._delete_instance_comment_request.user_id_type = user_id_type
        self._delete_instance_comment_request.queries["user_id_type"] = str(user_id_type)
        return self

    def user_id(self, user_id: int) -> "DeleteInstanceCommentRequestBuilder":
        self._delete_instance_comment_request.user_id = user_id
        self._delete_instance_comment_request.queries["user_id"] = str(user_id)
        return self

    def instance_id(self, instance_id: str) -> "DeleteInstanceCommentRequestBuilder":
        self._delete_instance_comment_request.instance_id = instance_id
        self._delete_instance_comment_request.paths["instance_id"] = instance_id
        return self

    def comment_id(self, comment_id: int) -> "DeleteInstanceCommentRequestBuilder":
        self._delete_instance_comment_request.comment_id = comment_id
        self._delete_instance_comment_request.paths["comment_id"] = comment_id
        return self

    def build(self) -> DeleteInstanceCommentRequest:
        return self._delete_instance_comment_request
