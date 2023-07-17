# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Node(object):
    _types = {
        "space_id": int,
        "node_token": str,
        "obj_token": str,
        "obj_type": str,
        "parent_node_token": str,
        "node_type": str,
        "origin_node_token": str,
        "origin_space_id": int,
        "has_child": bool,
        "title": str,
        "obj_create_time": int,
        "obj_edit_time": int,
        "node_create_time": int,
        "creator": str,
        "owner": str,
    }

    def __init__(self, d):
        self.space_id: Optional[int] = None
        self.node_token: Optional[str] = None
        self.obj_token: Optional[str] = None
        self.obj_type: Optional[str] = None
        self.parent_node_token: Optional[str] = None
        self.node_type: Optional[str] = None
        self.origin_node_token: Optional[str] = None
        self.origin_space_id: Optional[int] = None
        self.has_child: Optional[bool] = None
        self.title: Optional[str] = None
        self.obj_create_time: Optional[int] = None
        self.obj_edit_time: Optional[int] = None
        self.node_create_time: Optional[int] = None
        self.creator: Optional[str] = None
        self.owner: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NodeBuilder":
        return NodeBuilder()


class NodeBuilder(object):
    def __init__(self, node: Node = Node({})) -> None:
        self._node: Node = node

    def space_id(self, space_id: int) -> "NodeBuilder":
        self._node.space_id = space_id
        return self

    def node_token(self, node_token: str) -> "NodeBuilder":
        self._node.node_token = node_token
        return self

    def obj_token(self, obj_token: str) -> "NodeBuilder":
        self._node.obj_token = obj_token
        return self

    def obj_type(self, obj_type: str) -> "NodeBuilder":
        self._node.obj_type = obj_type
        return self

    def parent_node_token(self, parent_node_token: str) -> "NodeBuilder":
        self._node.parent_node_token = parent_node_token
        return self

    def node_type(self, node_type: str) -> "NodeBuilder":
        self._node.node_type = node_type
        return self

    def origin_node_token(self, origin_node_token: str) -> "NodeBuilder":
        self._node.origin_node_token = origin_node_token
        return self

    def origin_space_id(self, origin_space_id: int) -> "NodeBuilder":
        self._node.origin_space_id = origin_space_id
        return self

    def has_child(self, has_child: bool) -> "NodeBuilder":
        self._node.has_child = has_child
        return self

    def title(self, title: str) -> "NodeBuilder":
        self._node.title = title
        return self

    def obj_create_time(self, obj_create_time: int) -> "NodeBuilder":
        self._node.obj_create_time = obj_create_time
        return self

    def obj_edit_time(self, obj_edit_time: int) -> "NodeBuilder":
        self._node.obj_edit_time = obj_edit_time
        return self

    def node_create_time(self, node_create_time: int) -> "NodeBuilder":
        self._node.node_create_time = node_create_time
        return self

    def creator(self, creator: str) -> "NodeBuilder":
        self._node.creator = creator
        return self

    def owner(self, owner: str) -> "NodeBuilder":
        self._node.owner = owner
        return self

    def build(self) -> "Node":
        return self._node
