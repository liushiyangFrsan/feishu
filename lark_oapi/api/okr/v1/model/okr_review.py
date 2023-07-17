# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .okr_objective_aligned_objective_owner import OkrObjectiveAlignedObjectiveOwner
from .okr_review_period import OkrReviewPeriod


class OkrReview(object):
    _types = {
        "user_id": OkrObjectiveAlignedObjectiveOwner,
        "review_period_list": List[OkrReviewPeriod],
    }

    def __init__(self, d):
        self.user_id: Optional[OkrObjectiveAlignedObjectiveOwner] = None
        self.review_period_list: Optional[List[OkrReviewPeriod]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrReviewBuilder":
        return OkrReviewBuilder()


class OkrReviewBuilder(object):
    def __init__(self, okr_review: OkrReview = OkrReview({})) -> None:
        self._okr_review: OkrReview = okr_review

    def user_id(self, user_id: OkrObjectiveAlignedObjectiveOwner) -> "OkrReviewBuilder":
        self._okr_review.user_id = user_id
        return self

    def review_period_list(self, review_period_list: List[OkrReviewPeriod]) -> "OkrReviewBuilder":
        self._okr_review.review_period_list = review_period_list
        return self

    def build(self) -> "OkrReview":
        return self._okr_review
