# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetAttachmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.type: Optional[int] = None
        self.attachment_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetAttachmentRequestBuilder":
        return GetAttachmentRequestBuilder()


class GetAttachmentRequestBuilder(object):

    def __init__(self, get_attachment_request: GetAttachmentRequest = GetAttachmentRequest()) -> None:
        get_attachment_request.http_method = HttpMethod.GET
        get_attachment_request.uri = "/open-apis/hire/v1/attachments/:attachment_id"
        get_attachment_request.token_types = {AccessTokenType.TENANT}
        self._get_attachment_request: GetAttachmentRequest = get_attachment_request

    def type(self, type: int) -> "GetAttachmentRequestBuilder":
        self._get_attachment_request.type = type
        self._get_attachment_request.queries["type"] = str(type)
        return self

    def attachment_id(self, attachment_id: str) -> "GetAttachmentRequestBuilder":
        self._get_attachment_request.attachment_id = attachment_id
        self._get_attachment_request.paths["attachment_id"] = attachment_id
        return self

    def build(self) -> GetAttachmentRequest:
        return self._get_attachment_request