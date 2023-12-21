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
from lusid.models.reference_list import ReferenceList
from lusid.models.resource_id import ResourceId

class ReferenceListRequest(BaseModel):
    """
    ReferenceListRequest
    """
    id: ResourceId = Field(...)
    name: constr(strict=True, min_length=1) = Field(..., description="The name of the reference list.")
    description: Optional[StrictStr] = Field(None, description="The description of the reference list.")
    tags: Optional[conlist(StrictStr)] = Field(None, description="The tags associated with the reference list.")
    reference_list: ReferenceList = Field(..., alias="referenceList")
    __properties = ["id", "name", "description", "tags", "referenceList"]

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
    def from_json(cls, json_str: str) -> ReferenceListRequest:
        """Create an instance of ReferenceListRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reference_list
        if self.reference_list:
            _dict['referenceList'] = self.reference_list.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if tags (nullable) is None
        # and __fields_set__ contains the field
        if self.tags is None and "tags" in self.__fields_set__:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferenceListRequest:
        """Create an instance of ReferenceListRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferenceListRequest.parse_obj(obj)

        _obj = ReferenceListRequest.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "tags": obj.get("tags"),
            "reference_list": ReferenceList.from_dict(obj.get("referenceList")) if obj.get("referenceList") is not None else None
        })
        return _obj
