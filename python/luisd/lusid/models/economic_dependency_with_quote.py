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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from lusid.models.economic_dependency import EconomicDependency
from lusid.models.metric_value import MetricValue

class EconomicDependencyWithQuote(BaseModel):
    """
    Container class pairing economic dependencies and quote data  # noqa: E501
    """
    economic_dependency: EconomicDependency = Field(..., alias="economicDependency")
    metric_value: MetricValue = Field(..., alias="metricValue")
    scale_factor: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="scaleFactor", description="Scale factor for the quote - this can be null, in which case we default to 1.")
    __properties = ["economicDependency", "metricValue", "scaleFactor"]

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
    def from_json(cls, json_str: str) -> EconomicDependencyWithQuote:
        """Create an instance of EconomicDependencyWithQuote from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metric_value
        if self.metric_value:
            _dict['metricValue'] = self.metric_value.to_dict()
        # set to None if scale_factor (nullable) is None
        # and __fields_set__ contains the field
        if self.scale_factor is None and "scale_factor" in self.__fields_set__:
            _dict['scaleFactor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EconomicDependencyWithQuote:
        """Create an instance of EconomicDependencyWithQuote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EconomicDependencyWithQuote.parse_obj(obj)

        _obj = EconomicDependencyWithQuote.parse_obj({
            "economic_dependency": EconomicDependency.from_dict(obj.get("economicDependency")) if obj.get("economicDependency") is not None else None,
            "metric_value": MetricValue.from_dict(obj.get("metricValue")) if obj.get("metricValue") is not None else None,
            "scale_factor": obj.get("scaleFactor")
        })
        return _obj
