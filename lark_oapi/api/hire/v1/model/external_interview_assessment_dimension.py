# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ExternalInterviewAssessmentDimension(object):
    _types = {
        "score": int,
        "option": str,
        "options": List[str],
        "content": str,
        "assessment_type": int,
        "title": str,
        "description": str,
    }

    def __init__(self, d):
        self.score: Optional[int] = None
        self.option: Optional[str] = None
        self.options: Optional[List[str]] = None
        self.content: Optional[str] = None
        self.assessment_type: Optional[int] = None
        self.title: Optional[str] = None
        self.description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalInterviewAssessmentDimensionBuilder":
        return ExternalInterviewAssessmentDimensionBuilder()


class ExternalInterviewAssessmentDimensionBuilder(object):
    def __init__(self,
                 external_interview_assessment_dimension: ExternalInterviewAssessmentDimension = ExternalInterviewAssessmentDimension(
                     {})) -> None:
        self._external_interview_assessment_dimension: ExternalInterviewAssessmentDimension = external_interview_assessment_dimension

    def score(self, score: int) -> "ExternalInterviewAssessmentDimensionBuilder":
        self._external_interview_assessment_dimension.score = score
        return self

    def option(self, option: str) -> "ExternalInterviewAssessmentDimensionBuilder":
        self._external_interview_assessment_dimension.option = option
        return self

    def options(self, options: List[str]) -> "ExternalInterviewAssessmentDimensionBuilder":
        self._external_interview_assessment_dimension.options = options
        return self

    def content(self, content: str) -> "ExternalInterviewAssessmentDimensionBuilder":
        self._external_interview_assessment_dimension.content = content
        return self

    def assessment_type(self, assessment_type: int) -> "ExternalInterviewAssessmentDimensionBuilder":
        self._external_interview_assessment_dimension.assessment_type = assessment_type
        return self

    def title(self, title: str) -> "ExternalInterviewAssessmentDimensionBuilder":
        self._external_interview_assessment_dimension.title = title
        return self

    def description(self, description: str) -> "ExternalInterviewAssessmentDimensionBuilder":
        self._external_interview_assessment_dimension.description = description
        return self

    def build(self) -> "ExternalInterviewAssessmentDimension":
        return self._external_interview_assessment_dimension