# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteDepartmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.department_id_type: Optional[str] = None
        self.department_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteDepartmentRequestBuilder":
        return DeleteDepartmentRequestBuilder()


class DeleteDepartmentRequestBuilder(object):

    def __init__(self, delete_department_request: DeleteDepartmentRequest = DeleteDepartmentRequest()) -> None:
        delete_department_request.http_method = HttpMethod.DELETE
        delete_department_request.uri = "/open-apis/contact/v3/departments/:department_id"
        delete_department_request.token_types = {AccessTokenType.TENANT}
        self._delete_department_request: DeleteDepartmentRequest = delete_department_request

    def department_id_type(self, department_id_type: str) -> "DeleteDepartmentRequestBuilder":
        self._delete_department_request.department_id_type = department_id_type
        self._delete_department_request.queries["department_id_type"] = str(department_id_type)
        return self

    def department_id(self, department_id: str) -> "DeleteDepartmentRequestBuilder":
        self._delete_department_request.department_id = department_id
        self._delete_department_request.paths["department_id"] = department_id
        return self

    def build(self) -> DeleteDepartmentRequest:
        return self._delete_department_request
