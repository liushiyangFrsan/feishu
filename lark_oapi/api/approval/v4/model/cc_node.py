# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .external_instance_link import ExternalInstanceLink


class CcNode(object):
    _types = {
        "cc_id": str,
        "user_id": str,
        "open_id": str,
        "links": ExternalInstanceLink,
        "read_status": str,
        "extra": str,
        "title": str,
        "create_time": int,
        "update_time": int,
        "display_method": str,
    }

    def __init__(self, d):
        self.cc_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.open_id: Optional[str] = None
        self.links: Optional[ExternalInstanceLink] = None
        self.read_status: Optional[str] = None
        self.extra: Optional[str] = None
        self.title: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.display_method: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CcNodeBuilder":
        return CcNodeBuilder()


class CcNodeBuilder(object):
    def __init__(self, cc_node: CcNode = CcNode({})) -> None:
        self._cc_node: CcNode = cc_node

    def cc_id(self, cc_id: str) -> "CcNodeBuilder":
        self._cc_node.cc_id = cc_id
        return self

    def user_id(self, user_id: str) -> "CcNodeBuilder":
        self._cc_node.user_id = user_id
        return self

    def open_id(self, open_id: str) -> "CcNodeBuilder":
        self._cc_node.open_id = open_id
        return self

    def links(self, links: ExternalInstanceLink) -> "CcNodeBuilder":
        self._cc_node.links = links
        return self

    def read_status(self, read_status: str) -> "CcNodeBuilder":
        self._cc_node.read_status = read_status
        return self

    def extra(self, extra: str) -> "CcNodeBuilder":
        self._cc_node.extra = extra
        return self

    def title(self, title: str) -> "CcNodeBuilder":
        self._cc_node.title = title
        return self

    def create_time(self, create_time: int) -> "CcNodeBuilder":
        self._cc_node.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "CcNodeBuilder":
        self._cc_node.update_time = update_time
        return self

    def display_method(self, display_method: str) -> "CcNodeBuilder":
        self._cc_node.display_method = display_method
        return self

    def build(self) -> "CcNode":
        return self._cc_node
