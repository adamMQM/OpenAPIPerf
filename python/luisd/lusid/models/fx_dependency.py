# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict
from pydantic import Field, StrictStr, validator
from lusid.models.economic_dependency import EconomicDependency

class FxDependency(EconomicDependency):
    """
    For indicating a dependency on an fx rate.  For example domestic-foreign for USD-JPY  means that 1 unit (dollar) of domestic currency will buy you \"X\" units of foreign (Yen) currency; currently somewhere around 100.  This is equivalently denoted as USDJPY and USD/JPY                On the assumption that you wish to convert an amount in the domestic currency to the foreign, you would want the (dom,fgn) dependency; domfgn currency pair.  On the assumption that you wish to convert an amount in the foreign currency to the domestic, you would want the (fgn,dom) dependency; fgndom currency pair.                NB: There alternate descriptions for currency pairs that seem to vary between different banks and sectors of the industry, e.g. base and contract                In pricing we are taking the convention that we will convert from FGN to DOM by DIVIDING through by the DOMFGN spot rate.  # noqa: E501
    """
    domestic_currency: StrictStr = Field(..., alias="domesticCurrency", description="DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency.")
    foreign_currency: StrictStr = Field(..., alias="foreignCurrency", description="ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency.")
    var_date: datetime = Field(..., alias="date", description="The effectiveAt of the fx rate.")
    dependency_type: StrictStr = Field(..., alias="dependencyType", description="The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency")
    additional_properties: Dict[str, Any] = {}
    __properties = ["dependencyType", "domesticCurrency", "foreignCurrency", "date"]

    @validator('dependency_type')
    def dependency_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('OpaqueDependency', 'CashDependency', 'DiscountingDependency', 'EquityCurveDependency', 'EquityVolDependency', 'FxDependency', 'FxForwardsDependency', 'FxVolDependency', 'IndexProjectionDependency', 'IrVolDependency', 'QuoteDependency', 'Vendor', 'CalendarDependency', 'InflationFixingDependency'):
            raise ValueError("must be one of enum values ('OpaqueDependency', 'CashDependency', 'DiscountingDependency', 'EquityCurveDependency', 'EquityVolDependency', 'FxDependency', 'FxForwardsDependency', 'FxVolDependency', 'IndexProjectionDependency', 'IrVolDependency', 'QuoteDependency', 'Vendor', 'CalendarDependency', 'InflationFixingDependency')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FxDependency:
        """Create an instance of FxDependency from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FxDependency:
        """Create an instance of FxDependency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FxDependency.parse_obj(obj)

        _obj = FxDependency.parse_obj({
            "dependency_type": obj.get("dependencyType"),
            "domestic_currency": obj.get("domesticCurrency"),
            "foreign_currency": obj.get("foreignCurrency"),
            "var_date": obj.get("date")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
