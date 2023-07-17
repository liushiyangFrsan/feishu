# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.mail.v1.model.batch_create_public_mailbox_member_request import BatchCreatePublicMailboxMemberRequest
from lark_oapi.api.mail.v1.model.batch_create_public_mailbox_member_response import \
    BatchCreatePublicMailboxMemberResponse
from lark_oapi.api.mail.v1.model.batch_delete_public_mailbox_member_request import BatchDeletePublicMailboxMemberRequest
from lark_oapi.api.mail.v1.model.batch_delete_public_mailbox_member_response import \
    BatchDeletePublicMailboxMemberResponse
from lark_oapi.api.mail.v1.model.clear_public_mailbox_member_request import ClearPublicMailboxMemberRequest
from lark_oapi.api.mail.v1.model.clear_public_mailbox_member_response import ClearPublicMailboxMemberResponse
from lark_oapi.api.mail.v1.model.create_public_mailbox_member_request import CreatePublicMailboxMemberRequest
from lark_oapi.api.mail.v1.model.create_public_mailbox_member_response import CreatePublicMailboxMemberResponse
from lark_oapi.api.mail.v1.model.delete_public_mailbox_member_request import DeletePublicMailboxMemberRequest
from lark_oapi.api.mail.v1.model.delete_public_mailbox_member_response import DeletePublicMailboxMemberResponse
from lark_oapi.api.mail.v1.model.get_public_mailbox_member_request import GetPublicMailboxMemberRequest
from lark_oapi.api.mail.v1.model.get_public_mailbox_member_response import GetPublicMailboxMemberResponse
from lark_oapi.api.mail.v1.model.list_public_mailbox_member_request import ListPublicMailboxMemberRequest
from lark_oapi.api.mail.v1.model.list_public_mailbox_member_response import ListPublicMailboxMemberResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class PublicMailboxMember(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def batch_create(self, request: BatchCreatePublicMailboxMemberRequest,
                     option: RequestOption = RequestOption()) -> BatchCreatePublicMailboxMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchCreatePublicMailboxMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          BatchCreatePublicMailboxMemberResponse)
        response.raw = resp

        return response

    def batch_delete(self, request: BatchDeletePublicMailboxMemberRequest,
                     option: RequestOption = RequestOption()) -> BatchDeletePublicMailboxMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchDeletePublicMailboxMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          BatchDeletePublicMailboxMemberResponse)
        response.raw = resp

        return response

    def clear(self, request: ClearPublicMailboxMemberRequest,
              option: RequestOption = RequestOption()) -> ClearPublicMailboxMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ClearPublicMailboxMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    ClearPublicMailboxMemberResponse)
        response.raw = resp

        return response

    def create(self, request: CreatePublicMailboxMemberRequest,
               option: RequestOption = RequestOption()) -> CreatePublicMailboxMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreatePublicMailboxMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     CreatePublicMailboxMemberResponse)
        response.raw = resp

        return response

    def delete(self, request: DeletePublicMailboxMemberRequest,
               option: RequestOption = RequestOption()) -> DeletePublicMailboxMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeletePublicMailboxMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     DeletePublicMailboxMemberResponse)
        response.raw = resp

        return response

    def get(self, request: GetPublicMailboxMemberRequest,
            option: RequestOption = RequestOption()) -> GetPublicMailboxMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetPublicMailboxMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  GetPublicMailboxMemberResponse)
        response.raw = resp

        return response

    def list(self, request: ListPublicMailboxMemberRequest,
             option: RequestOption = RequestOption()) -> ListPublicMailboxMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListPublicMailboxMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   ListPublicMailboxMemberResponse)
        response.raw = resp

        return response
