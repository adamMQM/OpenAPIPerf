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
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class UnitsRatio(BaseModel):
    """
    todo: what even is this  # noqa: E501
    """
    input: Union[StrictFloat, StrictInt] = Field(..., description="Input amount.  Denominator of the Ratio")
    output: Union[StrictFloat, StrictInt] = Field(..., description="Output amount. Numerator of the Ratio")
    __properties = ["input", "output"]

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
    def from_json(cls, json_str: str) -> UnitsRatio:
        """Create an instance of UnitsRatio from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UnitsRatio:
        """Create an instance of UnitsRatio from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UnitsRatio.parse_obj(obj)

        _obj = UnitsRatio.parse_obj({
            "input": obj.get("input"),
            "output": obj.get("output")
        })
        return _obj
