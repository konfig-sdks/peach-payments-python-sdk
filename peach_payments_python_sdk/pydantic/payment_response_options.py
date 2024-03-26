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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class PaymentResponseOptions(BaseModel):
    # Indicates whether to send an email to the customer after creating the payment link.
    send_email: typing.Optional[bool] = Field(None, alias='sendEmail')

    # Indicates whether to send an SMS to the customer after creating the payment link.
    send_sms: typing.Optional[bool] = Field(None, alias='sendSms')

    # Indicates whether to send a WhatsApp message to the customer after creating the payment link.
    send_whatsapp: typing.Optional[bool] = Field(None, alias='sendWhatsapp')

    # List of comma-separated email addresses to CC.
    email_cc: typing.Optional[typing.Optional[str]] = Field(None, alias='emailCc')

    # List of comma-separated email addresses to BCC.
    email_bcc: typing.Optional[typing.Optional[str]] = Field(None, alias='emailBcc')

    # Webhook notification URL for this payment. Overrides the default set on the merchant.
    notification_url: typing.Optional[str] = Field(None, alias='notificationUrl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
