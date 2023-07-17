# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .chat_top_notice import ChatTopNotice


class PutTopNoticeChatTopNoticeRequestBody(object):
    _types = {
        "chat_top_notice": List[ChatTopNotice],
    }

    def __init__(self, d):
        self.chat_top_notice: Optional[List[ChatTopNotice]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PutTopNoticeChatTopNoticeRequestBodyBuilder":
        return PutTopNoticeChatTopNoticeRequestBodyBuilder()


class PutTopNoticeChatTopNoticeRequestBodyBuilder(object):
    def __init__(self,
                 put_top_notice_chat_top_notice_request_body: PutTopNoticeChatTopNoticeRequestBody = PutTopNoticeChatTopNoticeRequestBody(
                     {})) -> None:
        self._put_top_notice_chat_top_notice_request_body: PutTopNoticeChatTopNoticeRequestBody = put_top_notice_chat_top_notice_request_body

    def chat_top_notice(self, chat_top_notice: List[ChatTopNotice]) -> "PutTopNoticeChatTopNoticeRequestBodyBuilder":
        self._put_top_notice_chat_top_notice_request_body.chat_top_notice = chat_top_notice
        return self

    def build(self) -> "PutTopNoticeChatTopNoticeRequestBody":
        return self._put_top_notice_chat_top_notice_request_body
