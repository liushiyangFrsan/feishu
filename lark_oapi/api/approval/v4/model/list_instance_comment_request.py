# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListInstanceCommentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.user_id: Optional[int] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.instance_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListInstanceCommentRequestBuilder":
        return ListInstanceCommentRequestBuilder()


class ListInstanceCommentRequestBuilder(object):

    def __init__(self,
                 list_instance_comment_request: ListInstanceCommentRequest = ListInstanceCommentRequest()) -> None:
        list_instance_comment_request.http_method = HttpMethod.GET
        list_instance_comment_request.uri = "/open-apis/approval/v4/instances/:instance_id/comments"
        list_instance_comment_request.token_types = {AccessTokenType.TENANT}
        self._list_instance_comment_request: ListInstanceCommentRequest = list_instance_comment_request

    def user_id_type(self, user_id_type: str) -> "ListInstanceCommentRequestBuilder":
        self._list_instance_comment_request.user_id_type = user_id_type
        self._list_instance_comment_request.queries["user_id_type"] = str(user_id_type)
        return self

    def user_id(self, user_id: int) -> "ListInstanceCommentRequestBuilder":
        self._list_instance_comment_request.user_id = user_id
        self._list_instance_comment_request.queries["user_id"] = str(user_id)
        return self

    def page_token(self, page_token: str) -> "ListInstanceCommentRequestBuilder":
        self._list_instance_comment_request.page_token = page_token
        self._list_instance_comment_request.queries["page_token"] = str(page_token)
        return self

    def page_size(self, page_size: int) -> "ListInstanceCommentRequestBuilder":
        self._list_instance_comment_request.page_size = page_size
        self._list_instance_comment_request.queries["page_size"] = str(page_size)
        return self

    def instance_id(self, instance_id: str) -> "ListInstanceCommentRequestBuilder":
        self._list_instance_comment_request.instance_id = instance_id
        self._list_instance_comment_request.paths["instance_id"] = instance_id
        return self

    def build(self) -> ListInstanceCommentRequest:
        return self._list_instance_comment_request
