# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.corehr.v1.model.get_process_form_variable_data_request import GetProcessFormVariableDataRequest
from lark_oapi.api.corehr.v1.model.get_process_form_variable_data_response import GetProcessFormVariableDataResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class ProcessFormVariableData(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get(self, request: GetProcessFormVariableDataRequest,
            option: RequestOption = RequestOption()) -> GetProcessFormVariableDataResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetProcessFormVariableDataResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      GetProcessFormVariableDataResponse)
        response.raw = resp

        return response
