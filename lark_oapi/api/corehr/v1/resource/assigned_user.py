# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.corehr.v1.model.search_assigned_user_request import SearchAssignedUserRequest
from lark_oapi.api.corehr.v1.model.search_assigned_user_response import SearchAssignedUserResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class AssignedUser(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def search(self, request: SearchAssignedUserRequest,
               option: RequestOption = RequestOption()) -> SearchAssignedUserResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchAssignedUserResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchAssignedUserResponse)
        response.raw = resp

        return response
