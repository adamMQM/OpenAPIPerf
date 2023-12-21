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
from lusid.models.portfolio_group import PortfolioGroup

class PagedResourceListOfPortfolioGroup(BaseModel):
    """
    A paginated list of resource that can be returned from a request.  # noqa: E501
    """
    next_page: Optional[StrictStr] = Field(None, alias="nextPage", description="The next page of results.")
    previous_page: Optional[StrictStr] = Field(None, alias="previousPage", description="The previous page of results.")
    values: conlist(PortfolioGroup) = Field(..., description="The resources to list.")
    href: Optional[StrictStr] = Field(None, description="The URI of the resource list.")
    links: Optional[conlist(Link)] = Field(None, description="Collection of links.")
    __properties = ["nextPage", "previousPage", "values", "href", "links"]

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
    def from_json(cls, json_str: str) -> PagedResourceListOfPortfolioGroup:
        """Create an instance of PagedResourceListOfPortfolioGroup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if next_page (nullable) is None
        # and __fields_set__ contains the field
        if self.next_page is None and "next_page" in self.__fields_set__:
            _dict['nextPage'] = None

        # set to None if previous_page (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_page is None and "previous_page" in self.__fields_set__:
            _dict['previousPage'] = None

        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PagedResourceListOfPortfolioGroup:
        """Create an instance of PagedResourceListOfPortfolioGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PagedResourceListOfPortfolioGroup.parse_obj(obj)

        _obj = PagedResourceListOfPortfolioGroup.parse_obj({
            "next_page": obj.get("nextPage"),
            "previous_page": obj.get("previousPage"),
            "values": [PortfolioGroup.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None,
            "href": obj.get("href"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
