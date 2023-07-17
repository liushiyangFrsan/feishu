# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .delete_instance_comment_response_body import DeleteInstanceCommentResponseBody


class DeleteInstanceCommentResponse(BaseResponse):
    _types = {
        "data": DeleteInstanceCommentResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[DeleteInstanceCommentResponseBody] = None
        init(self, d, self._types)
