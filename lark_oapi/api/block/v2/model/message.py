# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Message(object):
    _types = {
        "body": str,
        "version": int,
        "block_id": str,
        "resource": str,
        "open_ids": List[str],
    }

    def __init__(self, d):
        self.body: Optional[str] = None
        self.version: Optional[int] = None
        self.block_id: Optional[str] = None
        self.resource: Optional[str] = None
        self.open_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MessageBuilder":
        return MessageBuilder()


class MessageBuilder(object):
    def __init__(self, message: Message = Message({})) -> None:
        self._message: Message = message

    def body(self, body: str) -> "MessageBuilder":
        self._message.body = body
        return self

    def version(self, version: int) -> "MessageBuilder":
        self._message.version = version
        return self

    def block_id(self, block_id: str) -> "MessageBuilder":
        self._message.block_id = block_id
        return self

    def resource(self, resource: str) -> "MessageBuilder":
        self._message.resource = resource
        return self

    def open_ids(self, open_ids: List[str]) -> "MessageBuilder":
        self._message.open_ids = open_ids
        return self

    def build(self) -> "Message":
        return self._message
