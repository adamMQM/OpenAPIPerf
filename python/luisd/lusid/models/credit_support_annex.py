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


from typing import Any, Dict, List, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr
from lusid.models.resource_id import ResourceId

class CreditSupportAnnex(BaseModel):
    """
    Entity to capture the calculable and queryable methods and practices of determining and transferring collateral  to a counterparty as part of margining of transactions. These typically come from a particular ISDA agreement  that is in place between the two counterparties.  # noqa: E501
    """
    reference_currency: StrictStr = Field(..., alias="referenceCurrency", description="The base, or reference, currency against which MtM value and exposure should be calculated  and in which the CSA parameters are defined if the currency is not otherwise explicitly stated.")
    collateral_currencies: conlist(StrictStr) = Field(..., alias="collateralCurrencies", description="The set of currencies within which it is acceptable to post cash collateral.")
    isda_agreement_version: constr(strict=True, max_length=128, min_length=0) = Field(..., alias="isdaAgreementVersion", description="The transactions will take place with reference to a particular ISDA master agreement. This  will likely be either the ISDA 1992 or ISDA 2002 agremeents or ISDA close-out 2009.")
    margin_call_frequency: constr(strict=True, max_length=32, min_length=0) = Field(..., alias="marginCallFrequency", description="The tenor, e.g. daily (1D) or biweekly (2W), at which frequency a margin call will be made, calculations  made and money transferred to readjust. The calculation might also require a specific time for valuation and notification.")
    valuation_agent: constr(strict=True, max_length=256, min_length=0) = Field(..., alias="valuationAgent", description="Are the calculations performed by the institutions's counterparty or the institution trading with them.")
    threshold_amount: Union[StrictFloat, StrictInt] = Field(..., alias="thresholdAmount", description="At what level of exposure does collateral need to be posted. Will typically be zero for banks.  Should be stated in reference currency")
    rounding_decimal_places: StrictInt = Field(..., alias="roundingDecimalPlaces", description="Where a calculation needs to be rounded to a specific number of decimal places,  this states the number that that requires.")
    initial_margin_amount: Union[StrictFloat, StrictInt] = Field(..., alias="initialMarginAmount", description="The initial margin that is required. In the reference currency")
    minimum_transfer_amount: Union[StrictFloat, StrictInt] = Field(..., alias="minimumTransferAmount", description="The minimum amount, in the reference currency, that must be transferred when required.")
    id: ResourceId = Field(...)
    __properties = ["referenceCurrency", "collateralCurrencies", "isdaAgreementVersion", "marginCallFrequency", "valuationAgent", "thresholdAmount", "roundingDecimalPlaces", "initialMarginAmount", "minimumTransferAmount", "id"]

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
    def from_json(cls, json_str: str) -> CreditSupportAnnex:
        """Create an instance of CreditSupportAnnex from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreditSupportAnnex:
        """Create an instance of CreditSupportAnnex from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreditSupportAnnex.parse_obj(obj)

        _obj = CreditSupportAnnex.parse_obj({
            "reference_currency": obj.get("referenceCurrency"),
            "collateral_currencies": obj.get("collateralCurrencies"),
            "isda_agreement_version": obj.get("isdaAgreementVersion"),
            "margin_call_frequency": obj.get("marginCallFrequency"),
            "valuation_agent": obj.get("valuationAgent"),
            "threshold_amount": obj.get("thresholdAmount"),
            "rounding_decimal_places": obj.get("roundingDecimalPlaces"),
            "initial_margin_amount": obj.get("initialMarginAmount"),
            "minimum_transfer_amount": obj.get("minimumTransferAmount"),
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None
        })
        return _obj
