# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .profile_setting_custom_field import ProfileSettingCustomField


class ProfileSettingNational(object):
    _types = {
        "country_region": str,
        "national_id_type": str,
        "national_id_number": str,
        "issued_date": str,
        "issued_by": str,
        "expiration_date": str,
        "custom_fields": List[ProfileSettingCustomField],
    }

    def __init__(self, d=None):
        self.country_region: Optional[str] = None
        self.national_id_type: Optional[str] = None
        self.national_id_number: Optional[str] = None
        self.issued_date: Optional[str] = None
        self.issued_by: Optional[str] = None
        self.expiration_date: Optional[str] = None
        self.custom_fields: Optional[List[ProfileSettingCustomField]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingNationalBuilder":
        return ProfileSettingNationalBuilder()


class ProfileSettingNationalBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_national = ProfileSettingNational()

    def country_region(self, country_region: str) -> "ProfileSettingNationalBuilder":
        self._profile_setting_national.country_region = country_region
        return self

    def national_id_type(self, national_id_type: str) -> "ProfileSettingNationalBuilder":
        self._profile_setting_national.national_id_type = national_id_type
        return self

    def national_id_number(self, national_id_number: str) -> "ProfileSettingNationalBuilder":
        self._profile_setting_national.national_id_number = national_id_number
        return self

    def issued_date(self, issued_date: str) -> "ProfileSettingNationalBuilder":
        self._profile_setting_national.issued_date = issued_date
        return self

    def issued_by(self, issued_by: str) -> "ProfileSettingNationalBuilder":
        self._profile_setting_national.issued_by = issued_by
        return self

    def expiration_date(self, expiration_date: str) -> "ProfileSettingNationalBuilder":
        self._profile_setting_national.expiration_date = expiration_date
        return self

    def custom_fields(self, custom_fields: List[ProfileSettingCustomField]) -> "ProfileSettingNationalBuilder":
        self._profile_setting_national.custom_fields = custom_fields
        return self

    def build(self) -> "ProfileSettingNational":
        return self._profile_setting_national