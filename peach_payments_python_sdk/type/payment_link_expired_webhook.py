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

from peach_payments_python_sdk.type.payment_link_base_webhook import PaymentLinkBaseWebhook

PaymentLinkExpiredWebhook = typing.Union[PaymentLinkBaseWebhook,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
