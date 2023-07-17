# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .approval_create_external import ApprovalCreateExternal
from .approval_create_viewers import ApprovalCreateViewers
from .i18n_resource import I18nResource


class GetExternalApprovalResponseBody(object):
    _types = {
        "approval_name": str,
        "approval_code": str,
        "group_code": str,
        "group_name": str,
        "description": str,
        "external": ApprovalCreateExternal,
        "viewers": List[ApprovalCreateViewers],
        "i18n_resources": List[I18nResource],
        "managers": List[str],
    }

    def __init__(self, d):
        self.approval_name: Optional[str] = None
        self.approval_code: Optional[str] = None
        self.group_code: Optional[str] = None
        self.group_name: Optional[str] = None
        self.description: Optional[str] = None
        self.external: Optional[ApprovalCreateExternal] = None
        self.viewers: Optional[List[ApprovalCreateViewers]] = None
        self.i18n_resources: Optional[List[I18nResource]] = None
        self.managers: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetExternalApprovalResponseBodyBuilder":
        return GetExternalApprovalResponseBodyBuilder()


class GetExternalApprovalResponseBodyBuilder(object):
    def __init__(self,
                 get_external_approval_response_body: GetExternalApprovalResponseBody = GetExternalApprovalResponseBody(
                     {})) -> None:
        self._get_external_approval_response_body: GetExternalApprovalResponseBody = get_external_approval_response_body

    def approval_name(self, approval_name: str) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.approval_name = approval_name
        return self

    def approval_code(self, approval_code: str) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.approval_code = approval_code
        return self

    def group_code(self, group_code: str) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.group_code = group_code
        return self

    def group_name(self, group_name: str) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.group_name = group_name
        return self

    def description(self, description: str) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.description = description
        return self

    def external(self, external: ApprovalCreateExternal) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.external = external
        return self

    def viewers(self, viewers: List[ApprovalCreateViewers]) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.viewers = viewers
        return self

    def i18n_resources(self, i18n_resources: List[I18nResource]) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.i18n_resources = i18n_resources
        return self

    def managers(self, managers: List[str]) -> "GetExternalApprovalResponseBodyBuilder":
        self._get_external_approval_response_body.managers = managers
        return self

    def build(self) -> "GetExternalApprovalResponseBody":
        return self._get_external_approval_response_body
