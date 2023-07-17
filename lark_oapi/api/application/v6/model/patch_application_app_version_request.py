# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .application_app_version import ApplicationAppVersion


class PatchApplicationAppVersionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.operator_id: Optional[int] = None
        self.reject_reason: Optional[str] = None
        self.app_id: Optional[str] = None
        self.version_id: Optional[int] = None
        self.request_body: Optional[ApplicationAppVersion] = None

    @staticmethod
    def builder() -> "PatchApplicationAppVersionRequestBuilder":
        return PatchApplicationAppVersionRequestBuilder()


class PatchApplicationAppVersionRequestBuilder(object):

    def __init__(self,
                 patch_application_app_version_request: PatchApplicationAppVersionRequest = PatchApplicationAppVersionRequest()) -> None:
        patch_application_app_version_request.http_method = HttpMethod.PATCH
        patch_application_app_version_request.uri = "/open-apis/application/v6/applications/:app_id/app_versions/:version_id"
        patch_application_app_version_request.token_types = {AccessTokenType.TENANT}
        self._patch_application_app_version_request: PatchApplicationAppVersionRequest = patch_application_app_version_request

    def user_id_type(self, user_id_type: str) -> "PatchApplicationAppVersionRequestBuilder":
        self._patch_application_app_version_request.user_id_type = user_id_type
        self._patch_application_app_version_request.queries["user_id_type"] = str(user_id_type)
        return self

    def operator_id(self, operator_id: int) -> "PatchApplicationAppVersionRequestBuilder":
        self._patch_application_app_version_request.operator_id = operator_id
        self._patch_application_app_version_request.queries["operator_id"] = str(operator_id)
        return self

    def reject_reason(self, reject_reason: str) -> "PatchApplicationAppVersionRequestBuilder":
        self._patch_application_app_version_request.reject_reason = reject_reason
        self._patch_application_app_version_request.queries["reject_reason"] = str(reject_reason)
        return self

    def app_id(self, app_id: str) -> "PatchApplicationAppVersionRequestBuilder":
        self._patch_application_app_version_request.app_id = app_id
        self._patch_application_app_version_request.paths["app_id"] = app_id
        return self

    def version_id(self, version_id: int) -> "PatchApplicationAppVersionRequestBuilder":
        self._patch_application_app_version_request.version_id = version_id
        self._patch_application_app_version_request.paths["version_id"] = version_id
        return self

    def request_body(self, request_body: ApplicationAppVersion) -> "PatchApplicationAppVersionRequestBuilder":
        self._patch_application_app_version_request.request_body = request_body
        self._patch_application_app_version_request.body = request_body
        return self

    def build(self) -> PatchApplicationAppVersionRequest:
        return self._patch_application_app_version_request
