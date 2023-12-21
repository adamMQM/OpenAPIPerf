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
from pydantic import BaseModel, Field, conlist
from lusid.models.list_aggregation_response import ListAggregationResponse
from lusid.models.result_data_schema import ResultDataSchema

class ListAggregationReconciliation(BaseModel):
    """
    ListAggregationReconciliation
    """
    left: Optional[ListAggregationResponse] = None
    right: Optional[ListAggregationResponse] = None
    diff: Optional[conlist(Dict[str, Any])] = None
    data_schema: Optional[ResultDataSchema] = Field(None, alias="dataSchema")
    __properties = ["left", "right", "diff", "dataSchema"]

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
    def from_json(cls, json_str: str) -> ListAggregationReconciliation:
        """Create an instance of ListAggregationReconciliation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of left
        if self.left:
            _dict['left'] = self.left.to_dict()
        # override the default output from pydantic by calling `to_dict()` of right
        if self.right:
            _dict['right'] = self.right.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_schema
        if self.data_schema:
            _dict['dataSchema'] = self.data_schema.to_dict()
        # set to None if diff (nullable) is None
        # and __fields_set__ contains the field
        if self.diff is None and "diff" in self.__fields_set__:
            _dict['diff'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListAggregationReconciliation:
        """Create an instance of ListAggregationReconciliation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListAggregationReconciliation.parse_obj(obj)

        _obj = ListAggregationReconciliation.parse_obj({
            "left": ListAggregationResponse.from_dict(obj.get("left")) if obj.get("left") is not None else None,
            "right": ListAggregationResponse.from_dict(obj.get("right")) if obj.get("right") is not None else None,
            "diff": obj.get("diff"),
            "data_schema": ResultDataSchema.from_dict(obj.get("dataSchema")) if obj.get("dataSchema") is not None else None
        })
        return _obj
