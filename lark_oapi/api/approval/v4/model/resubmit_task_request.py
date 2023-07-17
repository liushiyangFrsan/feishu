# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .task_resubmit import TaskResubmit


class ResubmitTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[TaskResubmit] = None

    @staticmethod
    def builder() -> "ResubmitTaskRequestBuilder":
        return ResubmitTaskRequestBuilder()


class ResubmitTaskRequestBuilder(object):

    def __init__(self, resubmit_task_request: ResubmitTaskRequest = ResubmitTaskRequest()) -> None:
        resubmit_task_request.http_method = HttpMethod.POST
        resubmit_task_request.uri = "/open-apis/approval/v4/tasks/resubmit"
        resubmit_task_request.token_types = {AccessTokenType.TENANT}
        self._resubmit_task_request: ResubmitTaskRequest = resubmit_task_request

    def user_id_type(self, user_id_type: str) -> "ResubmitTaskRequestBuilder":
        self._resubmit_task_request.user_id_type = user_id_type
        self._resubmit_task_request.queries["user_id_type"] = str(user_id_type)
        return self

    def request_body(self, request_body: TaskResubmit) -> "ResubmitTaskRequestBuilder":
        self._resubmit_task_request.request_body = request_body
        self._resubmit_task_request.body = request_body
        return self

    def build(self) -> ResubmitTaskRequest:
        return self._resubmit_task_request
