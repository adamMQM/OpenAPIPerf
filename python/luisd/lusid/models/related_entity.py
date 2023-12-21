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
from lusid.models.entity_identifier import EntityIdentifier
from lusid.models.lusid_unique_id import LusidUniqueId
from lusid.models.model_property import ModelProperty

class RelatedEntity(BaseModel):
    """
    Information about the other related entity in the relationship  # noqa: E501
    """
    entity_type: constr(strict=True, min_length=1) = Field(..., alias="entityType", description="The type of the entity.")
    entity_id: Dict[str, StrictStr] = Field(..., alias="entityId", description="The identifier of the other related entity in the relationship. It contains 'scope' and 'code' as keys for identifiers of a Portfolio or Portfolio Group, or 'idTypeScope', 'idTypeCode', 'code' as keys for identifiers of a Person or Legal Entity.")
    display_name: constr(strict=True, min_length=1) = Field(..., alias="displayName", description="The display name of the entity.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="The properties of the entity. This field is empty until further notice.")
    scope: Optional[StrictStr] = Field(None, description="The scope of the identifier")
    lusid_unique_id: Optional[LusidUniqueId] = Field(None, alias="lusidUniqueId")
    identifiers: conlist(EntityIdentifier) = Field(..., description="The identifiers of the related entity in the relationship.")
    href: Optional[StrictStr] = Field(None, description="The link to the entity.")
    __properties = ["entityType", "entityId", "displayName", "properties", "scope", "lusidUniqueId", "identifiers", "href"]

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
    def from_json(cls, json_str: str) -> RelatedEntity:
        """Create an instance of RelatedEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of lusid_unique_id
        if self.lusid_unique_id:
            _dict['lusidUniqueId'] = self.lusid_unique_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in identifiers (list)
        _items = []
        if self.identifiers:
            for _item in self.identifiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identifiers'] = _items
        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RelatedEntity:
        """Create an instance of RelatedEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RelatedEntity.parse_obj(obj)

        _obj = RelatedEntity.parse_obj({
            "entity_type": obj.get("entityType"),
            "entity_id": obj.get("entityId"),
            "display_name": obj.get("displayName"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "scope": obj.get("scope"),
            "lusid_unique_id": LusidUniqueId.from_dict(obj.get("lusidUniqueId")) if obj.get("lusidUniqueId") is not None else None,
            "identifiers": [EntityIdentifier.from_dict(_item) for _item in obj.get("identifiers")] if obj.get("identifiers") is not None else None,
            "href": obj.get("href")
        })
        return _obj
