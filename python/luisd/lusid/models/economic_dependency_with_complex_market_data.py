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


from typing import Any, Dict
from pydantic import BaseModel, Field
from lusid.models.complex_market_data import ComplexMarketData
from lusid.models.economic_dependency import EconomicDependency

class EconomicDependencyWithComplexMarketData(BaseModel):
    """
    Container class pairing economic dependency and complex market data (i.e. discounting curves, etc.)  # noqa: E501
    """
    economic_dependency: EconomicDependency = Field(..., alias="economicDependency")
    complex_market_data: ComplexMarketData = Field(..., alias="complexMarketData")
    __properties = ["economicDependency", "complexMarketData"]

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
    def from_json(cls, json_str: str) -> EconomicDependencyWithComplexMarketData:
        """Create an instance of EconomicDependencyWithComplexMarketData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of economic_dependency
        if self.economic_dependency:
            _dict['economicDependency'] = self.economic_dependency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of complex_market_data
        if self.complex_market_data:
            _dict['complexMarketData'] = self.complex_market_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EconomicDependencyWithComplexMarketData:
        """Create an instance of EconomicDependencyWithComplexMarketData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EconomicDependencyWithComplexMarketData.parse_obj(obj)

        _obj = EconomicDependencyWithComplexMarketData.parse_obj({
            "economic_dependency": EconomicDependency.from_dict(obj.get("economicDependency")) if obj.get("economicDependency") is not None else None,
            "complex_market_data": ComplexMarketData.from_dict(obj.get("complexMarketData")) if obj.get("complexMarketData") is not None else None
        })
        return _obj
