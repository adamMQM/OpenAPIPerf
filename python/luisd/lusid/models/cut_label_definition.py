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
from lusid.models.cut_local_time import CutLocalTime
from lusid.models.link import Link
from lusid.models.version import Version

class CutLabelDefinition(BaseModel):
    """
    CutLabelDefinition
    """
    code: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = Field(None, alias="displayName")
    description: Optional[StrictStr] = None
    cut_local_time: Optional[CutLocalTime] = Field(None, alias="cutLocalTime")
    time_zone: Optional[StrictStr] = Field(None, alias="timeZone")
    href: Optional[StrictStr] = None
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = Field(None, description="Collection of links.")
    __properties = ["code", "displayName", "description", "cutLocalTime", "timeZone", "href", "version", "links"]

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
    def from_json(cls, json_str: str) -> CutLabelDefinition:
        """Create an instance of CutLabelDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cut_local_time
        if self.cut_local_time:
            _dict['cutLocalTime'] = self.cut_local_time.to_dict()
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
        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if time_zone (nullable) is None
        # and __fields_set__ contains the field
        if self.time_zone is None and "time_zone" in self.__fields_set__:
            _dict['timeZone'] = None

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
    def from_dict(cls, obj: dict) -> CutLabelDefinition:
        """Create an instance of CutLabelDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CutLabelDefinition.parse_obj(obj)

        _obj = CutLabelDefinition.parse_obj({
            "code": obj.get("code"),
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "cut_local_time": CutLocalTime.from_dict(obj.get("cutLocalTime")) if obj.get("cutLocalTime") is not None else None,
            "time_zone": obj.get("timeZone"),
            "href": obj.get("href"),
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
