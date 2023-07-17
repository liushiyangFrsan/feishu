# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WebsiteDeliveryDto(object):
    _types = {
        "application_id": str,
        "id": str,
        "job_id": str,
        "job_post_id": str,
        "portal_resume_id": str,
        "user_id": str,
        "talent_id": str,
    }

    def __init__(self, d):
        self.application_id: Optional[str] = None
        self.id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.job_post_id: Optional[str] = None
        self.portal_resume_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.talent_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliveryDtoBuilder":
        return WebsiteDeliveryDtoBuilder()


class WebsiteDeliveryDtoBuilder(object):
    def __init__(self, website_delivery_dto: WebsiteDeliveryDto = WebsiteDeliveryDto({})) -> None:
        self._website_delivery_dto: WebsiteDeliveryDto = website_delivery_dto

    def application_id(self, application_id: str) -> "WebsiteDeliveryDtoBuilder":
        self._website_delivery_dto.application_id = application_id
        return self

    def id(self, id: str) -> "WebsiteDeliveryDtoBuilder":
        self._website_delivery_dto.id = id
        return self

    def job_id(self, job_id: str) -> "WebsiteDeliveryDtoBuilder":
        self._website_delivery_dto.job_id = job_id
        return self

    def job_post_id(self, job_post_id: str) -> "WebsiteDeliveryDtoBuilder":
        self._website_delivery_dto.job_post_id = job_post_id
        return self

    def portal_resume_id(self, portal_resume_id: str) -> "WebsiteDeliveryDtoBuilder":
        self._website_delivery_dto.portal_resume_id = portal_resume_id
        return self

    def user_id(self, user_id: str) -> "WebsiteDeliveryDtoBuilder":
        self._website_delivery_dto.user_id = user_id
        return self

    def talent_id(self, talent_id: str) -> "WebsiteDeliveryDtoBuilder":
        self._website_delivery_dto.talent_id = talent_id
        return self

    def build(self) -> "WebsiteDeliveryDto":
        return self._website_delivery_dto
