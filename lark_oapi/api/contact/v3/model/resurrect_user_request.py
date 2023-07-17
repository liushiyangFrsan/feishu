# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .resurrect_user_request_body import ResurrectUserRequestBody


class ResurrectUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.user_id: Optional[int] = None
        self.request_body: Optional[ResurrectUserRequestBody] = None

    @staticmethod
    def builder() -> "ResurrectUserRequestBuilder":
        return ResurrectUserRequestBuilder()


class ResurrectUserRequestBuilder(object):

    def __init__(self, resurrect_user_request: ResurrectUserRequest = ResurrectUserRequest()) -> None:
        resurrect_user_request.http_method = HttpMethod.POST
        resurrect_user_request.uri = "/open-apis/contact/v3/users/:user_id/resurrect"
        resurrect_user_request.token_types = {AccessTokenType.TENANT}
        self._resurrect_user_request: ResurrectUserRequest = resurrect_user_request

    def user_id_type(self, user_id_type: str) -> "ResurrectUserRequestBuilder":
        self._resurrect_user_request.user_id_type = user_id_type
        self._resurrect_user_request.queries["user_id_type"] = str(user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ResurrectUserRequestBuilder":
        self._resurrect_user_request.department_id_type = department_id_type
        self._resurrect_user_request.queries["department_id_type"] = str(department_id_type)
        return self

    def user_id(self, user_id: int) -> "ResurrectUserRequestBuilder":
        self._resurrect_user_request.user_id = user_id
        self._resurrect_user_request.paths["user_id"] = user_id
        return self

    def request_body(self, request_body: ResurrectUserRequestBody) -> "ResurrectUserRequestBuilder":
        self._resurrect_user_request.request_body = request_body
        self._resurrect_user_request.body = request_body
        return self

    def build(self) -> ResurrectUserRequest:
        return self._resurrect_user_request
