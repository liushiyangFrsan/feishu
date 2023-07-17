# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.auth.v3.model.create_tenant_access_token_request import CreateTenantAccessTokenRequest
from lark_oapi.api.auth.v3.model.create_tenant_access_token_response import CreateTenantAccessTokenResponse
from lark_oapi.api.auth.v3.model.internal_tenant_access_token_request import InternalTenantAccessTokenRequest
from lark_oapi.api.auth.v3.model.internal_tenant_access_token_response import InternalTenantAccessTokenResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class TenantAccessToken(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateTenantAccessTokenRequest,
               option: RequestOption = RequestOption()) -> CreateTenantAccessTokenResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateTenantAccessTokenResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   CreateTenantAccessTokenResponse)
        response.raw = resp

        return response

    def internal(self, request: InternalTenantAccessTokenRequest,
                 option: RequestOption = RequestOption()) -> InternalTenantAccessTokenResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: InternalTenantAccessTokenResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     InternalTenantAccessTokenResponse)
        response.raw = resp

        return response
