# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.corehr.v1.model.create_location_request import CreateLocationRequest
from lark_oapi.api.corehr.v1.model.create_location_response import CreateLocationResponse
from lark_oapi.api.corehr.v1.model.delete_location_request import DeleteLocationRequest
from lark_oapi.api.corehr.v1.model.delete_location_response import DeleteLocationResponse
from lark_oapi.api.corehr.v1.model.get_location_request import GetLocationRequest
from lark_oapi.api.corehr.v1.model.get_location_response import GetLocationResponse
from lark_oapi.api.corehr.v1.model.list_location_request import ListLocationRequest
from lark_oapi.api.corehr.v1.model.list_location_response import ListLocationResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class Location(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateLocationRequest, option: RequestOption = RequestOption()) -> CreateLocationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateLocationResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteLocationRequest, option: RequestOption = RequestOption()) -> DeleteLocationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteLocationResponse)
        response.raw = resp

        return response

    def get(self, request: GetLocationRequest, option: RequestOption = RequestOption()) -> GetLocationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), GetLocationResponse)
        response.raw = resp

        return response

    def list(self, request: ListLocationRequest, option: RequestOption = RequestOption()) -> ListLocationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), ListLocationResponse)
        response.raw = resp

        return response