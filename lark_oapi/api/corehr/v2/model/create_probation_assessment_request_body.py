# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .assessment_for_create import AssessmentForCreate


class CreateProbationAssessmentRequestBody(object):
    _types = {
        "employment_id": str,
        "assessments": List[AssessmentForCreate],
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.assessments: Optional[List[AssessmentForCreate]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateProbationAssessmentRequestBodyBuilder":
        return CreateProbationAssessmentRequestBodyBuilder()


class CreateProbationAssessmentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_probation_assessment_request_body = CreateProbationAssessmentRequestBody()

    def employment_id(self, employment_id: str) -> "CreateProbationAssessmentRequestBodyBuilder":
        self._create_probation_assessment_request_body.employment_id = employment_id
        return self

    def assessments(self, assessments: List[AssessmentForCreate]) -> "CreateProbationAssessmentRequestBodyBuilder":
        self._create_probation_assessment_request_body.assessments = assessments
        return self

    def build(self) -> "CreateProbationAssessmentRequestBody":
        return self._create_probation_assessment_request_body