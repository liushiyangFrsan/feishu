# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .content_block import ContentBlock


class CreateProgressRecordResponseBody(object):
    _types = {
        "progress_id": int,
        "modify_time": int,
        "content": ContentBlock,
    }

    def __init__(self, d):
        self.progress_id: Optional[int] = None
        self.modify_time: Optional[int] = None
        self.content: Optional[ContentBlock] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateProgressRecordResponseBodyBuilder":
        return CreateProgressRecordResponseBodyBuilder()


class CreateProgressRecordResponseBodyBuilder(object):
    def __init__(self,
                 create_progress_record_response_body: CreateProgressRecordResponseBody = CreateProgressRecordResponseBody(
                     {})) -> None:
        self._create_progress_record_response_body: CreateProgressRecordResponseBody = create_progress_record_response_body

    def progress_id(self, progress_id: int) -> "CreateProgressRecordResponseBodyBuilder":
        self._create_progress_record_response_body.progress_id = progress_id
        return self

    def modify_time(self, modify_time: int) -> "CreateProgressRecordResponseBodyBuilder":
        self._create_progress_record_response_body.modify_time = modify_time
        return self

    def content(self, content: ContentBlock) -> "CreateProgressRecordResponseBodyBuilder":
        self._create_progress_record_response_body.content = content
        return self

    def build(self) -> "CreateProgressRecordResponseBody":
        return self._create_progress_record_response_body
