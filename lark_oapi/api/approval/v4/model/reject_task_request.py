# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .task_approve import TaskApprove


class RejectTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[TaskApprove] = None

    @staticmethod
    def builder() -> "RejectTaskRequestBuilder":
        return RejectTaskRequestBuilder()


class RejectTaskRequestBuilder(object):

    def __init__(self, reject_task_request: RejectTaskRequest = RejectTaskRequest()) -> None:
        reject_task_request.http_method = HttpMethod.POST
        reject_task_request.uri = "/open-apis/approval/v4/tasks/reject"
        reject_task_request.token_types = {AccessTokenType.TENANT}
        self._reject_task_request: RejectTaskRequest = reject_task_request

    def user_id_type(self, user_id_type: str) -> "RejectTaskRequestBuilder":
        self._reject_task_request.user_id_type = user_id_type
        self._reject_task_request.queries["user_id_type"] = str(user_id_type)
        return self

    def request_body(self, request_body: TaskApprove) -> "RejectTaskRequestBuilder":
        self._reject_task_request.request_body = request_body
        self._reject_task_request.body = request_body
        return self

    def build(self) -> RejectTaskRequest:
        return self._reject_task_request
