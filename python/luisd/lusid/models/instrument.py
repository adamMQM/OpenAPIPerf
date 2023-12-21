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
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from lusid.models.link import Link
from lusid.models.lusid_instrument import LusidInstrument
from lusid.models.model_property import ModelProperty
from lusid.models.relationship import Relationship
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class Instrument(BaseModel):
    """
    A list of instruments.  # noqa: E501
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    scope: Optional[StrictStr] = Field(None, description="The scope in which the instrument lies.")
    lusid_instrument_id: constr(strict=True, min_length=1) = Field(..., alias="lusidInstrumentId", description="The unique LUSID Instrument Identifier (LUID) of the instrument.")
    version: Version = Field(...)
    name: constr(strict=True, min_length=1) = Field(..., description="The name of the instrument.")
    identifiers: Dict[str, StrictStr] = Field(..., description="The set of identifiers that can be used to identify the instrument.")
    properties: Optional[conlist(ModelProperty)] = Field(None, description="The requested instrument properties. These will be from the 'Instrument' domain.")
    lookthrough_portfolio: Optional[ResourceId] = Field(None, alias="lookthroughPortfolio")
    instrument_definition: Optional[LusidInstrument] = Field(None, alias="instrumentDefinition")
    state: StrictStr = Field(..., description="The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive, Deleted")
    asset_class: Optional[StrictStr] = Field(None, alias="assetClass", description="The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown")
    dom_ccy: Optional[StrictStr] = Field(None, alias="domCcy", description="The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD.")
    relationships: Optional[conlist(Relationship)] = Field(None, description="A set of relationships associated to the instrument.")
    links: Optional[conlist(Link)] = Field(None, description="Collection of links.")
    __properties = ["href", "scope", "lusidInstrumentId", "version", "name", "identifiers", "properties", "lookthroughPortfolio", "instrumentDefinition", "state", "assetClass", "domCcy", "relationships", "links"]

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Active', 'Inactive', 'Deleted'):
            raise ValueError("must be one of enum values ('Active', 'Inactive', 'Deleted')")
        return value

    @validator('asset_class')
    def asset_class_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('InterestRates', 'FX', 'Inflation', 'Equities', 'Credit', 'Commodities', 'Money', 'Unknown'):
            raise ValueError("must be one of enum values ('InterestRates', 'FX', 'Inflation', 'Equities', 'Credit', 'Commodities', 'Money', 'Unknown')")
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
    def from_json(cls, json_str: str) -> Instrument:
        """Create an instance of Instrument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item in self.properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of lookthrough_portfolio
        if self.lookthrough_portfolio:
            _dict['lookthroughPortfolio'] = self.lookthrough_portfolio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of instrument_definition
        if self.instrument_definition:
            _dict['instrumentDefinition'] = self.instrument_definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in relationships (list)
        _items = []
        if self.relationships:
            for _item in self.relationships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relationships'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if dom_ccy (nullable) is None
        # and __fields_set__ contains the field
        if self.dom_ccy is None and "dom_ccy" in self.__fields_set__:
            _dict['domCcy'] = None

        # set to None if relationships (nullable) is None
        # and __fields_set__ contains the field
        if self.relationships is None and "relationships" in self.__fields_set__:
            _dict['relationships'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Instrument:
        """Create an instance of Instrument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Instrument.parse_obj(obj)

        _obj = Instrument.parse_obj({
            "href": obj.get("href"),
            "scope": obj.get("scope"),
            "lusid_instrument_id": obj.get("lusidInstrumentId"),
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "name": obj.get("name"),
            "identifiers": obj.get("identifiers"),
            "properties": [ModelProperty.from_dict(_item) for _item in obj.get("properties")] if obj.get("properties") is not None else None,
            "lookthrough_portfolio": ResourceId.from_dict(obj.get("lookthroughPortfolio")) if obj.get("lookthroughPortfolio") is not None else None,
            "instrument_definition": LusidInstrument.from_dict(obj.get("instrumentDefinition")) if obj.get("instrumentDefinition") is not None else None,
            "state": obj.get("state"),
            "asset_class": obj.get("assetClass"),
            "dom_ccy": obj.get("domCcy"),
            "relationships": [Relationship.from_dict(_item) for _item in obj.get("relationships")] if obj.get("relationships") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
