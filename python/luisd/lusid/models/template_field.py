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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, StrictStr, conlist, constr

class TemplateField(BaseModel):
    """
    TemplateField
    """
    field_name: constr(strict=True, min_length=1) = Field(..., alias="fieldName")
    specificity: constr(strict=True, min_length=1) = Field(...)
    description: constr(strict=True, min_length=1) = Field(...)
    type: constr(strict=True, min_length=1) = Field(...)
    usage: conlist(StrictStr) = Field(...)
    __properties = ["fieldName", "specificity", "description", "type", "usage"]

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
    def from_json(cls, json_str: str) -> TemplateField:
        """Create an instance of TemplateField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TemplateField:
        """Create an instance of TemplateField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TemplateField.parse_obj(obj)

        _obj = TemplateField.parse_obj({
            "field_name": obj.get("fieldName"),
            "specificity": obj.get("specificity"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "usage": obj.get("usage")
        })
        return _obj
