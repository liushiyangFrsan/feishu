# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .boolean_rule_condition import BooleanRuleCondition


class ConditionalFormatRule(object):
    _types = {
        "boolean_rule": BooleanRuleCondition,
        "type": str,
    }

    def __init__(self, d):
        self.boolean_rule: Optional[BooleanRuleCondition] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ConditionalFormatRuleBuilder":
        return ConditionalFormatRuleBuilder()


class ConditionalFormatRuleBuilder(object):
    def __init__(self, conditional_format_rule: ConditionalFormatRule = ConditionalFormatRule({})) -> None:
        self._conditional_format_rule: ConditionalFormatRule = conditional_format_rule

    def boolean_rule(self, boolean_rule: BooleanRuleCondition) -> "ConditionalFormatRuleBuilder":
        self._conditional_format_rule.boolean_rule = boolean_rule
        return self

    def type(self, type: str) -> "ConditionalFormatRuleBuilder":
        self._conditional_format_rule.type = type
        return self

    def build(self) -> "ConditionalFormatRule":
        return self._conditional_format_rule
