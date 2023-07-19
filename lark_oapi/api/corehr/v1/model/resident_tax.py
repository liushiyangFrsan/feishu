# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .address import Address
from .enum import Enum
from .object_field_data import ObjectFieldData


class ResidentTax(object):
    _types = {
        "id": str,
        "year_resident_tax": str,
        "tax_address": Address,
        "tax_country_region_id": str,
        "resident_status": Enum,
        "resident_status_specification": str,
        "custom_fields": List[ObjectFieldData],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.year_resident_tax: Optional[str] = None
        self.tax_address: Optional[Address] = None
        self.tax_country_region_id: Optional[str] = None
        self.resident_status: Optional[Enum] = None
        self.resident_status_specification: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ResidentTaxBuilder":
        return ResidentTaxBuilder()


class ResidentTaxBuilder(object):
    def __init__(self, resident_tax: ResidentTax = ResidentTax({})) -> None:
        self._resident_tax: ResidentTax = resident_tax

    def id(self, id: str) -> "ResidentTaxBuilder":
        self._resident_tax.id = id
        return self

    def year_resident_tax(self, year_resident_tax: str) -> "ResidentTaxBuilder":
        self._resident_tax.year_resident_tax = year_resident_tax
        return self

    def tax_address(self, tax_address: Address) -> "ResidentTaxBuilder":
        self._resident_tax.tax_address = tax_address
        return self

    def tax_country_region_id(self, tax_country_region_id: str) -> "ResidentTaxBuilder":
        self._resident_tax.tax_country_region_id = tax_country_region_id
        return self

    def resident_status(self, resident_status: Enum) -> "ResidentTaxBuilder":
        self._resident_tax.resident_status = resident_status
        return self

    def resident_status_specification(self, resident_status_specification: str) -> "ResidentTaxBuilder":
        self._resident_tax.resident_status_specification = resident_status_specification
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "ResidentTaxBuilder":
        self._resident_tax.custom_fields = custom_fields
        return self

    def build(self) -> "ResidentTax":
        return self._resident_tax