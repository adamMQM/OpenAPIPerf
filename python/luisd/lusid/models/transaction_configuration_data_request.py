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
from pydantic import BaseModel, Field, conlist
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.transaction_configuration_movement_data_request import TransactionConfigurationMovementDataRequest
from lusid.models.transaction_configuration_type_alias import TransactionConfigurationTypeAlias

class TransactionConfigurationDataRequest(BaseModel):
    """
    TransactionConfigurationDataRequest
    """
    aliases: conlist(TransactionConfigurationTypeAlias) = Field(..., description="List of transaction codes that map to this specific transaction model")
    movements: conlist(TransactionConfigurationMovementDataRequest) = Field(..., description="Movement data for the transaction code")
    properties: Optional[Dict[str, PerpetualProperty]] = Field(None, description="Properties attached to the underlying holding.")
    __properties = ["aliases", "movements", "properties"]

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
    def from_json(cls, json_str: str) -> TransactionConfigurationDataRequest:
        """Create an instance of TransactionConfigurationDataRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in aliases (list)
        _items = []
        if self.aliases:
            for _item in self.aliases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['aliases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in movements (list)
        _items = []
        if self.movements:
            for _item in self.movements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['movements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionConfigurationDataRequest:
        """Create an instance of TransactionConfigurationDataRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionConfigurationDataRequest.parse_obj(obj)

        _obj = TransactionConfigurationDataRequest.parse_obj({
            "aliases": [TransactionConfigurationTypeAlias.from_dict(_item) for _item in obj.get("aliases")] if obj.get("aliases") is not None else None,
            "movements": [TransactionConfigurationMovementDataRequest.from_dict(_item) for _item in obj.get("movements")] if obj.get("movements") is not None else None,
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None
        })
        return _obj
