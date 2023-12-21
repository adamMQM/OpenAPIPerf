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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from lusid.models.aggregate_spec import AggregateSpec
from lusid.models.order_by_spec import OrderBySpec
from lusid.models.property_filter import PropertyFilter
from lusid.models.resource_id import ResourceId

class AggregatedTransactionsRequest(BaseModel):
    """
    AggregatedTransactionsRequest
    """
    from_transaction_date: datetime = Field(..., alias="fromTransactionDate")
    to_transaction_date: datetime = Field(..., alias="toTransactionDate")
    portfolio_id: ResourceId = Field(..., alias="portfolioId")
    as_at: Optional[datetime] = Field(None, alias="asAt")
    metrics: conlist(AggregateSpec) = Field(...)
    group_by: Optional[conlist(StrictStr)] = Field(None, alias="groupBy")
    filters: Optional[conlist(PropertyFilter)] = None
    sort: Optional[conlist(OrderBySpec)] = None
    __properties = ["fromTransactionDate", "toTransactionDate", "portfolioId", "asAt", "metrics", "groupBy", "filters", "sort"]

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
    def from_json(cls, json_str: str) -> AggregatedTransactionsRequest:
        """Create an instance of AggregatedTransactionsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of portfolio_id
        if self.portfolio_id:
            _dict['portfolioId'] = self.portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item in self.metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metrics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sort (list)
        _items = []
        if self.sort:
            for _item in self.sort:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sort'] = _items
        # set to None if as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at is None and "as_at" in self.__fields_set__:
            _dict['asAt'] = None

        # set to None if group_by (nullable) is None
        # and __fields_set__ contains the field
        if self.group_by is None and "group_by" in self.__fields_set__:
            _dict['groupBy'] = None

        # set to None if filters (nullable) is None
        # and __fields_set__ contains the field
        if self.filters is None and "filters" in self.__fields_set__:
            _dict['filters'] = None

        # set to None if sort (nullable) is None
        # and __fields_set__ contains the field
        if self.sort is None and "sort" in self.__fields_set__:
            _dict['sort'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AggregatedTransactionsRequest:
        """Create an instance of AggregatedTransactionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AggregatedTransactionsRequest.parse_obj(obj)

        _obj = AggregatedTransactionsRequest.parse_obj({
            "from_transaction_date": obj.get("fromTransactionDate"),
            "to_transaction_date": obj.get("toTransactionDate"),
            "portfolio_id": ResourceId.from_dict(obj.get("portfolioId")) if obj.get("portfolioId") is not None else None,
            "as_at": obj.get("asAt"),
            "metrics": [AggregateSpec.from_dict(_item) for _item in obj.get("metrics")] if obj.get("metrics") is not None else None,
            "group_by": obj.get("groupBy"),
            "filters": [PropertyFilter.from_dict(_item) for _item in obj.get("filters")] if obj.get("filters") is not None else None,
            "sort": [OrderBySpec.from_dict(_item) for _item in obj.get("sort")] if obj.get("sort") is not None else None
        })
        return _obj
