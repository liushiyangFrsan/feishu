# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_setting import UserSetting


class ModifyUserSettingResponseBody(object):
    _types = {
        "user_setting": UserSetting,
    }

    def __init__(self, d):
        self.user_setting: Optional[UserSetting] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ModifyUserSettingResponseBodyBuilder":
        return ModifyUserSettingResponseBodyBuilder()


class ModifyUserSettingResponseBodyBuilder(object):
    def __init__(self, modify_user_setting_response_body: ModifyUserSettingResponseBody = ModifyUserSettingResponseBody(
        {})) -> None:
        self._modify_user_setting_response_body: ModifyUserSettingResponseBody = modify_user_setting_response_body

    def user_setting(self, user_setting: UserSetting) -> "ModifyUserSettingResponseBodyBuilder":
        self._modify_user_setting_response_body.user_setting = user_setting
        return self

    def build(self) -> "ModifyUserSettingResponseBody":
        return self._modify_user_setting_response_body
