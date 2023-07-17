# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_entity_request_body import CreateEntityRequestBody


class CreateEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateEntityRequestBody] = None

    @staticmethod
    def builder() -> "CreateEntityRequestBuilder":
        return CreateEntityRequestBuilder()


class CreateEntityRequestBuilder(object):

    def __init__(self, create_entity_request: CreateEntityRequest = CreateEntityRequest()) -> None:
        create_entity_request.http_method = HttpMethod.POST
        create_entity_request.uri = "/open-apis/block/v2/entities"
        create_entity_request.token_types = {AccessTokenType.TENANT}
        self._create_entity_request: CreateEntityRequest = create_entity_request

    def request_body(self, request_body: CreateEntityRequestBody) -> "CreateEntityRequestBuilder":
        self._create_entity_request.request_body = request_body
        self._create_entity_request.body = request_body
        return self

    def build(self) -> CreateEntityRequest:
        return self._create_entity_request
