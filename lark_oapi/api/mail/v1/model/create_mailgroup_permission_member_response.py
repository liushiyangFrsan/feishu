# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_mailgroup_permission_member_response_body import CreateMailgroupPermissionMemberResponseBody


class CreateMailgroupPermissionMemberResponse(BaseResponse):
    _types = {
        "data": CreateMailgroupPermissionMemberResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateMailgroupPermissionMemberResponseBody] = None
        init(self, d, self._types)
