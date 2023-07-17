# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .message import Message


class MergeForwardMessageResponseBody(object):
    _types = {
        "message": Message,
        "invalid_message_id_list": List[str],
    }

    def __init__(self, d):
        self.message: Optional[Message] = None
        self.invalid_message_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MergeForwardMessageResponseBodyBuilder":
        return MergeForwardMessageResponseBodyBuilder()


class MergeForwardMessageResponseBodyBuilder(object):
    def __init__(self,
                 merge_forward_message_response_body: MergeForwardMessageResponseBody = MergeForwardMessageResponseBody(
                     {})) -> None:
        self._merge_forward_message_response_body: MergeForwardMessageResponseBody = merge_forward_message_response_body

    def message(self, message: Message) -> "MergeForwardMessageResponseBodyBuilder":
        self._merge_forward_message_response_body.message = message
        return self

    def invalid_message_id_list(self, invalid_message_id_list: List[str]) -> "MergeForwardMessageResponseBodyBuilder":
        self._merge_forward_message_response_body.invalid_message_id_list = invalid_message_id_list
        return self

    def build(self) -> "MergeForwardMessageResponseBody":
        return self._merge_forward_message_response_body
