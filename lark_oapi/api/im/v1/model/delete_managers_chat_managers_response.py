# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .delete_managers_chat_managers_response_body import DeleteManagersChatManagersResponseBody


class DeleteManagersChatManagersResponse(BaseResponse):
    _types = {
        "data": DeleteManagersChatManagersResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[DeleteManagersChatManagersResponseBody] = None
        init(self, d, self._types)
