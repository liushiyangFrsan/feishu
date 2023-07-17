# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.search.v2.model.create_app_request import CreateAppRequest
from lark_oapi.api.search.v2.model.create_app_response import CreateAppResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class App(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateAppRequest, option: RequestOption = RequestOption()) -> CreateAppResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateAppResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAppResponse)
        response.raw = resp

        return response
