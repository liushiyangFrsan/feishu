# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .website_delivery_resume import WebsiteDeliveryResume


class WebsiteDelivery(object):
    _types = {
        "job_post_id": str,
        "resume": WebsiteDeliveryResume,
        "user_id": str,
        "application_preferred_city_code_list": List[str],
        "channel_id": str,
    }

    def __init__(self, d):
        self.job_post_id: Optional[str] = None
        self.resume: Optional[WebsiteDeliveryResume] = None
        self.user_id: Optional[str] = None
        self.application_preferred_city_code_list: Optional[List[str]] = None
        self.channel_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliveryBuilder":
        return WebsiteDeliveryBuilder()


class WebsiteDeliveryBuilder(object):
    def __init__(self, website_delivery: WebsiteDelivery = WebsiteDelivery({})) -> None:
        self._website_delivery: WebsiteDelivery = website_delivery

    def job_post_id(self, job_post_id: str) -> "WebsiteDeliveryBuilder":
        self._website_delivery.job_post_id = job_post_id
        return self

    def resume(self, resume: WebsiteDeliveryResume) -> "WebsiteDeliveryBuilder":
        self._website_delivery.resume = resume
        return self

    def user_id(self, user_id: str) -> "WebsiteDeliveryBuilder":
        self._website_delivery.user_id = user_id
        return self

    def application_preferred_city_code_list(self, application_preferred_city_code_list: List[
        str]) -> "WebsiteDeliveryBuilder":
        self._website_delivery.application_preferred_city_code_list = application_preferred_city_code_list
        return self

    def channel_id(self, channel_id: str) -> "WebsiteDeliveryBuilder":
        self._website_delivery.channel_id = channel_id
        return self

    def build(self) -> "WebsiteDelivery":
        return self._website_delivery
