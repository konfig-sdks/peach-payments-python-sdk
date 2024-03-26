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


class RequiredPaymentOptions(TypedDict):
    pass

class OptionalPaymentOptions(TypedDict, total=False):
    # Indicates whether to send an email to the customer after creating the payment link.
    sendEmail: bool

    # Indicates whether to send an SMS to the customer after creating the payment link.
    sendSms: bool

    # Indicates whether to send a WhatsApp message to the customer after creating the payment link.
    sendWhatsapp: bool

    # List of comma-separated email addresses to CC.
    emailCc: str

    # List of comma-separated email addresses to BCC.
    emailBcc: str

    # Time in minutes until the link expires. By default, expiry time is set to 30 days, which is also the maximum expiry time.
    expiryTime: int

    # Webhook notification URL for this payment. Overrides the default set on the merchant.
    notificationUrl: str

class PaymentOptions(RequiredPaymentOptions, OptionalPaymentOptions):
    pass
