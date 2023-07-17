# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ExternalInstanceLink(object):
    _types = {
        "pc_link": str,
        "mobile_link": str,
    }

    def __init__(self, d):
        self.pc_link: Optional[str] = None
        self.mobile_link: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalInstanceLinkBuilder":
        return ExternalInstanceLinkBuilder()


class ExternalInstanceLinkBuilder(object):
    def __init__(self, external_instance_link: ExternalInstanceLink = ExternalInstanceLink({})) -> None:
        self._external_instance_link: ExternalInstanceLink = external_instance_link

    def pc_link(self, pc_link: str) -> "ExternalInstanceLinkBuilder":
        self._external_instance_link.pc_link = pc_link
        return self

    def mobile_link(self, mobile_link: str) -> "ExternalInstanceLinkBuilder":
        self._external_instance_link.mobile_link = mobile_link
        return self

    def build(self) -> "ExternalInstanceLink":
        return self._external_instance_link
