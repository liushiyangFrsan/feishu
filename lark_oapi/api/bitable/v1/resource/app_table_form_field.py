# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.bitable.v1.model.list_app_table_form_field_request import ListAppTableFormFieldRequest
from lark_oapi.api.bitable.v1.model.list_app_table_form_field_response import ListAppTableFormFieldResponse
from lark_oapi.api.bitable.v1.model.patch_app_table_form_field_request import PatchAppTableFormFieldRequest
from lark_oapi.api.bitable.v1.model.patch_app_table_form_field_response import PatchAppTableFormFieldResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class AppTableFormField(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def list(self, request: ListAppTableFormFieldRequest,
             option: RequestOption = RequestOption()) -> ListAppTableFormFieldResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAppTableFormFieldResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 ListAppTableFormFieldResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchAppTableFormFieldRequest,
              option: RequestOption = RequestOption()) -> PatchAppTableFormFieldResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchAppTableFormFieldResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  PatchAppTableFormFieldResponse)
        response.raw = resp

        return response
