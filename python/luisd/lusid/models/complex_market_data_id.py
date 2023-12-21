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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr

class ComplexMarketDataId(BaseModel):
    """
    An identifier that uniquely describes an item of complex market data such as an interest rate curve or volatility surface.  # noqa: E501
    """
    provider: constr(strict=True, max_length=32, min_length=0) = Field(..., description="The platform or vendor that provided the complex market data, e.g. 'DataScope', 'LUSID', etc.")
    price_source: Optional[constr(strict=True, max_length=256, min_length=0)] = Field(None, alias="priceSource", description="The source or originator of the complex market data, e.g. a bank or financial institution.")
    lineage: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="This is obsolete. It is not used, it will not be stored, and has no effects.  If you wish to attach a Lineage to your ComplexMarketData,  you should provide it in the optional Lineage field in the ComplexMarketData class.")
    effective_at: Optional[StrictStr] = Field(None, alias="effectiveAt", description="The effectiveAt or cut label that this item of complex market data is/was updated/inserted with.")
    market_asset: constr(strict=True, max_length=256, min_length=0) = Field(..., alias="marketAsset", description="The name of the market entity that the document represents")
    __properties = ["provider", "priceSource", "lineage", "effectiveAt", "marketAsset"]

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
    def from_json(cls, json_str: str) -> ComplexMarketDataId:
        """Create an instance of ComplexMarketDataId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if price_source (nullable) is None
        # and __fields_set__ contains the field
        if self.price_source is None and "price_source" in self.__fields_set__:
            _dict['priceSource'] = None

        # set to None if lineage (nullable) is None
        # and __fields_set__ contains the field
        if self.lineage is None and "lineage" in self.__fields_set__:
            _dict['lineage'] = None

        # set to None if effective_at (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_at is None and "effective_at" in self.__fields_set__:
            _dict['effectiveAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplexMarketDataId:
        """Create an instance of ComplexMarketDataId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplexMarketDataId.parse_obj(obj)

        _obj = ComplexMarketDataId.parse_obj({
            "provider": obj.get("provider"),
            "price_source": obj.get("priceSource"),
            "lineage": obj.get("lineage"),
            "effective_at": obj.get("effectiveAt"),
            "market_asset": obj.get("marketAsset")
        })
        return _obj
