# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .tasklist import Tasklist


class RemoveMembersTasklistResponseBody(object):
    _types = {
        "tasklist": Tasklist,
    }

    def __init__(self, d=None):
        self.tasklist: Optional[Tasklist] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RemoveMembersTasklistResponseBodyBuilder":
        return RemoveMembersTasklistResponseBodyBuilder()


class RemoveMembersTasklistResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._remove_members_tasklist_response_body = RemoveMembersTasklistResponseBody()

    def tasklist(self, tasklist: Tasklist) -> "RemoveMembersTasklistResponseBodyBuilder":
        self._remove_members_tasklist_response_body.tasklist = tasklist
        return self

    def build(self) -> "RemoveMembersTasklistResponseBody":
        return self._remove_members_tasklist_response_body