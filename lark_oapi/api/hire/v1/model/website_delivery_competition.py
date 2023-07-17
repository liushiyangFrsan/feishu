# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .website_delivery_customized_data import WebsiteDeliveryCustomizedData


class WebsiteDeliveryCompetition(object):
    _types = {
        "customized_data": List[WebsiteDeliveryCustomizedData],
        "desc": str,
        "name": str,
    }

    def __init__(self, d):
        self.customized_data: Optional[List[WebsiteDeliveryCustomizedData]] = None
        self.desc: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliveryCompetitionBuilder":
        return WebsiteDeliveryCompetitionBuilder()


class WebsiteDeliveryCompetitionBuilder(object):
    def __init__(self,
                 website_delivery_competition: WebsiteDeliveryCompetition = WebsiteDeliveryCompetition({})) -> None:
        self._website_delivery_competition: WebsiteDeliveryCompetition = website_delivery_competition

    def customized_data(self,
                        customized_data: List[WebsiteDeliveryCustomizedData]) -> "WebsiteDeliveryCompetitionBuilder":
        self._website_delivery_competition.customized_data = customized_data
        return self

    def desc(self, desc: str) -> "WebsiteDeliveryCompetitionBuilder":
        self._website_delivery_competition.desc = desc
        return self

    def name(self, name: str) -> "WebsiteDeliveryCompetitionBuilder":
        self._website_delivery_competition.name = name
        return self

    def build(self) -> "WebsiteDeliveryCompetition":
        return self._website_delivery_competition
