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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator
from lusid.models.resource_id import ResourceId

class AggregatedReturnsDispersionRequest(BaseModel):
    """
    The request used in the AggregatedReturnsDispersionMetric.  # noqa: E501
    """
    to_effective_at: Optional[constr(strict=True, max_length=256, min_length=0)] = Field(None, alias="toEffectiveAt", description="The end date for when the you want the dispersion to be calculated.")
    years_count: Optional[StrictInt] = Field(None, alias="yearsCount", description="For how many years to calculate the dispersion. Default to 10.")
    return_ids: Optional[conlist(ResourceId)] = Field(None, alias="returnIds", description="The Scope and code of the returns.")
    recipe_id: Optional[ResourceId] = Field(None, alias="recipeId")
    composite_method: Optional[StrictStr] = Field(None, alias="compositeMethod", description="The method used to calculate the Portfolio performance: Equal/Asset.")
    alternative_inception_date: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, alias="alternativeInceptionDate", description="Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.")
    __properties = ["toEffectiveAt", "yearsCount", "returnIds", "recipeId", "compositeMethod", "alternativeInceptionDate"]

    @validator('to_effective_at')
    def to_effective_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_\+:\.]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_\+:\.]+$/")
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
    def from_json(cls, json_str: str) -> AggregatedReturnsDispersionRequest:
        """Create an instance of AggregatedReturnsDispersionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in return_ids (list)
        _items = []
        if self.return_ids:
            for _item in self.return_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['returnIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of recipe_id
        if self.recipe_id:
            _dict['recipeId'] = self.recipe_id.to_dict()
        # set to None if to_effective_at (nullable) is None
        # and __fields_set__ contains the field
        if self.to_effective_at is None and "to_effective_at" in self.__fields_set__:
            _dict['toEffectiveAt'] = None

        # set to None if return_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.return_ids is None and "return_ids" in self.__fields_set__:
            _dict['returnIds'] = None

        # set to None if composite_method (nullable) is None
        # and __fields_set__ contains the field
        if self.composite_method is None and "composite_method" in self.__fields_set__:
            _dict['compositeMethod'] = None

        # set to None if alternative_inception_date (nullable) is None
        # and __fields_set__ contains the field
        if self.alternative_inception_date is None and "alternative_inception_date" in self.__fields_set__:
            _dict['alternativeInceptionDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AggregatedReturnsDispersionRequest:
        """Create an instance of AggregatedReturnsDispersionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AggregatedReturnsDispersionRequest.parse_obj(obj)

        _obj = AggregatedReturnsDispersionRequest.parse_obj({
            "to_effective_at": obj.get("toEffectiveAt"),
            "years_count": obj.get("yearsCount"),
            "return_ids": [ResourceId.from_dict(_item) for _item in obj.get("returnIds")] if obj.get("returnIds") is not None else None,
            "recipe_id": ResourceId.from_dict(obj.get("recipeId")) if obj.get("recipeId") is not None else None,
            "composite_method": obj.get("compositeMethod"),
            "alternative_inception_date": obj.get("alternativeInceptionDate")
        })
        return _obj
