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
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from lusid.models.currency_and_amount import CurrencyAndAmount
from lusid.models.link import Link
from lusid.models.model_property import ModelProperty
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.resource_id import ResourceId

class JournalEntryLine(BaseModel):
    """
    A Journal Entry line entity.  # noqa: E501
    """
    accounting_date: datetime = Field(..., alias="accountingDate", description="The Journal Entry Line accounting date.")
    activity_date: datetime = Field(..., alias="activityDate", description="The actual date of the activity. Differs from the accounting date when creating journals that would occur in a closed period.")
    portfolio_id: ResourceId = Field(..., alias="portfolioId")
    instrument_id: constr(strict=True, min_length=1) = Field(..., alias="instrumentId", description="To indicate the instrument of the transaction that the Journal Entry Line posted for, if applicable.")
    instrument_scope: constr(strict=True, min_length=1) = Field(..., alias="instrumentScope", description="The scope in which the Journal Entry Line instrument is in.")
    sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = Field(None, alias="subHoldingKeys", description="The sub-holding properties which are part of the AccountingKey.")
    tax_lot_id: constr(strict=True, min_length=1) = Field(..., alias="taxLotId", description="The tax lot Id that the Journal Entry Line is impacting.")
    general_ledger_account_code: constr(strict=True, min_length=1) = Field(..., alias="generalLedgerAccountCode", description="The code of the account in the general ledger the Journal Entry was posted to.")
    local: CurrencyAndAmount = Field(...)
    base: CurrencyAndAmount = Field(...)
    posting_module_code: Optional[StrictStr] = Field(None, alias="postingModuleCode", description="The code of the posting module where the posting rules derived the Journal Entry lines.")
    posting_rule: constr(strict=True, min_length=1) = Field(..., alias="postingRule", description="The rule generating the Journal Entry Line.")
    as_at_date: datetime = Field(..., alias="asAtDate", description="The corresponding input date and time of the Transaction generating the Journal Entry Line.")
    activities_description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, alias="activitiesDescription", description="This would be the description of the business activities this Journal Entry Line is for.")
    source_type: constr(strict=True, min_length=1) = Field(..., alias="sourceType", description="So far are 4 types: LusidTxn, LusidValuation, Manual and External.")
    source_id: constr(strict=True, min_length=1) = Field(..., alias="sourceId", description="For the Lusid Source Type this will be the txn Id. For the rest will be what the user populates.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="A set of properties for the Abor.")
    movement_name: constr(strict=True, min_length=1) = Field(..., alias="movementName", description="The name of the movement.")
    holding_type: constr(strict=True, min_length=1) = Field(..., alias="holdingType", description="Defines the broad category holding within the portfolio.")
    economic_bucket: constr(strict=True, min_length=1) = Field(..., alias="economicBucket", description="Raw Journal Entry Line details of the economic bucket for the Journal Entry Line.")
    levels: Optional[conlist(StrictStr)] = Field(None, description="Resolved data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body.")
    source_levels: Optional[conlist(StrictStr)] = Field(None, alias="sourceLevels", description="Source data from the general ledger profile where the GeneralLedgerProfileCode is specified in the GetJournalEntryLines request body.")
    movement_sign: Optional[StrictStr] = Field(None, alias="movementSign", description="Indicates if the Journal Entry Line corresponds to a Long or Short movement.")
    holding_sign: Optional[StrictStr] = Field(None, alias="holdingSign", description="Indicates if the Journal Entry Line is operating against a Long or Short holding.")
    links: Optional[conlist(Link)] = Field(None, description="Collection of links.")
    __properties = ["accountingDate", "activityDate", "portfolioId", "instrumentId", "instrumentScope", "subHoldingKeys", "taxLotId", "generalLedgerAccountCode", "local", "base", "postingModuleCode", "postingRule", "asAtDate", "activitiesDescription", "sourceType", "sourceId", "properties", "movementName", "holdingType", "economicBucket", "levels", "sourceLevels", "movementSign", "holdingSign", "links"]

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
    def from_json(cls, json_str: str) -> JournalEntryLine:
        """Create an instance of JournalEntryLine from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in sub_holding_keys (dict)
        _field_dict = {}
        if self.sub_holding_keys:
            for _key in self.sub_holding_keys:
                if self.sub_holding_keys[_key]:
                    _field_dict[_key] = self.sub_holding_keys[_key].to_dict()
            _dict['subHoldingKeys'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of local
        if self.local:
            _dict['local'] = self.local.to_dict()
        # override the default output from pydantic by calling `to_dict()` of base
        if self.base:
            _dict['base'] = self.base.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if sub_holding_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.sub_holding_keys is None and "sub_holding_keys" in self.__fields_set__:
            _dict['subHoldingKeys'] = None

        # set to None if posting_module_code (nullable) is None
        # and __fields_set__ contains the field
        if self.posting_module_code is None and "posting_module_code" in self.__fields_set__:
            _dict['postingModuleCode'] = None

        # set to None if activities_description (nullable) is None
        # and __fields_set__ contains the field
        if self.activities_description is None and "activities_description" in self.__fields_set__:
            _dict['activitiesDescription'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if levels (nullable) is None
        # and __fields_set__ contains the field
        if self.levels is None and "levels" in self.__fields_set__:
            _dict['levels'] = None

        # set to None if source_levels (nullable) is None
        # and __fields_set__ contains the field
        if self.source_levels is None and "source_levels" in self.__fields_set__:
            _dict['sourceLevels'] = None

        # set to None if movement_sign (nullable) is None
        # and __fields_set__ contains the field
        if self.movement_sign is None and "movement_sign" in self.__fields_set__:
            _dict['movementSign'] = None

        # set to None if holding_sign (nullable) is None
        # and __fields_set__ contains the field
        if self.holding_sign is None and "holding_sign" in self.__fields_set__:
            _dict['holdingSign'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JournalEntryLine:
        """Create an instance of JournalEntryLine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JournalEntryLine.parse_obj(obj)

        _obj = JournalEntryLine.parse_obj({
            "accounting_date": obj.get("accountingDate"),
            "activity_date": obj.get("activityDate"),
            "portfolio_id": ResourceId.from_dict(obj.get("portfolioId")) if obj.get("portfolioId") is not None else None,
            "instrument_id": obj.get("instrumentId"),
            "instrument_scope": obj.get("instrumentScope"),
            "sub_holding_keys": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("subHoldingKeys").items()
            )
            if obj.get("subHoldingKeys") is not None
            else None,
            "tax_lot_id": obj.get("taxLotId"),
            "general_ledger_account_code": obj.get("generalLedgerAccountCode"),
            "local": CurrencyAndAmount.from_dict(obj.get("local")) if obj.get("local") is not None else None,
            "base": CurrencyAndAmount.from_dict(obj.get("base")) if obj.get("base") is not None else None,
            "posting_module_code": obj.get("postingModuleCode"),
            "posting_rule": obj.get("postingRule"),
            "as_at_date": obj.get("asAtDate"),
            "activities_description": obj.get("activitiesDescription"),
            "source_type": obj.get("sourceType"),
            "source_id": obj.get("sourceId"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "movement_name": obj.get("movementName"),
            "holding_type": obj.get("holdingType"),
            "economic_bucket": obj.get("economicBucket"),
            "levels": obj.get("levels"),
            "source_levels": obj.get("sourceLevels"),
            "movement_sign": obj.get("movementSign"),
            "holding_sign": obj.get("holdingSign"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
