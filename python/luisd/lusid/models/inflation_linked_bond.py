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
from typing import Any, Dict, List, Optional, Union
from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from lusid.models.flow_conventions import FlowConventions
from lusid.models.inflation_index_conventions import InflationIndexConventions
from lusid.models.lusid_instrument import LusidInstrument
from lusid.models.rounding_convention import RoundingConvention

class InflationLinkedBond(LusidInstrument):
    """
    Inflation Linked Bond.  # noqa: E501
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the bond.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.")
    flow_conventions: FlowConventions = Field(..., alias="flowConventions")
    inflation_index_conventions: InflationIndexConventions = Field(..., alias="inflationIndexConventions")
    coupon_rate: Union[StrictFloat, StrictInt] = Field(..., alias="couponRate", description="Simple coupon rate.")
    identifiers: Optional[Dict[str, StrictStr]] = Field(None, description="External market codes and identifiers for the bond, e.g. ISIN.")
    base_cpi: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="baseCPI", description="BaseCPI value. This is optional, if not provided the BaseCPI value will be calculated from the BaseCPIDate,  if that too is not present the StartDate will be used.                If provided then this value will always set the BaseCPI on this bond.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the BaseCPIDate.")
    base_cpi_date: Optional[datetime] = Field(None, alias="baseCPIDate", description="BaseCPIDate. This is optional. Gives the date that the BaseCPI is calculated for.                Note this is an un-lagged date (similar to StartDate) so the Bond ObservationLag will  be applied to this date when calculating the CPI.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the actual BaseCPI.")
    calculation_type: Optional[StrictStr] = Field(None, alias="calculationType", description="The calculation type applied to the bond coupon and principal amount.  The default CalculationType is `Standard`.    Supported string (enumeration) values are: [Standard, Quarterly, Ratio, Brazil].")
    ex_dividend_days: Optional[StrictInt] = Field(None, alias="exDividendDays", description="Number of Good Business Days before the next coupon payment, in which the bond goes ex-dividend.")
    index_precision: Optional[StrictInt] = Field(None, alias="indexPrecision", description="Number of decimal places used to round IndexRatio. This defaults to 5 if not set.")
    principal: Union[StrictFloat, StrictInt] = Field(..., description="The face-value or principal for the bond at outset.")
    principal_protection: Optional[StrictBool] = Field(None, alias="principalProtection", description="If true then the principal is protected in that the redemption amount will be at least the face value (Principal).  This is typically set to true for inflation linked bonds issued by the United States and France (for example).  This is typically set to false for inflation linked bonds issued by the United Kingdom (post 2005).  For other sovereigns this can vary from issue to issue.  If not set this property defaults to true.  This is sometimes referred to as Deflation protection or an inflation floor of 0%.")
    stub_type: Optional[StrictStr] = Field(None, alias="stubType", description="StubType. Most Inflation linked bonds have a ShortFront stub type so this is the default, however in some cases  with a long front stub LongFront should be selected.  StubType Both is not supported for InflationLinkedBonds.    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both].")
    rounding_conventions: Optional[conlist(RoundingConvention)] = Field(None, alias="roundingConventions", description="Rounding conventions for analytics, if any.")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "startDate", "maturityDate", "flowConventions", "inflationIndexConventions", "couponRate", "identifiers", "baseCPI", "baseCPIDate", "calculationType", "exDividendDays", "indexPrecision", "principal", "principalProtection", "stubType", "roundingConventions"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg'):
            raise ValueError("must be one of enum values ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg')")
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
    def from_json(cls, json_str: str) -> InflationLinkedBond:
        """Create an instance of InflationLinkedBond from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of flow_conventions
        if self.flow_conventions:
            _dict['flowConventions'] = self.flow_conventions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inflation_index_conventions
        if self.inflation_index_conventions:
            _dict['inflationIndexConventions'] = self.inflation_index_conventions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rounding_conventions (list)
        _items = []
        if self.rounding_conventions:
            for _item in self.rounding_conventions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roundingConventions'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if identifiers (nullable) is None
        # and __fields_set__ contains the field
        if self.identifiers is None and "identifiers" in self.__fields_set__:
            _dict['identifiers'] = None

        # set to None if base_cpi (nullable) is None
        # and __fields_set__ contains the field
        if self.base_cpi is None and "base_cpi" in self.__fields_set__:
            _dict['baseCPI'] = None

        # set to None if base_cpi_date (nullable) is None
        # and __fields_set__ contains the field
        if self.base_cpi_date is None and "base_cpi_date" in self.__fields_set__:
            _dict['baseCPIDate'] = None

        # set to None if calculation_type (nullable) is None
        # and __fields_set__ contains the field
        if self.calculation_type is None and "calculation_type" in self.__fields_set__:
            _dict['calculationType'] = None

        # set to None if ex_dividend_days (nullable) is None
        # and __fields_set__ contains the field
        if self.ex_dividend_days is None and "ex_dividend_days" in self.__fields_set__:
            _dict['exDividendDays'] = None

        # set to None if stub_type (nullable) is None
        # and __fields_set__ contains the field
        if self.stub_type is None and "stub_type" in self.__fields_set__:
            _dict['stubType'] = None

        # set to None if rounding_conventions (nullable) is None
        # and __fields_set__ contains the field
        if self.rounding_conventions is None and "rounding_conventions" in self.__fields_set__:
            _dict['roundingConventions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InflationLinkedBond:
        """Create an instance of InflationLinkedBond from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InflationLinkedBond.parse_obj(obj)

        _obj = InflationLinkedBond.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "flow_conventions": FlowConventions.from_dict(obj.get("flowConventions")) if obj.get("flowConventions") is not None else None,
            "inflation_index_conventions": InflationIndexConventions.from_dict(obj.get("inflationIndexConventions")) if obj.get("inflationIndexConventions") is not None else None,
            "coupon_rate": obj.get("couponRate"),
            "identifiers": obj.get("identifiers"),
            "base_cpi": obj.get("baseCPI"),
            "base_cpi_date": obj.get("baseCPIDate"),
            "calculation_type": obj.get("calculationType"),
            "ex_dividend_days": obj.get("exDividendDays"),
            "index_precision": obj.get("indexPrecision"),
            "principal": obj.get("principal"),
            "principal_protection": obj.get("principalProtection"),
            "stub_type": obj.get("stubType"),
            "rounding_conventions": [RoundingConvention.from_dict(_item) for _item in obj.get("roundingConventions")] if obj.get("roundingConventions") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
