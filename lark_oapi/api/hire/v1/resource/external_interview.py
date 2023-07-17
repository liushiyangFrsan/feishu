# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.hire.v1.model.create_external_interview_request import CreateExternalInterviewRequest
from lark_oapi.api.hire.v1.model.create_external_interview_response import CreateExternalInterviewResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class ExternalInterview(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateExternalInterviewRequest,
               option: RequestOption = RequestOption()) -> CreateExternalInterviewResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateExternalInterviewResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   CreateExternalInterviewResponse)
        response.raw = resp

        return response
