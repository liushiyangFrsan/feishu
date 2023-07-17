# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ReplyMessageRequestBody(object):
    _types = {
        "content": str,
        "msg_type": str,
        "uuid": str,
    }

    def __init__(self, d):
        self.content: Optional[str] = None
        self.msg_type: Optional[str] = None
        self.uuid: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReplyMessageRequestBodyBuilder":
        return ReplyMessageRequestBodyBuilder()


class ReplyMessageRequestBodyBuilder(object):
    def __init__(self, reply_message_request_body: ReplyMessageRequestBody = ReplyMessageRequestBody({})) -> None:
        self._reply_message_request_body: ReplyMessageRequestBody = reply_message_request_body

    def content(self, content: str) -> "ReplyMessageRequestBodyBuilder":
        self._reply_message_request_body.content = content
        return self

    def msg_type(self, msg_type: str) -> "ReplyMessageRequestBodyBuilder":
        self._reply_message_request_body.msg_type = msg_type
        return self

    def uuid(self, uuid: str) -> "ReplyMessageRequestBodyBuilder":
        self._reply_message_request_body.uuid = uuid
        return self

    def build(self) -> "ReplyMessageRequestBody":
        return self._reply_message_request_body
