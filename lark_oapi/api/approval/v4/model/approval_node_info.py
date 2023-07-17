# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .approver_chosen_range import ApproverChosenRange


class ApprovalNodeInfo(object):
    _types = {
        "name": str,
        "need_approver": bool,
        "node_id": str,
        "custom_node_id": str,
        "node_type": str,
        "approver_chosen_multi": bool,
        "approver_chosen_range": List[ApproverChosenRange],
        "require_signature": bool,
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        self.need_approver: Optional[bool] = None
        self.node_id: Optional[str] = None
        self.custom_node_id: Optional[str] = None
        self.node_type: Optional[str] = None
        self.approver_chosen_multi: Optional[bool] = None
        self.approver_chosen_range: Optional[List[ApproverChosenRange]] = None
        self.require_signature: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalNodeInfoBuilder":
        return ApprovalNodeInfoBuilder()


class ApprovalNodeInfoBuilder(object):
    def __init__(self, approval_node_info: ApprovalNodeInfo = ApprovalNodeInfo({})) -> None:
        self._approval_node_info: ApprovalNodeInfo = approval_node_info

    def name(self, name: str) -> "ApprovalNodeInfoBuilder":
        self._approval_node_info.name = name
        return self

    def need_approver(self, need_approver: bool) -> "ApprovalNodeInfoBuilder":
        self._approval_node_info.need_approver = need_approver
        return self

    def node_id(self, node_id: str) -> "ApprovalNodeInfoBuilder":
        self._approval_node_info.node_id = node_id
        return self

    def custom_node_id(self, custom_node_id: str) -> "ApprovalNodeInfoBuilder":
        self._approval_node_info.custom_node_id = custom_node_id
        return self

    def node_type(self, node_type: str) -> "ApprovalNodeInfoBuilder":
        self._approval_node_info.node_type = node_type
        return self

    def approver_chosen_multi(self, approver_chosen_multi: bool) -> "ApprovalNodeInfoBuilder":
        self._approval_node_info.approver_chosen_multi = approver_chosen_multi
        return self

    def approver_chosen_range(self, approver_chosen_range: List[ApproverChosenRange]) -> "ApprovalNodeInfoBuilder":
        self._approval_node_info.approver_chosen_range = approver_chosen_range
        return self

    def require_signature(self, require_signature: bool) -> "ApprovalNodeInfoBuilder":
        self._approval_node_info.require_signature = require_signature
        return self

    def build(self) -> "ApprovalNodeInfo":
        return self._approval_node_info
