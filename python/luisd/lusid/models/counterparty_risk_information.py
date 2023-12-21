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
from pydantic import BaseModel, Field, conlist, constr, validator
from lusid.models.credit_rating import CreditRating
from lusid.models.industry_classifier import IndustryClassifier

class CounterpartyRiskInformation(BaseModel):
    """
    In the event that the legal entity is a counterparty to an OTC transaction  (as signatory to a counterparty agreement such as an ISDA 2002 Master Agreement),  this information would be needed for calculations  such as Credit-Valuation-Adjustments and Debit-Valuation-Adjustments (CVA, DVA, XVA etc).  # noqa: E501
    """
    country_of_risk: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="countryOfRisk", description="The country to which one would naturally ascribe risk, typically the legal entity's country of registration. This can be used to infer funding currency and related market data in the absence of a specific preference.")
    credit_ratings: conlist(CreditRating) = Field(..., alias="creditRatings")
    industry_classifiers: conlist(IndustryClassifier) = Field(..., alias="industryClassifiers")
    __properties = ["countryOfRisk", "creditRatings", "industryClassifiers"]

    @validator('country_of_risk')
    def country_of_risk_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
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
    def from_json(cls, json_str: str) -> CounterpartyRiskInformation:
        """Create an instance of CounterpartyRiskInformation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in credit_ratings (list)
        _items = []
        if self.credit_ratings:
            for _item in self.credit_ratings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['creditRatings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in industry_classifiers (list)
        _items = []
        if self.industry_classifiers:
            for _item in self.industry_classifiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['industryClassifiers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CounterpartyRiskInformation:
        """Create an instance of CounterpartyRiskInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CounterpartyRiskInformation.parse_obj(obj)

        _obj = CounterpartyRiskInformation.parse_obj({
            "country_of_risk": obj.get("countryOfRisk"),
            "credit_ratings": [CreditRating.from_dict(_item) for _item in obj.get("creditRatings")] if obj.get("creditRatings") is not None else None,
            "industry_classifiers": [IndustryClassifier.from_dict(_item) for _item in obj.get("industryClassifiers")] if obj.get("industryClassifiers") is not None else None
        })
        return _obj
