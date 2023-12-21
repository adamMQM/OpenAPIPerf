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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, conlist, constr
from lusid.models.compliance_template_parameter import ComplianceTemplateParameter
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.resource_id import ResourceId

class ComplianceTemplateVariation(BaseModel):
    """
    ComplianceTemplateVariation
    """
    label: constr(strict=True, min_length=1) = Field(..., description="Label of a Compliance Template Variation")
    description: constr(strict=True, min_length=1) = Field(..., description="The description of the Compliance Template Variation")
    required_parameters: conlist(ComplianceTemplateParameter) = Field(..., alias="requiredParameters", description="A parameter required by a Compliance Template Variation")
    properties: Dict[str, PerpetualProperty] = Field(..., description="Properties associated with the Compliance Template Variation")
    accepted_address_keys: ResourceId = Field(..., alias="acceptedAddressKeys")
    __properties = ["label", "description", "requiredParameters", "properties", "acceptedAddressKeys"]

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
    def from_json(cls, json_str: str) -> ComplianceTemplateVariation:
        """Create an instance of ComplianceTemplateVariation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in required_parameters (list)
        _items = []
        if self.required_parameters:
            for _item in self.required_parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requiredParameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of accepted_address_keys
        if self.accepted_address_keys:
            _dict['acceptedAddressKeys'] = self.accepted_address_keys.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceTemplateVariation:
        """Create an instance of ComplianceTemplateVariation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceTemplateVariation.parse_obj(obj)

        _obj = ComplianceTemplateVariation.parse_obj({
            "label": obj.get("label"),
            "description": obj.get("description"),
            "required_parameters": [ComplianceTemplateParameter.from_dict(_item) for _item in obj.get("requiredParameters")] if obj.get("requiredParameters") is not None else None,
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "accepted_address_keys": ResourceId.from_dict(obj.get("acceptedAddressKeys")) if obj.get("acceptedAddressKeys") is not None else None
        })
        return _obj
