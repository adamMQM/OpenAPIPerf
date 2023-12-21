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
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from lusid.models.complete_portfolio import CompletePortfolio
from lusid.models.link import Link
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class ExpandedGroup(BaseModel):
    """
    ExpandedGroup
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    id: ResourceId = Field(...)
    display_name: constr(strict=True, min_length=1) = Field(..., alias="displayName", description="The name of the portfolio group.")
    description: Optional[StrictStr] = Field(None, description="The long form description of the portfolio group.")
    values: Optional[conlist(CompletePortfolio)] = Field(None, description="The collection of resource identifiers for the portfolios contained in the portfolio group.")
    sub_groups: Optional[conlist(ExpandedGroup)] = Field(None, alias="subGroups", description="The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.")
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = Field(None, description="Collection of links.")
    __properties = ["href", "id", "displayName", "description", "values", "subGroups", "version", "links"]

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
    def from_json(cls, json_str: str) -> ExpandedGroup:
        """Create an instance of ExpandedGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sub_groups (list)
        _items = []
        if self.sub_groups:
            for _item in self.sub_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
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

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if values (nullable) is None
        # and __fields_set__ contains the field
        if self.values is None and "values" in self.__fields_set__:
            _dict['values'] = None

        # set to None if sub_groups (nullable) is None
        # and __fields_set__ contains the field
        if self.sub_groups is None and "sub_groups" in self.__fields_set__:
            _dict['subGroups'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExpandedGroup:
        """Create an instance of ExpandedGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExpandedGroup.parse_obj(obj)

        _obj = ExpandedGroup.parse_obj({
            "href": obj.get("href"),
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "values": [CompletePortfolio.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None,
            "sub_groups": [ExpandedGroup.from_dict(_item) for _item in obj.get("subGroups")] if obj.get("subGroups") is not None else None,
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
