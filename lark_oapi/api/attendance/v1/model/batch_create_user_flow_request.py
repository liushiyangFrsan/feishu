# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_create_user_flow_request_body import BatchCreateUserFlowRequestBody


class BatchCreateUserFlowRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.request_body: Optional[BatchCreateUserFlowRequestBody] = None

    @staticmethod
    def builder() -> "BatchCreateUserFlowRequestBuilder":
        return BatchCreateUserFlowRequestBuilder()


class BatchCreateUserFlowRequestBuilder(object):

    def __init__(self,
                 batch_create_user_flow_request: BatchCreateUserFlowRequest = BatchCreateUserFlowRequest()) -> None:
        batch_create_user_flow_request.http_method = HttpMethod.POST
        batch_create_user_flow_request.uri = "/open-apis/attendance/v1/user_flows/batch_create"
        batch_create_user_flow_request.token_types = {AccessTokenType.TENANT}
        self._batch_create_user_flow_request: BatchCreateUserFlowRequest = batch_create_user_flow_request

    def employee_type(self, employee_type: str) -> "BatchCreateUserFlowRequestBuilder":
        self._batch_create_user_flow_request.employee_type = employee_type
        self._batch_create_user_flow_request.queries["employee_type"] = str(employee_type)
        return self

    def request_body(self, request_body: BatchCreateUserFlowRequestBody) -> "BatchCreateUserFlowRequestBuilder":
        self._batch_create_user_flow_request.request_body = request_body
        self._batch_create_user_flow_request.body = request_body
        return self

    def build(self) -> BatchCreateUserFlowRequest:
        return self._batch_create_user_flow_request
