# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .mailgroup_manager import MailgroupManager


class BatchDeleteMailgroupManagerRequestBody(object):
    _types = {
        "mailgroup_manager_list": List[MailgroupManager],
    }

    def __init__(self, d):
        self.mailgroup_manager_list: Optional[List[MailgroupManager]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteMailgroupManagerRequestBodyBuilder":
        return BatchDeleteMailgroupManagerRequestBodyBuilder()


class BatchDeleteMailgroupManagerRequestBodyBuilder(object):
    def __init__(self,
                 batch_delete_mailgroup_manager_request_body: BatchDeleteMailgroupManagerRequestBody = BatchDeleteMailgroupManagerRequestBody(
                     {})) -> None:
        self._batch_delete_mailgroup_manager_request_body: BatchDeleteMailgroupManagerRequestBody = batch_delete_mailgroup_manager_request_body

    def mailgroup_manager_list(self, mailgroup_manager_list: List[
        MailgroupManager]) -> "BatchDeleteMailgroupManagerRequestBodyBuilder":
        self._batch_delete_mailgroup_manager_request_body.mailgroup_manager_list = mailgroup_manager_list
        return self

    def build(self) -> "BatchDeleteMailgroupManagerRequestBody":
        return self._batch_delete_mailgroup_manager_request_body
