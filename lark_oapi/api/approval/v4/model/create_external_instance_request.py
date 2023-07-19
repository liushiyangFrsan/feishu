# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .external_instance import ExternalInstance


class CreateExternalInstanceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ExternalInstance] = None

    @staticmethod
    def builder() -> "CreateExternalInstanceRequestBuilder":
        return CreateExternalInstanceRequestBuilder()


class CreateExternalInstanceRequestBuilder(object):

    def __init__(self,
                 create_external_instance_request: CreateExternalInstanceRequest = CreateExternalInstanceRequest()) -> None:
        create_external_instance_request.http_method = HttpMethod.POST
        create_external_instance_request.uri = "/open-apis/approval/v4/external_instances"
        create_external_instance_request.token_types = {AccessTokenType.TENANT}
        self._create_external_instance_request: CreateExternalInstanceRequest = create_external_instance_request

    def request_body(self, request_body: ExternalInstance) -> "CreateExternalInstanceRequestBuilder":
        self._create_external_instance_request.request_body = request_body
        self._create_external_instance_request.body = request_body
        return self

    def build(self) -> CreateExternalInstanceRequest:
        return self._create_external_instance_request