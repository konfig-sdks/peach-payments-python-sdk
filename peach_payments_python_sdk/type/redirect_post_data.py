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


RequiredRedirectPostData = TypedDict("RequiredRedirectPostData", {
    })

OptionalRedirectPostData = TypedDict("OptionalRedirectPostData", {
    # The checkout amount.
    "amount": str,

    "checkoutId": str,

    # The currency code of the payment request amount.
    "currency": str,

    # The merchant transaction ID set when creating the checkout.
    "merchantTransactionId": str,

    "paymentType": str,

    # A code representing the transaction state.
    "result.code": str,

    # A friendly message.
    "result.description": str,

    # Date and time when the checkout was created.
    "timestamp": str,
    }, total=False)

class RedirectPostData(RequiredRedirectPostData, OptionalRedirectPostData):
    pass
