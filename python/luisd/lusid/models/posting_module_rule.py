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


from typing import Any, Dict
from pydantic import BaseModel, Field, constr, validator

class PostingModuleRule(BaseModel):
    """
    A Posting rule  # noqa: E501
    """
    rule_id: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="ruleId", description="The identifier for the Posting Rule.")
    account: constr(strict=True, max_length=512, min_length=1) = Field(..., description="The account to post the Activity credit or debit to.")
    rule_filter: constr(strict=True, max_length=16384, min_length=1) = Field(..., alias="ruleFilter", description="The filter syntax for the Posting Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax.")
    __properties = ["ruleId", "account", "ruleFilter"]

    @validator('rule_id')
    def rule_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('account')
    def account_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('rule_filter')
    def rule_filter_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
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
    def from_json(cls, json_str: str) -> PostingModuleRule:
        """Create an instance of PostingModuleRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostingModuleRule:
        """Create an instance of PostingModuleRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostingModuleRule.parse_obj(obj)

        _obj = PostingModuleRule.parse_obj({
            "rule_id": obj.get("ruleId"),
            "account": obj.get("account"),
            "rule_filter": obj.get("ruleFilter")
        })
        return _obj
