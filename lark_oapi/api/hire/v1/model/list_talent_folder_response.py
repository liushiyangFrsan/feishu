# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_talent_folder_response_body import ListTalentFolderResponseBody


class ListTalentFolderResponse(BaseResponse):
    _types = {
        "data": ListTalentFolderResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListTalentFolderResponseBody] = None
        init(self, d, self._types)
