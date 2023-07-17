# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .style import Style


class StyleRanges(object):
    _types = {
        "style_ranges": List[Style],
    }

    def __init__(self, d):
        self.style_ranges: Optional[List[Style]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StyleRangesBuilder":
        return StyleRangesBuilder()


class StyleRangesBuilder(object):
    def __init__(self, style_ranges: StyleRanges = StyleRanges({})) -> None:
        self._style_ranges: StyleRanges = style_ranges

    def style_ranges(self, style_ranges: List[Style]) -> "StyleRangesBuilder":
        self._style_ranges.style_ranges = style_ranges
        return self

    def build(self) -> "StyleRanges":
        return self._style_ranges
