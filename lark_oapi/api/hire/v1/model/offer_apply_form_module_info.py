# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .offer_apply_form_object_info import OfferApplyFormObjectInfo


class OfferApplyFormModuleInfo(object):
    _types = {
        "id": str,
        "name": I18n,
        "is_customized": bool,
        "active_status": int,
        "hint": I18n,
        "object_list": List[OfferApplyFormObjectInfo],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.is_customized: Optional[bool] = None
        self.active_status: Optional[int] = None
        self.hint: Optional[I18n] = None
        self.object_list: Optional[List[OfferApplyFormObjectInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplyFormModuleInfoBuilder":
        return OfferApplyFormModuleInfoBuilder()


class OfferApplyFormModuleInfoBuilder(object):
    def __init__(self, offer_apply_form_module_info: OfferApplyFormModuleInfo = OfferApplyFormModuleInfo({})) -> None:
        self._offer_apply_form_module_info: OfferApplyFormModuleInfo = offer_apply_form_module_info

    def id(self, id: str) -> "OfferApplyFormModuleInfoBuilder":
        self._offer_apply_form_module_info.id = id
        return self

    def name(self, name: I18n) -> "OfferApplyFormModuleInfoBuilder":
        self._offer_apply_form_module_info.name = name
        return self

    def is_customized(self, is_customized: bool) -> "OfferApplyFormModuleInfoBuilder":
        self._offer_apply_form_module_info.is_customized = is_customized
        return self

    def active_status(self, active_status: int) -> "OfferApplyFormModuleInfoBuilder":
        self._offer_apply_form_module_info.active_status = active_status
        return self

    def hint(self, hint: I18n) -> "OfferApplyFormModuleInfoBuilder":
        self._offer_apply_form_module_info.hint = hint
        return self

    def object_list(self, object_list: List[OfferApplyFormObjectInfo]) -> "OfferApplyFormModuleInfoBuilder":
        self._offer_apply_form_module_info.object_list = object_list
        return self

    def build(self) -> "OfferApplyFormModuleInfo":
        return self._offer_apply_form_module_info
