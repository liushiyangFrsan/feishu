# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_by_application_referral_response_body import GetByApplicationReferralResponseBody


class GetByApplicationReferralResponse(BaseResponse):
    _types = {
        "data": GetByApplicationReferralResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetByApplicationReferralResponseBody] = None
        init(self, d, self._types)
