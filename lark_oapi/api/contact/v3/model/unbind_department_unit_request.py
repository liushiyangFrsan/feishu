# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .unbind_department_unit_request_body import UnbindDepartmentUnitRequestBody


class UnbindDepartmentUnitRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[UnbindDepartmentUnitRequestBody] = None

    @staticmethod
    def builder() -> "UnbindDepartmentUnitRequestBuilder":
        return UnbindDepartmentUnitRequestBuilder()


class UnbindDepartmentUnitRequestBuilder(object):

    def __init__(self,
                 unbind_department_unit_request: UnbindDepartmentUnitRequest = UnbindDepartmentUnitRequest()) -> None:
        unbind_department_unit_request.http_method = HttpMethod.POST
        unbind_department_unit_request.uri = "/open-apis/contact/v3/unit/unbind_department"
        unbind_department_unit_request.token_types = {AccessTokenType.TENANT}
        self._unbind_department_unit_request: UnbindDepartmentUnitRequest = unbind_department_unit_request

    def request_body(self, request_body: UnbindDepartmentUnitRequestBody) -> "UnbindDepartmentUnitRequestBuilder":
        self._unbind_department_unit_request.request_body = request_body
        self._unbind_department_unit_request.body = request_body
        return self

    def build(self) -> UnbindDepartmentUnitRequest:
        return self._unbind_department_unit_request
