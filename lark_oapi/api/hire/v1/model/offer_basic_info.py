# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OfferBasicInfo(object):
    _types = {
        "department_id": str,
        "leader_user_id": str,
        "employment_job_id": str,
        "employee_type_id": str,
        "job_family_id": str,
        "job_level_id": str,
        "probation_month": int,
        "contract_year": int,
        "expected_onboard_date": str,
        "onboard_address_id": str,
        "work_address_id": str,
        "owner_user_id": str,
        "recommended_words": str,
        "job_requirement_id": str,
        "job_process_type_id": int,
        "attachment_id_list": List[str],
        "attachment_description": str,
        "operator_user_id": str,
    }

    def __init__(self, d):
        self.department_id: Optional[str] = None
        self.leader_user_id: Optional[str] = None
        self.employment_job_id: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.job_level_id: Optional[str] = None
        self.probation_month: Optional[int] = None
        self.contract_year: Optional[int] = None
        self.expected_onboard_date: Optional[str] = None
        self.onboard_address_id: Optional[str] = None
        self.work_address_id: Optional[str] = None
        self.owner_user_id: Optional[str] = None
        self.recommended_words: Optional[str] = None
        self.job_requirement_id: Optional[str] = None
        self.job_process_type_id: Optional[int] = None
        self.attachment_id_list: Optional[List[str]] = None
        self.attachment_description: Optional[str] = None
        self.operator_user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferBasicInfoBuilder":
        return OfferBasicInfoBuilder()


class OfferBasicInfoBuilder(object):
    def __init__(self, offer_basic_info: OfferBasicInfo = OfferBasicInfo({})) -> None:
        self._offer_basic_info: OfferBasicInfo = offer_basic_info

    def department_id(self, department_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.department_id = department_id
        return self

    def leader_user_id(self, leader_user_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.leader_user_id = leader_user_id
        return self

    def employment_job_id(self, employment_job_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.employment_job_id = employment_job_id
        return self

    def employee_type_id(self, employee_type_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.employee_type_id = employee_type_id
        return self

    def job_family_id(self, job_family_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.job_family_id = job_family_id
        return self

    def job_level_id(self, job_level_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.job_level_id = job_level_id
        return self

    def probation_month(self, probation_month: int) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.probation_month = probation_month
        return self

    def contract_year(self, contract_year: int) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.contract_year = contract_year
        return self

    def expected_onboard_date(self, expected_onboard_date: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.expected_onboard_date = expected_onboard_date
        return self

    def onboard_address_id(self, onboard_address_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.onboard_address_id = onboard_address_id
        return self

    def work_address_id(self, work_address_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.work_address_id = work_address_id
        return self

    def owner_user_id(self, owner_user_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.owner_user_id = owner_user_id
        return self

    def recommended_words(self, recommended_words: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.recommended_words = recommended_words
        return self

    def job_requirement_id(self, job_requirement_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.job_requirement_id = job_requirement_id
        return self

    def job_process_type_id(self, job_process_type_id: int) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.job_process_type_id = job_process_type_id
        return self

    def attachment_id_list(self, attachment_id_list: List[str]) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.attachment_id_list = attachment_id_list
        return self

    def attachment_description(self, attachment_description: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.attachment_description = attachment_description
        return self

    def operator_user_id(self, operator_user_id: str) -> "OfferBasicInfoBuilder":
        self._offer_basic_info.operator_user_id = operator_user_id
        return self

    def build(self) -> "OfferBasicInfo":
        return self._offer_basic_info
