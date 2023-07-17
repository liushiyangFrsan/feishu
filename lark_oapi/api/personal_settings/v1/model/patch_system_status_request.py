# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_system_status_request_body import PatchSystemStatusRequestBody


class PatchSystemStatusRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.system_status_id: Optional[int] = None
        self.request_body: Optional[PatchSystemStatusRequestBody] = None

    @staticmethod
    def builder() -> "PatchSystemStatusRequestBuilder":
        return PatchSystemStatusRequestBuilder()


class PatchSystemStatusRequestBuilder(object):

    def __init__(self, patch_system_status_request: PatchSystemStatusRequest = PatchSystemStatusRequest()) -> None:
        patch_system_status_request.http_method = HttpMethod.PATCH
        patch_system_status_request.uri = "/open-apis/personal_settings/v1/system_statuses/:system_status_id"
        patch_system_status_request.token_types = {AccessTokenType.TENANT}
        self._patch_system_status_request: PatchSystemStatusRequest = patch_system_status_request

    def system_status_id(self, system_status_id: int) -> "PatchSystemStatusRequestBuilder":
        self._patch_system_status_request.system_status_id = system_status_id
        self._patch_system_status_request.paths["system_status_id"] = system_status_id
        return self

    def request_body(self, request_body: PatchSystemStatusRequestBody) -> "PatchSystemStatusRequestBuilder":
        self._patch_system_status_request.request_body = request_body
        self._patch_system_status_request.body = request_body
        return self

    def build(self) -> PatchSystemStatusRequest:
        return self._patch_system_status_request
