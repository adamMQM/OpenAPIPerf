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

from datetime import datetime
from typing import Any, Dict
from pydantic import BaseModel, Field, constr
from lusid.models.resource_id import ResourceId

class ComplianceRunInfoV2(BaseModel):
    """
    ComplianceRunInfoV2
    """
    run_id: ResourceId = Field(..., alias="runId")
    instigated_at: datetime = Field(..., alias="instigatedAt")
    completed_at: datetime = Field(..., alias="completedAt")
    schedule: constr(strict=True, min_length=1) = Field(...)
    instigated_by: constr(strict=True, min_length=1) = Field(..., alias="instigatedBy")
    __properties = ["runId", "instigatedAt", "completedAt", "schedule", "instigatedBy"]

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
    def from_json(cls, json_str: str) -> ComplianceRunInfoV2:
        """Create an instance of ComplianceRunInfoV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of run_id
        if self.run_id:
            _dict['runId'] = self.run_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceRunInfoV2:
        """Create an instance of ComplianceRunInfoV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ComplianceRunInfoV2.parse_obj(obj)

        _obj = ComplianceRunInfoV2.parse_obj({
            "run_id": ResourceId.from_dict(obj.get("runId")) if obj.get("runId") is not None else None,
            "instigated_at": obj.get("instigatedAt"),
            "completed_at": obj.get("completedAt"),
            "schedule": obj.get("schedule"),
            "instigated_by": obj.get("instigatedBy")
        })
        return _obj
