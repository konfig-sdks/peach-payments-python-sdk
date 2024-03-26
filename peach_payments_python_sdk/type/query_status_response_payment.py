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


class RequiredQueryStatusResponsePayment(TypedDict):
    pass

class OptionalQueryStatusResponsePayment(TypedDict, total=False):
    # Payment link ID.
    linkId: str

    # Payment link URL.
    linkUrl: str

    # Payment amount.
    amount: typing.Union[int, float]

    # Payment link status.
    status: str

    # Currency code for the payment.
    currency: str

    # Payment order number provided by merchant.
    merchantInvoiceId: str

    # Merchant channel ID that the payment link was created in.
    entityId: str

    # A note to include with the payment link.
    notes: str

    # Timestamp when the payment link expires.
    expiryTime: str

    # Batch ID for the payment link.
    batchId: str

class QueryStatusResponsePayment(RequiredQueryStatusResponsePayment, OptionalQueryStatusResponsePayment):
    pass
