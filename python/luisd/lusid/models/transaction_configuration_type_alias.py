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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator

class TransactionConfigurationTypeAlias(BaseModel):
    """
    TransactionConfigurationTypeAlias
    """
    type: constr(strict=True, min_length=1) = Field(..., description="The transaction type")
    description: constr(strict=True, min_length=1) = Field(..., description="Brief description of the transaction")
    transaction_class: constr(strict=True, min_length=1) = Field(..., alias="transactionClass", description="Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut")
    transaction_group: Optional[StrictStr] = Field(None, alias="transactionGroup", description="Group is a set of codes related to a source, or sync. DEPRECATED: This field will be removed, use `Source` instead")
    source: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, description="Used to group a set of transaction types")
    transaction_roles: StrictStr = Field(..., alias="transactionRoles", description=". The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles")
    is_default: Optional[StrictBool] = Field(None, alias="isDefault", description="IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source.")
    __properties = ["type", "description", "transactionClass", "transactionGroup", "source", "transactionRoles", "isDefault"]

    @validator('source')
    def source_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('transaction_roles')
    def transaction_roles_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('None', 'LongLonger', 'LongShorter', 'ShortShorter', 'Shorter', 'ShortLonger', 'Longer', 'AllRoles'):
            raise ValueError("must be one of enum values ('None', 'LongLonger', 'LongShorter', 'ShortShorter', 'Shorter', 'ShortLonger', 'Longer', 'AllRoles')")
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
    def from_json(cls, json_str: str) -> TransactionConfigurationTypeAlias:
        """Create an instance of TransactionConfigurationTypeAlias from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if transaction_group (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction_group is None and "transaction_group" in self.__fields_set__:
            _dict['transactionGroup'] = None

        # set to None if source (nullable) is None
        # and __fields_set__ contains the field
        if self.source is None and "source" in self.__fields_set__:
            _dict['source'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionConfigurationTypeAlias:
        """Create an instance of TransactionConfigurationTypeAlias from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionConfigurationTypeAlias.parse_obj(obj)

        _obj = TransactionConfigurationTypeAlias.parse_obj({
            "type": obj.get("type"),
            "description": obj.get("description"),
            "transaction_class": obj.get("transactionClass"),
            "transaction_group": obj.get("transactionGroup"),
            "source": obj.get("source"),
            "transaction_roles": obj.get("transactionRoles"),
            "is_default": obj.get("isDefault")
        })
        return _obj
