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
from lusid.models.link import Link

class InstrumentModels(BaseModel):
    """
    Supported pricing models for an instrument.  # noqa: E501
    """
    instrument_id: Optional[StrictStr] = Field(None, alias="instrumentId", description="The unique LUSID Instrument Identifier (LUID) of the instrument.")
    supported_models: Optional[conlist(StrictStr)] = Field(None, alias="supportedModels", description="The pricing models supported by the instrument e.g. 'Discounting'.")
    links: Optional[conlist(Link)] = Field(None, description="Collection of links.")
    __properties = ["instrumentId", "supportedModels", "links"]

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
    def from_json(cls, json_str: str) -> InstrumentModels:
        """Create an instance of InstrumentModels from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if instrument_id (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_id is None and "instrument_id" in self.__fields_set__:
            _dict['instrumentId'] = None

        # set to None if supported_models (nullable) is None
        # and __fields_set__ contains the field
        if self.supported_models is None and "supported_models" in self.__fields_set__:
            _dict['supportedModels'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstrumentModels:
        """Create an instance of InstrumentModels from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstrumentModels.parse_obj(obj)

        _obj = InstrumentModels.parse_obj({
            "instrument_id": obj.get("instrumentId"),
            "supported_models": obj.get("supportedModels"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
