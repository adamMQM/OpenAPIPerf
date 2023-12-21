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


from typing import Any, Dict
from pydantic import BaseModel, Field, constr
from lusid.models.lusid_instrument import LusidInstrument

class AssetLeg(BaseModel):
    """
    The underlying instrument representing one side of the TRS and its pay-receive direction.  # noqa: E501
    """
    asset: LusidInstrument = Field(...)
    pay_receive: constr(strict=True, min_length=1) = Field(..., alias="payReceive", description="Either Pay or Receive stating direction of the asset in the swap.    Supported string (enumeration) values are: [Pay, Receive].")
    __properties = ["asset", "payReceive"]

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
    def from_json(cls, json_str: str) -> AssetLeg:
        """Create an instance of AssetLeg from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetLeg:
        """Create an instance of AssetLeg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AssetLeg.parse_obj(obj)

        _obj = AssetLeg.parse_obj({
            "asset": LusidInstrument.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "pay_receive": obj.get("payReceive")
        })
        return _obj
