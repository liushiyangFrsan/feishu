# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Miniprogram(object):
    _types = {
        "enable_pc_mode": int,
        "schema_urls": List[str],
        "pc_use_mobile_pkg": bool,
        "pc_version_id": str,
        "mobile_version_id": str,
        "mobile_min_lark_version": str,
        "pc_min_lark_version": str,
    }

    def __init__(self, d):
        self.enable_pc_mode: Optional[int] = None
        self.schema_urls: Optional[List[str]] = None
        self.pc_use_mobile_pkg: Optional[bool] = None
        self.pc_version_id: Optional[str] = None
        self.mobile_version_id: Optional[str] = None
        self.mobile_min_lark_version: Optional[str] = None
        self.pc_min_lark_version: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MiniprogramBuilder":
        return MiniprogramBuilder()


class MiniprogramBuilder(object):
    def __init__(self, miniprogram: Miniprogram = Miniprogram({})) -> None:
        self._miniprogram: Miniprogram = miniprogram

    def enable_pc_mode(self, enable_pc_mode: int) -> "MiniprogramBuilder":
        self._miniprogram.enable_pc_mode = enable_pc_mode
        return self

    def schema_urls(self, schema_urls: List[str]) -> "MiniprogramBuilder":
        self._miniprogram.schema_urls = schema_urls
        return self

    def pc_use_mobile_pkg(self, pc_use_mobile_pkg: bool) -> "MiniprogramBuilder":
        self._miniprogram.pc_use_mobile_pkg = pc_use_mobile_pkg
        return self

    def pc_version_id(self, pc_version_id: str) -> "MiniprogramBuilder":
        self._miniprogram.pc_version_id = pc_version_id
        return self

    def mobile_version_id(self, mobile_version_id: str) -> "MiniprogramBuilder":
        self._miniprogram.mobile_version_id = mobile_version_id
        return self

    def mobile_min_lark_version(self, mobile_min_lark_version: str) -> "MiniprogramBuilder":
        self._miniprogram.mobile_min_lark_version = mobile_min_lark_version
        return self

    def pc_min_lark_version(self, pc_min_lark_version: str) -> "MiniprogramBuilder":
        self._miniprogram.pc_min_lark_version = pc_min_lark_version
        return self

    def build(self) -> "Miniprogram":
        return self._miniprogram
