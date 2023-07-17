# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_user_mailbox_alias_response_body import ListUserMailboxAliasResponseBody


class ListUserMailboxAliasResponse(BaseResponse):
    _types = {
        "data": ListUserMailboxAliasResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListUserMailboxAliasResponseBody] = None
        init(self, d, self._types)
