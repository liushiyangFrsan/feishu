# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_tenant_product_assign_info_response_body import QueryTenantProductAssignInfoResponseBody


class QueryTenantProductAssignInfoResponse(BaseResponse):
    _types = {
        "data": QueryTenantProductAssignInfoResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[QueryTenantProductAssignInfoResponseBody] = None
        init(self, d, self._types)
