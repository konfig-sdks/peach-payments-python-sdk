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


class RequiredPaymentResponseOptions(TypedDict):
    pass

class OptionalPaymentResponseOptions(TypedDict, total=False):
    # Indicates whether to send an email to the customer after creating the payment link.
    sendEmail: bool

    # Indicates whether to send an SMS to the customer after creating the payment link.
    sendSms: bool

    # Indicates whether to send a WhatsApp message to the customer after creating the payment link.
    sendWhatsapp: bool

    # List of comma-separated email addresses to CC.
    emailCc: typing.Optional[str]

    # List of comma-separated email addresses to BCC.
    emailBcc: typing.Optional[str]

    # Webhook notification URL for this payment. Overrides the default set on the merchant.
    notificationUrl: str

class PaymentResponseOptions(RequiredPaymentResponseOptions, OptionalPaymentResponseOptions):
    pass
