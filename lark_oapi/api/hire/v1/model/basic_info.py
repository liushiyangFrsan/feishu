# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .identification import Identification


class BasicInfo(object):
    _types = {
        "name": str,
        "mobile": str,
        "mobile_country_code": str,
        "email": str,
        "birthday": int,
        "confidentiality": int,
        "creator_account_type": int,
        "creator_id": str,
        "current_city_code": str,
        "gender": int,
        "hometown_city_code": str,
        "identification": Identification,
        "init_source_id": str,
        "nationality_id": str,
        "resume_attachment_id": str,
        "self_evaluation": str,
        "start_work_time": int,
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        self.mobile: Optional[str] = None
        self.mobile_country_code: Optional[str] = None
        self.email: Optional[str] = None
        self.birthday: Optional[int] = None
        self.confidentiality: Optional[int] = None
        self.creator_account_type: Optional[int] = None
        self.creator_id: Optional[str] = None
        self.current_city_code: Optional[str] = None
        self.gender: Optional[int] = None
        self.hometown_city_code: Optional[str] = None
        self.identification: Optional[Identification] = None
        self.init_source_id: Optional[str] = None
        self.nationality_id: Optional[str] = None
        self.resume_attachment_id: Optional[str] = None
        self.self_evaluation: Optional[str] = None
        self.start_work_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BasicInfoBuilder":
        return BasicInfoBuilder()


class BasicInfoBuilder(object):
    def __init__(self, basic_info: BasicInfo = BasicInfo({})) -> None:
        self._basic_info: BasicInfo = basic_info

    def name(self, name: str) -> "BasicInfoBuilder":
        self._basic_info.name = name
        return self

    def mobile(self, mobile: str) -> "BasicInfoBuilder":
        self._basic_info.mobile = mobile
        return self

    def mobile_country_code(self, mobile_country_code: str) -> "BasicInfoBuilder":
        self._basic_info.mobile_country_code = mobile_country_code
        return self

    def email(self, email: str) -> "BasicInfoBuilder":
        self._basic_info.email = email
        return self

    def birthday(self, birthday: int) -> "BasicInfoBuilder":
        self._basic_info.birthday = birthday
        return self

    def confidentiality(self, confidentiality: int) -> "BasicInfoBuilder":
        self._basic_info.confidentiality = confidentiality
        return self

    def creator_account_type(self, creator_account_type: int) -> "BasicInfoBuilder":
        self._basic_info.creator_account_type = creator_account_type
        return self

    def creator_id(self, creator_id: str) -> "BasicInfoBuilder":
        self._basic_info.creator_id = creator_id
        return self

    def current_city_code(self, current_city_code: str) -> "BasicInfoBuilder":
        self._basic_info.current_city_code = current_city_code
        return self

    def gender(self, gender: int) -> "BasicInfoBuilder":
        self._basic_info.gender = gender
        return self

    def hometown_city_code(self, hometown_city_code: str) -> "BasicInfoBuilder":
        self._basic_info.hometown_city_code = hometown_city_code
        return self

    def identification(self, identification: Identification) -> "BasicInfoBuilder":
        self._basic_info.identification = identification
        return self

    def init_source_id(self, init_source_id: str) -> "BasicInfoBuilder":
        self._basic_info.init_source_id = init_source_id
        return self

    def nationality_id(self, nationality_id: str) -> "BasicInfoBuilder":
        self._basic_info.nationality_id = nationality_id
        return self

    def resume_attachment_id(self, resume_attachment_id: str) -> "BasicInfoBuilder":
        self._basic_info.resume_attachment_id = resume_attachment_id
        return self

    def self_evaluation(self, self_evaluation: str) -> "BasicInfoBuilder":
        self._basic_info.self_evaluation = self_evaluation
        return self

    def start_work_time(self, start_work_time: int) -> "BasicInfoBuilder":
        self._basic_info.start_work_time = start_work_time
        return self

    def build(self) -> "BasicInfo":
        return self._basic_info
