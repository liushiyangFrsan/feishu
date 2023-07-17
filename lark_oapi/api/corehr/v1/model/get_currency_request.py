# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetCurrencyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.currency_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetCurrencyRequestBuilder":
        return GetCurrencyRequestBuilder()


class GetCurrencyRequestBuilder(object):

    def __init__(self, get_currency_request: GetCurrencyRequest = GetCurrencyRequest()) -> None:
        get_currency_request.http_method = HttpMethod.GET
        get_currency_request.uri = "/open-apis/corehr/v1/currencies/:currency_id"
        get_currency_request.token_types = {AccessTokenType.TENANT}
        self._get_currency_request: GetCurrencyRequest = get_currency_request

    def currency_id(self, currency_id: str) -> "GetCurrencyRequestBuilder":
        self._get_currency_request.currency_id = currency_id
        self._get_currency_request.paths["currency_id"] = currency_id
        return self

    def build(self) -> GetCurrencyRequest:
        return self._get_currency_request
