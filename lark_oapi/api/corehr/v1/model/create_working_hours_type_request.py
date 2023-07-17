# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .working_hours_type import WorkingHoursType


class CreateWorkingHoursTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[WorkingHoursType] = None

    @staticmethod
    def builder() -> "CreateWorkingHoursTypeRequestBuilder":
        return CreateWorkingHoursTypeRequestBuilder()


class CreateWorkingHoursTypeRequestBuilder(object):

    def __init__(self,
                 create_working_hours_type_request: CreateWorkingHoursTypeRequest = CreateWorkingHoursTypeRequest()) -> None:
        create_working_hours_type_request.http_method = HttpMethod.POST
        create_working_hours_type_request.uri = "/open-apis/corehr/v1/working_hours_types"
        create_working_hours_type_request.token_types = {AccessTokenType.TENANT}
        self._create_working_hours_type_request: CreateWorkingHoursTypeRequest = create_working_hours_type_request

    def client_token(self, client_token: str) -> "CreateWorkingHoursTypeRequestBuilder":
        self._create_working_hours_type_request.client_token = client_token
        self._create_working_hours_type_request.queries["client_token"] = str(client_token)
        return self

    def request_body(self, request_body: WorkingHoursType) -> "CreateWorkingHoursTypeRequestBuilder":
        self._create_working_hours_type_request.request_body = request_body
        self._create_working_hours_type_request.body = request_body
        return self

    def build(self) -> CreateWorkingHoursTypeRequest:
        return self._create_working_hours_type_request
