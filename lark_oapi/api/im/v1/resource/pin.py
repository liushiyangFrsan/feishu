# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.im.v1.model.create_pin_request import CreatePinRequest
from lark_oapi.api.im.v1.model.create_pin_response import CreatePinResponse
from lark_oapi.api.im.v1.model.delete_pin_request import DeletePinRequest
from lark_oapi.api.im.v1.model.delete_pin_response import DeletePinResponse
from lark_oapi.api.im.v1.model.list_pin_request import ListPinRequest
from lark_oapi.api.im.v1.model.list_pin_response import ListPinResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class Pin(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreatePinRequest, option: RequestOption = RequestOption()) -> CreatePinResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreatePinResponse = JSON.unmarshal(str(resp.content, UTF_8), CreatePinResponse)
        response.raw = resp

        return response

    def delete(self, request: DeletePinRequest, option: RequestOption = RequestOption()) -> DeletePinResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeletePinResponse = JSON.unmarshal(str(resp.content, UTF_8), DeletePinResponse)
        response.raw = resp

        return response

    def list(self, request: ListPinRequest, option: RequestOption = RequestOption()) -> ListPinResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListPinResponse = JSON.unmarshal(str(resp.content, UTF_8), ListPinResponse)
        response.raw = resp

        return response
