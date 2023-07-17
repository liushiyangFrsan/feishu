# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .mailgroup_member import MailgroupMember


class BatchCreateMailgroupMemberRequestBody(object):
    _types = {
        "items": List[MailgroupMember],
    }

    def __init__(self, d):
        self.items: Optional[List[MailgroupMember]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateMailgroupMemberRequestBodyBuilder":
        return BatchCreateMailgroupMemberRequestBodyBuilder()


class BatchCreateMailgroupMemberRequestBodyBuilder(object):
    def __init__(self,
                 batch_create_mailgroup_member_request_body: BatchCreateMailgroupMemberRequestBody = BatchCreateMailgroupMemberRequestBody(
                     {})) -> None:
        self._batch_create_mailgroup_member_request_body: BatchCreateMailgroupMemberRequestBody = batch_create_mailgroup_member_request_body

    def items(self, items: List[MailgroupMember]) -> "BatchCreateMailgroupMemberRequestBodyBuilder":
        self._batch_create_mailgroup_member_request_body.items = items
        return self

    def build(self) -> "BatchCreateMailgroupMemberRequestBody":
        return self._batch_create_mailgroup_member_request_body
