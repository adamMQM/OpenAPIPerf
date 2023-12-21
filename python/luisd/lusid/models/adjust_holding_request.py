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
from pydantic import BaseModel, Field, StrictStr, conlist
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.target_tax_lot_request import TargetTaxLotRequest

class AdjustHoldingRequest(BaseModel):
    """
    This request specifies target holdings. i.e. holding data that the  system should match. When processed by the movement  engine, it will create 'true-up' adjustments on the fly.  # noqa: E501
    """
    instrument_identifiers: Dict[str, StrictStr] = Field(..., alias="instrumentIdentifiers", description="A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.")
    sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = Field(None, alias="subHoldingKeys", description="Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the 'Transaction' domain.")
    properties: Optional[Dict[str, PerpetualProperty]] = Field(None, description="Set of unique holding properties and associated values to store with the target holding. Each property must be from the 'Holding' domain.")
    tax_lots: conlist(TargetTaxLotRequest) = Field(..., alias="taxLots", description="The tax-lots that together make up the target holding.")
    currency: Optional[StrictStr] = Field(None, description="The Holding currency. This needs to be equal with the one on the TaxLot -> cost if one is specified")
    __properties = ["instrumentIdentifiers", "subHoldingKeys", "properties", "taxLots", "currency"]

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
    def from_json(cls, json_str: str) -> AdjustHoldingRequest:
        """Create an instance of AdjustHoldingRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in sub_holding_keys (dict)
        _field_dict = {}
        if self.sub_holding_keys:
            for _key in self.sub_holding_keys:
                if self.sub_holding_keys[_key]:
                    _field_dict[_key] = self.sub_holding_keys[_key].to_dict()
            _dict['subHoldingKeys'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in tax_lots (list)
        _items = []
        if self.tax_lots:
            for _item in self.tax_lots:
                if _item:
                    _items.append(_item.to_dict())
            _dict['taxLots'] = _items
        # set to None if sub_holding_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.sub_holding_keys is None and "sub_holding_keys" in self.__fields_set__:
            _dict['subHoldingKeys'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdjustHoldingRequest:
        """Create an instance of AdjustHoldingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdjustHoldingRequest.parse_obj(obj)

        _obj = AdjustHoldingRequest.parse_obj({
            "instrument_identifiers": obj.get("instrumentIdentifiers"),
            "sub_holding_keys": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("subHoldingKeys").items()
            )
            if obj.get("subHoldingKeys") is not None
            else None,
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "tax_lots": [TargetTaxLotRequest.from_dict(_item) for _item in obj.get("taxLots")] if obj.get("taxLots") is not None else None,
            "currency": obj.get("currency")
        })
        return _obj
