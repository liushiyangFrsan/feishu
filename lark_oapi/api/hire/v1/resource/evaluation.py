# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.hire.v1.model.list_evaluation_request import ListEvaluationRequest
from lark_oapi.api.hire.v1.model.list_evaluation_response import ListEvaluationResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class Evaluation(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def list(self, request: ListEvaluationRequest, option: RequestOption = RequestOption()) -> ListEvaluationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListEvaluationResponse = JSON.unmarshal(str(resp.content, UTF_8), ListEvaluationResponse)
        response.raw = resp

        return response
