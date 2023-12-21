# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PerpetualEntityState(str, Enum):
    """
    PerpetualEntityState
    """

    """
    allowed enum values
    """
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    DELETED = 'Deleted'

    @classmethod
    def from_json(cls, json_str: str) -> PerpetualEntityState:
        """Create an instance of PerpetualEntityState from a JSON string"""
        return PerpetualEntityState(json.loads(json_str))
