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

from peach_payments_python_sdk.type.generate_link_payment_payment_files import GenerateLinkPaymentPaymentFiles

class RequiredGenerateLinkPaymentPayment(TypedDict):
    # Invoice ID that can be used to link the payment to an invoice on the merchant's system. Must be less than 17 characters.
    merchantInvoiceId: str

    # Payment amount. Must be positive and less than 1000000.00.
    amount: typing.Union[int, float]

    # The currency code of the payment request amount (ISO 4217).
    currency: str

class OptionalGenerateLinkPaymentPayment(TypedDict, total=False):
    files: GenerateLinkPaymentPaymentFiles

    # A note to include with the payment link.
    notes: str

class GenerateLinkPaymentPayment(RequiredGenerateLinkPaymentPayment, OptionalGenerateLinkPaymentPayment):
    pass
