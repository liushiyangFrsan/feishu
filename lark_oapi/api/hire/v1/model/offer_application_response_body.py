# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application_offer import ApplicationOffer


class OfferApplicationResponseBody(object):
    _types = {
        "offer": ApplicationOffer,
    }

    def __init__(self, d):
        self.offer: Optional[ApplicationOffer] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplicationResponseBodyBuilder":
        return OfferApplicationResponseBodyBuilder()


class OfferApplicationResponseBodyBuilder(object):
    def __init__(self, offer_application_response_body: OfferApplicationResponseBody = OfferApplicationResponseBody(
        {})) -> None:
        self._offer_application_response_body: OfferApplicationResponseBody = offer_application_response_body

    def offer(self, offer: ApplicationOffer) -> "OfferApplicationResponseBodyBuilder":
        self._offer_application_response_body.offer = offer
        return self

    def build(self) -> "OfferApplicationResponseBody":
        return self._offer_application_response_body
