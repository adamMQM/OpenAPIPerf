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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator
from lusid.models.address_key_option_definition import AddressKeyOptionDefinition

class AggregationQuery(BaseModel):
    """
    AggregationQuery
    """
    address_key: constr(strict=True, min_length=1) = Field(..., alias="addressKey", description="The address that is the query to be made into the system. e.g. a Valuation/PV or Instrument/MaturityDate")
    description: constr(strict=True, min_length=1) = Field(..., description="What does the information that is being queried by the address mean. What is the address for.")
    display_name: constr(strict=True, min_length=1) = Field(..., alias="displayName", description="The suggested name that the user would wish to put on to the returned information for visualisation in preference to the address.")
    type: StrictStr = Field(..., description="Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the more complex representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \"Result0D\", the decimal-currency pair. The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Result0D, Json")
    flattened_type: StrictStr = Field(..., alias="flattenedType", description="Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the simpler representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \"Decimal\". The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Result0D, Json")
    scales_with_holding_quantity: StrictBool = Field(..., alias="scalesWithHoldingQuantity", description="Is the data scaled when it is for, e.g. a holding in an instrument. A key example would be the difference between price and PV. The present value of an instrument would scale with the quantity held. The price would be that for a hypothetical unit of that instrument, typically associated with the contract size.")
    supported_operations: constr(strict=True, min_length=1) = Field(..., alias="supportedOperations", description="When performing an aggregation operation, what column type operations can be performed on the data. For example, it makes sense to sum decimals but not strings. Either can be counted. With more complex types, e.g. ResultValues, operations may be linked to a semantic meaning such as the currency of the result. In such cases the operations may be supported but context specific. For example, it makes sense to sum PVs in a single currency but not when the currency is different. In such cases, an error would result (it being assumed that no fx rates for currency conversion were implicit in the context).")
    life_cycle_status: constr(strict=True, min_length=1) = Field(..., alias="lifeCycleStatus", description="Within an API where an item can be accessed through an address or property, there is an associated status that determines whether the item is stable or likely to change. This status is one of [Experimental, Beta, EAP, Prod,  Deprecated]. If the item is deprecated it will be removed on or after the associated DateTime RemovalDate field. That field will not otherwise be set.")
    removal_date: Optional[datetime] = Field(None, alias="removalDate", description="If the life cycle status is set to deprecated then this will be populated with the date on or after which removal of the address query will happen")
    applicable_options: Optional[Dict[str, AddressKeyOptionDefinition]] = Field(None, alias="applicableOptions", description="A mapping from option names to the definition that the corresponding option value must match.")
    __properties = ["addressKey", "description", "displayName", "type", "flattenedType", "scalesWithHoldingQuantity", "supportedOperations", "lifeCycleStatus", "removalDate", "applicableOptions"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('String', 'Int', 'Decimal', 'DateTime', 'Boolean', 'ResultValue', 'Result0D', 'Json'):
            raise ValueError("must be one of enum values ('String', 'Int', 'Decimal', 'DateTime', 'Boolean', 'ResultValue', 'Result0D', 'Json')")
        return value

    @validator('flattened_type')
    def flattened_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('String', 'Int', 'Decimal', 'DateTime', 'Boolean', 'ResultValue', 'Result0D', 'Json'):
            raise ValueError("must be one of enum values ('String', 'Int', 'Decimal', 'DateTime', 'Boolean', 'ResultValue', 'Result0D', 'Json')")
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
    def from_json(cls, json_str: str) -> AggregationQuery:
        """Create an instance of AggregationQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in applicable_options (dict)
        _field_dict = {}
        if self.applicable_options:
            for _key in self.applicable_options:
                if self.applicable_options[_key]:
                    _field_dict[_key] = self.applicable_options[_key].to_dict()
            _dict['applicableOptions'] = _field_dict
        # set to None if removal_date (nullable) is None
        # and __fields_set__ contains the field
        if self.removal_date is None and "removal_date" in self.__fields_set__:
            _dict['removalDate'] = None

        # set to None if applicable_options (nullable) is None
        # and __fields_set__ contains the field
        if self.applicable_options is None and "applicable_options" in self.__fields_set__:
            _dict['applicableOptions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AggregationQuery:
        """Create an instance of AggregationQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AggregationQuery.parse_obj(obj)

        _obj = AggregationQuery.parse_obj({
            "address_key": obj.get("addressKey"),
            "description": obj.get("description"),
            "display_name": obj.get("displayName"),
            "type": obj.get("type"),
            "flattened_type": obj.get("flattenedType"),
            "scales_with_holding_quantity": obj.get("scalesWithHoldingQuantity"),
            "supported_operations": obj.get("supportedOperations"),
            "life_cycle_status": obj.get("lifeCycleStatus"),
            "removal_date": obj.get("removalDate"),
            "applicable_options": dict(
                (_k, AddressKeyOptionDefinition.from_dict(_v))
                for _k, _v in obj.get("applicableOptions").items()
            )
            if obj.get("applicableOptions") is not None
            else None
        })
        return _obj
