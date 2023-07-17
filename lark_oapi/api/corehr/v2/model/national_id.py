# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .custom_field_data import CustomFieldData


class NationalId(object):
    _types = {
        "national_id_type_id": str,
        "national_id_number": str,
        "issue_date": str,
        "expiration_date": str,
        "country_region_id": str,
        "issued_by": str,
        "custom_fields": List[CustomFieldData],
    }

    def __init__(self, d):
        self.national_id_type_id: Optional[str] = None
        self.national_id_number: Optional[str] = None
        self.issue_date: Optional[str] = None
        self.expiration_date: Optional[str] = None
        self.country_region_id: Optional[str] = None
        self.issued_by: Optional[str] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NationalIdBuilder":
        return NationalIdBuilder()


class NationalIdBuilder(object):
    def __init__(self, national_id: NationalId = NationalId({})) -> None:
        self._national_id: NationalId = national_id

    def national_id_type_id(self, national_id_type_id: str) -> "NationalIdBuilder":
        self._national_id.national_id_type_id = national_id_type_id
        return self

    def national_id_number(self, national_id_number: str) -> "NationalIdBuilder":
        self._national_id.national_id_number = national_id_number
        return self

    def issue_date(self, issue_date: str) -> "NationalIdBuilder":
        self._national_id.issue_date = issue_date
        return self

    def expiration_date(self, expiration_date: str) -> "NationalIdBuilder":
        self._national_id.expiration_date = expiration_date
        return self

    def country_region_id(self, country_region_id: str) -> "NationalIdBuilder":
        self._national_id.country_region_id = country_region_id
        return self

    def issued_by(self, issued_by: str) -> "NationalIdBuilder":
        self._national_id.issued_by = issued_by
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "NationalIdBuilder":
        self._national_id.custom_fields = custom_fields
        return self

    def build(self) -> "NationalId":
        return self._national_id
