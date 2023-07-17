# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class GetFileVersionResponseBody(object):
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
    def builder() -> "GetFileVersionResponseBodyBuilder":
        return GetFileVersionResponseBodyBuilder()


class GetFileVersionResponseBodyBuilder(object):
    def __init__(self,
                 get_file_version_response_body: GetFileVersionResponseBody = GetFileVersionResponseBody({})) -> None:
        self._get_file_version_response_body: GetFileVersionResponseBody = get_file_version_response_body

    def name(self, name: str) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.name = name
        return self

    def version(self, version: str) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.version = version
        return self

    def parent_token(self, parent_token: str) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.parent_token = parent_token
        return self

    def owner_id(self, owner_id: str) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.owner_id = owner_id
        return self

    def creator_id(self, creator_id: str) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.creator_id = creator_id
        return self

    def create_time(self, create_time: int) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.update_time = update_time
        return self

    def status(self, status: int) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.status = status
        return self

    def obj_type(self, obj_type: str) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.obj_type = obj_type
        return self

    def parent_type(self, parent_type: str) -> "GetFileVersionResponseBodyBuilder":
        self._get_file_version_response_body.parent_type = parent_type
        return self

    def build(self) -> "GetFileVersionResponseBody":
        return self._get_file_version_response_body
