# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class OfferApplyFormFormulaExtraMapInfo(object):
    _types = {
        "key": str,
        "value": I18n,
    }

    def __init__(self, d):
        self.key: Optional[str] = None
        self.value: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferApplyFormFormulaExtraMapInfoBuilder":
        return OfferApplyFormFormulaExtraMapInfoBuilder()


class OfferApplyFormFormulaExtraMapInfoBuilder(object):
    def __init__(self,
                 offer_apply_form_formula_extra_map_info: OfferApplyFormFormulaExtraMapInfo = OfferApplyFormFormulaExtraMapInfo(
                     {})) -> None:
        self._offer_apply_form_formula_extra_map_info: OfferApplyFormFormulaExtraMapInfo = offer_apply_form_formula_extra_map_info

    def key(self, key: str) -> "OfferApplyFormFormulaExtraMapInfoBuilder":
        self._offer_apply_form_formula_extra_map_info.key = key
        return self

    def value(self, value: I18n) -> "OfferApplyFormFormulaExtraMapInfoBuilder":
        self._offer_apply_form_formula_extra_map_info.value = value
        return self

    def build(self) -> "OfferApplyFormFormulaExtraMapInfo":
        return self._offer_apply_form_formula_extra_map_info
