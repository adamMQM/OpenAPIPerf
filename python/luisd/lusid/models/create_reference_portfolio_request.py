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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from lusid.models.model_property import ModelProperty

class CreateReferencePortfolioRequest(BaseModel):
    """
    CreateReferencePortfolioRequest
    """
    display_name: constr(strict=True, min_length=1) = Field(..., alias="displayName", description="The name of the reference portfolio.")
    description: Optional[StrictStr] = Field(None, description="A long form text description of the portfolio.")
    code: StrictStr = Field(..., description="Unique identifier for the portfolio.")
    created: Optional[datetime] = Field(None, description="The original creation date, defaults to today if not specified when creating a portfolio.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="Portfolio properties to add to the portfolio.")
    instrument_scopes: Optional[conlist(StrictStr, max_items=1)] = Field(None, alias="instrumentScopes", description="Instrument Scopes.")
    base_currency: Optional[StrictStr] = Field(None, alias="baseCurrency", description="The base currency of the transaction portfolio in ISO 4217 currency code format.")
    __properties = ["displayName", "description", "code", "created", "properties", "instrumentScopes", "baseCurrency"]

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
    def from_json(cls, json_str: str) -> CreateReferencePortfolioRequest:
        """Create an instance of CreateReferencePortfolioRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if created (nullable) is None
        # and __fields_set__ contains the field
        if self.created is None and "created" in self.__fields_set__:
            _dict['created'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if instrument_scopes (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_scopes is None and "instrument_scopes" in self.__fields_set__:
            _dict['instrumentScopes'] = None

        # set to None if base_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.base_currency is None and "base_currency" in self.__fields_set__:
            _dict['baseCurrency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateReferencePortfolioRequest:
        """Create an instance of CreateReferencePortfolioRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateReferencePortfolioRequest.parse_obj(obj)

        _obj = CreateReferencePortfolioRequest.parse_obj({
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "code": obj.get("code"),
            "created": obj.get("created"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "instrument_scopes": obj.get("instrumentScopes"),
            "base_currency": obj.get("baseCurrency")
        })
        return _obj
