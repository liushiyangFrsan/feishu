# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .interview_round_type_assessment_template import InterviewRoundTypeAssessmentTemplate


class InterviewRoundType(object):
    _types = {
        "id": str,
        "biz_id": str,
        "name": I18n,
        "process_type": int,
        "active_status": int,
        "interview_assessment_template_info": InterviewRoundTypeAssessmentTemplate,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.biz_id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.process_type: Optional[int] = None
        self.active_status: Optional[int] = None
        self.interview_assessment_template_info: Optional[InterviewRoundTypeAssessmentTemplate] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewRoundTypeBuilder":
        return InterviewRoundTypeBuilder()


class InterviewRoundTypeBuilder(object):
    def __init__(self, interview_round_type: InterviewRoundType = InterviewRoundType({})) -> None:
        self._interview_round_type: InterviewRoundType = interview_round_type

    def id(self, id: str) -> "InterviewRoundTypeBuilder":
        self._interview_round_type.id = id
        return self

    def biz_id(self, biz_id: str) -> "InterviewRoundTypeBuilder":
        self._interview_round_type.biz_id = biz_id
        return self

    def name(self, name: I18n) -> "InterviewRoundTypeBuilder":
        self._interview_round_type.name = name
        return self

    def process_type(self, process_type: int) -> "InterviewRoundTypeBuilder":
        self._interview_round_type.process_type = process_type
        return self

    def active_status(self, active_status: int) -> "InterviewRoundTypeBuilder":
        self._interview_round_type.active_status = active_status
        return self

    def interview_assessment_template_info(self,
                                           interview_assessment_template_info: InterviewRoundTypeAssessmentTemplate) -> "InterviewRoundTypeBuilder":
        self._interview_round_type.interview_assessment_template_info = interview_assessment_template_info
        return self

    def build(self) -> "InterviewRoundType":
        return self._interview_round_type
