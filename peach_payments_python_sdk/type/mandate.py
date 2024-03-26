# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredMandate(TypedDict):
    pass

class OptionalMandate(TypedDict, total=False):
    # The date the direct debit mandate was signed.
    dateOfSignature: str

    # The ID of the direct debit mandate.
    id: str

    # The mandate reference for direct debit as a contractual agreement between the creditor and the debtor.
    reference: str

class Mandate(RequiredMandate, OptionalMandate):
    pass
