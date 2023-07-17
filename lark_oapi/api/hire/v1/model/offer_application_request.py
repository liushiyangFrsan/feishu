# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class OfferApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.application_id: Optional[str] = None

    @staticmethod
    def builder() -> "OfferApplicationRequestBuilder":
        return OfferApplicationRequestBuilder()


class OfferApplicationRequestBuilder(object):

    def __init__(self, offer_application_request: OfferApplicationRequest = OfferApplicationRequest()) -> None:
        offer_application_request.http_method = HttpMethod.GET
        offer_application_request.uri = "/open-apis/hire/v1/applications/:application_id/offer"
        offer_application_request.token_types = {AccessTokenType.TENANT}
        self._offer_application_request: OfferApplicationRequest = offer_application_request

    def user_id_type(self, user_id_type: str) -> "OfferApplicationRequestBuilder":
        self._offer_application_request.user_id_type = user_id_type
        self._offer_application_request.queries["user_id_type"] = str(user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "OfferApplicationRequestBuilder":
        self._offer_application_request.department_id_type = department_id_type
        self._offer_application_request.queries["department_id_type"] = str(department_id_type)
        return self

    def application_id(self, application_id: str) -> "OfferApplicationRequestBuilder":
        self._offer_application_request.application_id = application_id
        self._offer_application_request.paths["application_id"] = application_id
        return self

    def build(self) -> OfferApplicationRequest:
        return self._offer_application_request
