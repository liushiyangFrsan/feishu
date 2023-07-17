# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListMetricSourceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None

    @staticmethod
    def builder() -> "ListMetricSourceRequestBuilder":
        return ListMetricSourceRequestBuilder()


class ListMetricSourceRequestBuilder(object):

    def __init__(self, list_metric_source_request: ListMetricSourceRequest = ListMetricSourceRequest()) -> None:
        list_metric_source_request.http_method = HttpMethod.GET
        list_metric_source_request.uri = "/open-apis/okr/v1/metric_sources"
        list_metric_source_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_metric_source_request: ListMetricSourceRequest = list_metric_source_request

    def page_token(self, page_token: str) -> "ListMetricSourceRequestBuilder":
        self._list_metric_source_request.page_token = page_token
        self._list_metric_source_request.queries["page_token"] = str(page_token)
        return self

    def page_size(self, page_size: str) -> "ListMetricSourceRequestBuilder":
        self._list_metric_source_request.page_size = page_size
        self._list_metric_source_request.queries["page_size"] = str(page_size)
        return self

    def build(self) -> ListMetricSourceRequest:
        return self._list_metric_source_request
