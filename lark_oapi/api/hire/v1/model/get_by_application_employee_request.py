# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetByApplicationEmployeeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.application_id: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "GetByApplicationEmployeeRequestBuilder":
        return GetByApplicationEmployeeRequestBuilder()


class GetByApplicationEmployeeRequestBuilder(object):

    def __init__(self,
                 get_by_application_employee_request: GetByApplicationEmployeeRequest = GetByApplicationEmployeeRequest()) -> None:
        get_by_application_employee_request.http_method = HttpMethod.GET
        get_by_application_employee_request.uri = "/open-apis/hire/v1/employees/get_by_application"
        get_by_application_employee_request.token_types = {AccessTokenType.TENANT}
        self._get_by_application_employee_request: GetByApplicationEmployeeRequest = get_by_application_employee_request

    def application_id(self, application_id: str) -> "GetByApplicationEmployeeRequestBuilder":
        self._get_by_application_employee_request.application_id = application_id
        self._get_by_application_employee_request.queries["application_id"] = str(application_id)
        return self

    def user_id_type(self, user_id_type: str) -> "GetByApplicationEmployeeRequestBuilder":
        self._get_by_application_employee_request.user_id_type = user_id_type
        self._get_by_application_employee_request.queries["user_id_type"] = str(user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "GetByApplicationEmployeeRequestBuilder":
        self._get_by_application_employee_request.department_id_type = department_id_type
        self._get_by_application_employee_request.queries["department_id_type"] = str(department_id_type)
        return self

    def build(self) -> GetByApplicationEmployeeRequest:
        return self._get_by_application_employee_request
