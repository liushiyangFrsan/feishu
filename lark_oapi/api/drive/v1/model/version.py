# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Version(object):
    _types = {
        "name": str,
        "version": str,
        "parent_token": str,
        "owner_id": str,
        "creator_id": str,
        "create_time": int,
        "update_time": int,
        "status": int,
        "obj_type": str,
        "parent_type": str,
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        self.version: Optional[str] = None
        self.parent_token: Optional[str] = None
        self.owner_id: Optional[str] = None
        self.creator_id: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.status: Optional[int] = None
        self.obj_type: Optional[str] = None
        self.parent_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "VersionBuilder":
        return VersionBuilder()


class VersionBuilder(object):
    def __init__(self, version: Version = Version({})) -> None:
        self._version: Version = version

    def name(self, name: str) -> "VersionBuilder":
        self._version.name = name
        return self

    def version(self, version: str) -> "VersionBuilder":
        self._version.version = version
        return self

    def parent_token(self, parent_token: str) -> "VersionBuilder":
        self._version.parent_token = parent_token
        return self

    def owner_id(self, owner_id: str) -> "VersionBuilder":
        self._version.owner_id = owner_id
        return self

    def creator_id(self, creator_id: str) -> "VersionBuilder":
        self._version.creator_id = creator_id
        return self

    def create_time(self, create_time: int) -> "VersionBuilder":
        self._version.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "VersionBuilder":
        self._version.update_time = update_time
        return self

    def status(self, status: int) -> "VersionBuilder":
        self._version.status = status
        return self

    def obj_type(self, obj_type: str) -> "VersionBuilder":
        self._version.obj_type = obj_type
        return self

    def parent_type(self, parent_type: str) -> "VersionBuilder":
        self._version.parent_type = parent_type
        return self

    def build(self) -> "Version":
        return self._version
