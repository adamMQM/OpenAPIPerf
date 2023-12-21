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
from pydantic import BaseModel, Field, StrictStr

class EquityAllOfIdentifiers(BaseModel):
    """
    External market codes and identifiers for the equity, e.g. IBM  # noqa: E501
    """
    lusid_instrument_id: Optional[StrictStr] = Field(None, alias="LusidInstrumentId")
    isin: Optional[StrictStr] = Field(None, alias="Isin")
    sedol: Optional[StrictStr] = Field(None, alias="Sedol")
    cusip: Optional[StrictStr] = Field(None, alias="Cusip")
    client_internal: Optional[StrictStr] = Field(None, alias="ClientInternal")
    figi: Optional[StrictStr] = Field(None, alias="Figi")
    ric: Optional[StrictStr] = Field(None, alias="RIC")
    quote_perm_id: Optional[StrictStr] = Field(None, alias="QuotePermId")
    red_code: Optional[StrictStr] = Field(None, alias="REDCode")
    bbgid: Optional[StrictStr] = Field(None, alias="BBGId")
    ice_code: Optional[StrictStr] = Field(None, alias="ICECode")
    additional_properties: Dict[str, Any] = {}
    __properties = ["LusidInstrumentId", "Isin", "Sedol", "Cusip", "ClientInternal", "Figi", "RIC", "QuotePermId", "REDCode", "BBGId", "ICECode"]

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
    def from_json(cls, json_str: str) -> EquityAllOfIdentifiers:
        """Create an instance of EquityAllOfIdentifiers from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EquityAllOfIdentifiers:
        """Create an instance of EquityAllOfIdentifiers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EquityAllOfIdentifiers.parse_obj(obj)

        _obj = EquityAllOfIdentifiers.parse_obj({
            "lusid_instrument_id": obj.get("LusidInstrumentId"),
            "isin": obj.get("Isin"),
            "sedol": obj.get("Sedol"),
            "cusip": obj.get("Cusip"),
            "client_internal": obj.get("ClientInternal"),
            "figi": obj.get("Figi"),
            "ric": obj.get("RIC"),
            "quote_perm_id": obj.get("QuotePermId"),
            "red_code": obj.get("REDCode"),
            "bbgid": obj.get("BBGId"),
            "ice_code": obj.get("ICECode")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
