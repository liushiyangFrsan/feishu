# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MultiRange(object):
    _types = {
        "ranges": List[str],
    }

    def __init__(self, d):
        self.ranges: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MultiRangeBuilder":
        return MultiRangeBuilder()


class MultiRangeBuilder(object):
    def __init__(self, multi_range: MultiRange = MultiRange({})) -> None:
        self._multi_range: MultiRange = multi_range

    def ranges(self, ranges: List[str]) -> "MultiRangeBuilder":
        self._multi_range.ranges = ranges
        return self

    def build(self) -> "MultiRange":
        return self._multi_range
