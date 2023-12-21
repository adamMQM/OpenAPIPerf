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


from typing import Any, Dict, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, constr

class CalculationInfo(BaseModel):
    """
    CalculationInfo
    """
    calculation_method: constr(strict=True, min_length=1) = Field(..., alias="calculationMethod", description="Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc.")
    multiplier: constr(strict=True, min_length=1) = Field(..., description="Field by which to multiply the numerical amount. Eg: Quantity, Value")
    calculation_amount: Union[StrictFloat, StrictInt] = Field(..., alias="calculationAmount", description="Numerical fee amount")
    __properties = ["calculationMethod", "multiplier", "calculationAmount"]

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
    def from_json(cls, json_str: str) -> CalculationInfo:
        """Create an instance of CalculationInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CalculationInfo:
        """Create an instance of CalculationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CalculationInfo.parse_obj(obj)

        _obj = CalculationInfo.parse_obj({
            "calculation_method": obj.get("calculationMethod"),
            "multiplier": obj.get("multiplier"),
            "calculation_amount": obj.get("calculationAmount")
        })
        return _obj
