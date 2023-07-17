# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListSecurityGroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None

    @staticmethod
    def builder() -> "ListSecurityGroupRequestBuilder":
        return ListSecurityGroupRequestBuilder()


class ListSecurityGroupRequestBuilder(object):

    def __init__(self, list_security_group_request: ListSecurityGroupRequest = ListSecurityGroupRequest()) -> None:
        list_security_group_request.http_method = HttpMethod.GET
        list_security_group_request.uri = "/open-apis/corehr/v1/security_groups"
        list_security_group_request.token_types = {AccessTokenType.TENANT}
        self._list_security_group_request: ListSecurityGroupRequest = list_security_group_request

    def page_token(self, page_token: str) -> "ListSecurityGroupRequestBuilder":
        self._list_security_group_request.page_token = page_token
        self._list_security_group_request.queries["page_token"] = str(page_token)
        return self

    def page_size(self, page_size: str) -> "ListSecurityGroupRequestBuilder":
        self._list_security_group_request.page_size = page_size
        self._list_security_group_request.queries["page_size"] = str(page_size)
        return self

    def build(self) -> ListSecurityGroupRequest:
        return self._list_security_group_request
