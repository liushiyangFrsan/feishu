# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.admin.v1.model.list_admin_dept_stat_request import ListAdminDeptStatRequest
from lark_oapi.api.admin.v1.model.list_admin_dept_stat_response import ListAdminDeptStatResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class AdminDeptStat(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def list(self, request: ListAdminDeptStatRequest,
             option: RequestOption = RequestOption()) -> ListAdminDeptStatResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAdminDeptStatResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAdminDeptStatResponse)
        response.raw = resp

        return response
