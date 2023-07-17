# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class Website(object):
    _types = {
        "id": str,
        "name": I18n,
        "process_type_list": List[int],
        "job_channel_id": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.process_type_list: Optional[List[int]] = None
        self.job_channel_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteBuilder":
        return WebsiteBuilder()


class WebsiteBuilder(object):
    def __init__(self, website: Website = Website({})) -> None:
        self._website: Website = website

    def id(self, id: str) -> "WebsiteBuilder":
        self._website.id = id
        return self

    def name(self, name: I18n) -> "WebsiteBuilder":
        self._website.name = name
        return self

    def process_type_list(self, process_type_list: List[int]) -> "WebsiteBuilder":
        self._website.process_type_list = process_type_list
        return self

    def job_channel_id(self, job_channel_id: str) -> "WebsiteBuilder":
        self._website.job_channel_id = job_channel_id
        return self

    def build(self) -> "Website":
        return self._website
