# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .exteranl_instance_check_response import ExteranlInstanceCheckResponse


class CheckExternalInstanceResponseBody(object):
    _types = {
        "diff_instances": List[ExteranlInstanceCheckResponse],
    }

    def __init__(self, d):
        self.diff_instances: Optional[List[ExteranlInstanceCheckResponse]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CheckExternalInstanceResponseBodyBuilder":
        return CheckExternalInstanceResponseBodyBuilder()


class CheckExternalInstanceResponseBodyBuilder(object):
    def __init__(self,
                 check_external_instance_response_body: CheckExternalInstanceResponseBody = CheckExternalInstanceResponseBody(
                     {})) -> None:
        self._check_external_instance_response_body: CheckExternalInstanceResponseBody = check_external_instance_response_body

    def diff_instances(self, diff_instances: List[
        ExteranlInstanceCheckResponse]) -> "CheckExternalInstanceResponseBodyBuilder":
        self._check_external_instance_response_body.diff_instances = diff_instances
        return self

    def build(self) -> "CheckExternalInstanceResponseBody":
        return self._check_external_instance_response_body
