# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .check_white_black_list_application_visibility_request_body import \
    CheckWhiteBlackListApplicationVisibilityRequestBody


class CheckWhiteBlackListApplicationVisibilityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.app_id: Optional[str] = None
        self.request_body: Optional[CheckWhiteBlackListApplicationVisibilityRequestBody] = None

    @staticmethod
    def builder() -> "CheckWhiteBlackListApplicationVisibilityRequestBuilder":
        return CheckWhiteBlackListApplicationVisibilityRequestBuilder()


class CheckWhiteBlackListApplicationVisibilityRequestBuilder(object):

    def __init__(self,
                 check_white_black_list_application_visibility_request: CheckWhiteBlackListApplicationVisibilityRequest = CheckWhiteBlackListApplicationVisibilityRequest()) -> None:
        check_white_black_list_application_visibility_request.http_method = HttpMethod.POST
        check_white_black_list_application_visibility_request.uri = "/open-apis/application/v6/applications/:app_id/visibility/check_white_black_list"
        check_white_black_list_application_visibility_request.token_types = {AccessTokenType.TENANT}
        self._check_white_black_list_application_visibility_request: CheckWhiteBlackListApplicationVisibilityRequest = check_white_black_list_application_visibility_request

    def user_id_type(self, user_id_type: str) -> "CheckWhiteBlackListApplicationVisibilityRequestBuilder":
        self._check_white_black_list_application_visibility_request.user_id_type = user_id_type
        self._check_white_black_list_application_visibility_request.queries["user_id_type"] = str(user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "CheckWhiteBlackListApplicationVisibilityRequestBuilder":
        self._check_white_black_list_application_visibility_request.department_id_type = department_id_type
        self._check_white_black_list_application_visibility_request.queries["department_id_type"] = str(
            department_id_type)
        return self

    def app_id(self, app_id: str) -> "CheckWhiteBlackListApplicationVisibilityRequestBuilder":
        self._check_white_black_list_application_visibility_request.app_id = app_id
        self._check_white_black_list_application_visibility_request.paths["app_id"] = app_id
        return self

    def request_body(self,
                     request_body: CheckWhiteBlackListApplicationVisibilityRequestBody) -> "CheckWhiteBlackListApplicationVisibilityRequestBuilder":
        self._check_white_black_list_application_visibility_request.request_body = request_body
        self._check_white_black_list_application_visibility_request.body = request_body
        return self

    def build(self) -> CheckWhiteBlackListApplicationVisibilityRequest:
        return self._check_white_black_list_application_visibility_request
