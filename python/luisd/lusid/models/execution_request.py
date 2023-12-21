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
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr
from lusid.models.currency_and_amount import CurrencyAndAmount
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.resource_id import ResourceId

class ExecutionRequest(BaseModel):
    """
    A request to create or update a Execution.  # noqa: E501
    """
    id: ResourceId = Field(...)
    placement_id: ResourceId = Field(..., alias="placementId")
    properties: Optional[Dict[str, PerpetualProperty]] = Field(None, description="Client-defined properties associated with this execution.")
    instrument_identifiers: Dict[str, StrictStr] = Field(..., alias="instrumentIdentifiers", description="The instrument ordered.")
    quantity: Union[StrictFloat, StrictInt] = Field(..., description="The quantity of given instrument ordered.")
    state: constr(strict=True, min_length=1) = Field(..., description="The state of this execution (typically a FIX state; Open, Filled, etc).")
    side: constr(strict=True, min_length=1) = Field(..., description="The side (Buy, Sell, ...) of this execution.")
    type: constr(strict=True, min_length=1) = Field(..., description="The type of this execution (Market, Limit, etc).")
    created_date: datetime = Field(..., alias="createdDate", description="The active date of this execution.")
    settlement_date: Optional[datetime] = Field(None, alias="settlementDate", description="The (optional) settlement date for this execution")
    price: CurrencyAndAmount = Field(...)
    settlement_currency: StrictStr = Field(..., alias="settlementCurrency", description="The execution's settlement currency.")
    settlement_currency_fx_rate: Union[StrictFloat, StrictInt] = Field(..., alias="settlementCurrencyFxRate", description="The exectuion's settlement currency rate.")
    counterparty: constr(strict=True, min_length=1) = Field(..., description="The market entity this placement is placed with.")
    average_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="averagePrice", description="The average price of all executions for a given placement at the time of upsert")
    __properties = ["id", "placementId", "properties", "instrumentIdentifiers", "quantity", "state", "side", "type", "createdDate", "settlementDate", "price", "settlementCurrency", "settlementCurrencyFxRate", "counterparty", "averagePrice"]

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
    def from_json(cls, json_str: str) -> ExecutionRequest:
        """Create an instance of ExecutionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of placement_id
        if self.placement_id:
            _dict['placementId'] = self.placement_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if settlement_date (nullable) is None
        # and __fields_set__ contains the field
        if self.settlement_date is None and "settlement_date" in self.__fields_set__:
            _dict['settlementDate'] = None

        # set to None if average_price (nullable) is None
        # and __fields_set__ contains the field
        if self.average_price is None and "average_price" in self.__fields_set__:
            _dict['averagePrice'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExecutionRequest:
        """Create an instance of ExecutionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExecutionRequest.parse_obj(obj)

        _obj = ExecutionRequest.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "placement_id": ResourceId.from_dict(obj.get("placementId")) if obj.get("placementId") is not None else None,
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "instrument_identifiers": obj.get("instrumentIdentifiers"),
            "quantity": obj.get("quantity"),
            "state": obj.get("state"),
            "side": obj.get("side"),
            "type": obj.get("type"),
            "created_date": obj.get("createdDate"),
            "settlement_date": obj.get("settlementDate"),
            "price": CurrencyAndAmount.from_dict(obj.get("price")) if obj.get("price") is not None else None,
            "settlement_currency": obj.get("settlementCurrency"),
            "settlement_currency_fx_rate": obj.get("settlementCurrencyFxRate"),
            "counterparty": obj.get("counterparty"),
            "average_price": obj.get("averagePrice")
        })
        return _obj
