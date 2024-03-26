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


class RequiredPaymentGetAllPaymentLinks200Response(TypedDict):
    pass

class OptionalPaymentGetAllPaymentLinks200Response(TypedDict, total=False):
    # A URL to download the exported file.
    file: str

class PaymentGetAllPaymentLinks200Response(RequiredPaymentGetAllPaymentLinks200Response, OptionalPaymentGetAllPaymentLinks200Response):
    pass
