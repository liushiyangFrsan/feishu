# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .badge import Badge


class CreateBadgeResponseBody(object):
    _types = {
        "badge": Badge,
    }

    def __init__(self, d):
        self.badge: Optional[Badge] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateBadgeResponseBodyBuilder":
        return CreateBadgeResponseBodyBuilder()


class CreateBadgeResponseBodyBuilder(object):
    def __init__(self, create_badge_response_body: CreateBadgeResponseBody = CreateBadgeResponseBody({})) -> None:
        self._create_badge_response_body: CreateBadgeResponseBody = create_badge_response_body

    def badge(self, badge: Badge) -> "CreateBadgeResponseBodyBuilder":
        self._create_badge_response_body.badge = badge
        return self

    def build(self) -> "CreateBadgeResponseBody":
        return self._create_badge_response_body
