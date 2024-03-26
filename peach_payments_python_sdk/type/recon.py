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


class RequiredRecon(TypedDict):
    pass

class OptionalRecon(TypedDict, total=False):
    # The payment service provider merchant number.
    ciMerchantNumber: str

    # The reconciliation reference number from the payment service provider.
    rrn: str

    # The authorisation code from the payment service provider.
    authCode: str

    # The result code from the payment service provider.
    resultCode: str

    # The STAN reference number from the payment service provider.
    stan: str

class Recon(RequiredRecon, OptionalRecon):
    pass
