# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BatchDeleteMailgroupMemberRequestBody(object):
    _types = {
        "member_id_list": List[str],
    }

    def __init__(self, d):
        self.member_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteMailgroupMemberRequestBodyBuilder":
        return BatchDeleteMailgroupMemberRequestBodyBuilder()


class BatchDeleteMailgroupMemberRequestBodyBuilder(object):
    def __init__(self,
                 batch_delete_mailgroup_member_request_body: BatchDeleteMailgroupMemberRequestBody = BatchDeleteMailgroupMemberRequestBody(
                     {})) -> None:
        self._batch_delete_mailgroup_member_request_body: BatchDeleteMailgroupMemberRequestBody = batch_delete_mailgroup_member_request_body

    def member_id_list(self, member_id_list: List[str]) -> "BatchDeleteMailgroupMemberRequestBodyBuilder":
        self._batch_delete_mailgroup_member_request_body.member_id_list = member_id_list
        return self

    def build(self) -> "BatchDeleteMailgroupMemberRequestBody":
        return self._batch_delete_mailgroup_member_request_body
