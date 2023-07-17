# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Point(object):
    _types = {
        "amount": int,
    }

    def __init__(self, d):
        self.amount: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PointBuilder":
        return PointBuilder()


class PointBuilder(object):
    def __init__(self, point: Point = Point({})) -> None:
        self._point: Point = point

    def amount(self, amount: int) -> "PointBuilder":
        self._point.amount = amount
        return self

    def build(self) -> "Point":
        return self._point
