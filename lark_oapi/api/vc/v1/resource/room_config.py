# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.vc.v1.model.query_room_config_request import QueryRoomConfigRequest
from lark_oapi.api.vc.v1.model.query_room_config_response import QueryRoomConfigResponse
from lark_oapi.api.vc.v1.model.set_checkboard_access_code_room_config_request import \
    SetCheckboardAccessCodeRoomConfigRequest
from lark_oapi.api.vc.v1.model.set_checkboard_access_code_room_config_response import \
    SetCheckboardAccessCodeRoomConfigResponse
from lark_oapi.api.vc.v1.model.set_room_access_code_room_config_request import SetRoomAccessCodeRoomConfigRequest
from lark_oapi.api.vc.v1.model.set_room_access_code_room_config_response import SetRoomAccessCodeRoomConfigResponse
from lark_oapi.api.vc.v1.model.set_room_config_request import SetRoomConfigRequest
from lark_oapi.api.vc.v1.model.set_room_config_response import SetRoomConfigResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class RoomConfig(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def query(self, request: QueryRoomConfigRequest,
              option: RequestOption = RequestOption()) -> QueryRoomConfigResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryRoomConfigResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryRoomConfigResponse)
        response.raw = resp

        return response

    def set(self, request: SetRoomConfigRequest, option: RequestOption = RequestOption()) -> SetRoomConfigResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SetRoomConfigResponse = JSON.unmarshal(str(resp.content, UTF_8), SetRoomConfigResponse)
        response.raw = resp

        return response

    def set_checkboard_access_code(self, request: SetCheckboardAccessCodeRoomConfigRequest,
                                   option: RequestOption = RequestOption()) -> SetCheckboardAccessCodeRoomConfigResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SetCheckboardAccessCodeRoomConfigResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                             SetCheckboardAccessCodeRoomConfigResponse)
        response.raw = resp

        return response

    def set_room_access_code(self, request: SetRoomAccessCodeRoomConfigRequest,
                             option: RequestOption = RequestOption()) -> SetRoomAccessCodeRoomConfigResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SetRoomAccessCodeRoomConfigResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                       SetRoomAccessCodeRoomConfigResponse)
        response.raw = resp

        return response
