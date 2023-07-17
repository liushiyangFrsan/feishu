# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.approval.v4.model.create_instance_comment_request import CreateInstanceCommentRequest
from lark_oapi.api.approval.v4.model.create_instance_comment_response import CreateInstanceCommentResponse
from lark_oapi.api.approval.v4.model.delete_instance_comment_request import DeleteInstanceCommentRequest
from lark_oapi.api.approval.v4.model.delete_instance_comment_response import DeleteInstanceCommentResponse
from lark_oapi.api.approval.v4.model.list_instance_comment_request import ListInstanceCommentRequest
from lark_oapi.api.approval.v4.model.list_instance_comment_response import ListInstanceCommentResponse
from lark_oapi.api.approval.v4.model.remove_instance_comment_request import RemoveInstanceCommentRequest
from lark_oapi.api.approval.v4.model.remove_instance_comment_response import RemoveInstanceCommentResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class InstanceComment(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateInstanceCommentRequest,
               option: RequestOption = RequestOption()) -> CreateInstanceCommentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateInstanceCommentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 CreateInstanceCommentResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteInstanceCommentRequest,
               option: RequestOption = RequestOption()) -> DeleteInstanceCommentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteInstanceCommentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 DeleteInstanceCommentResponse)
        response.raw = resp

        return response

    def list(self, request: ListInstanceCommentRequest,
             option: RequestOption = RequestOption()) -> ListInstanceCommentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListInstanceCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), ListInstanceCommentResponse)
        response.raw = resp

        return response

    def remove(self, request: RemoveInstanceCommentRequest,
               option: RequestOption = RequestOption()) -> RemoveInstanceCommentResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: RemoveInstanceCommentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 RemoveInstanceCommentResponse)
        response.raw = resp

        return response
