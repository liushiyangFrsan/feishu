# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .translate_text_response_body import TranslateTextResponseBody


class TranslateTextResponse(BaseResponse):
    _types = {
        "data": TranslateTextResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[TranslateTextResponseBody] = None
        init(self, d, self._types)