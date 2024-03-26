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

from peach_payments_python_sdk.type.redirect_post_data import RedirectPostData

class RequiredCheckoutStatus(TypedDict):
    pass

class OptionalCheckoutStatus(TypedDict, total=False):
    # The status of the object.
    status: str

    # The remaining time, in seconds, of the checkout instance.
    timestamp: str

    # Redirect URL for Checkout.
    redirect_url: str

    redirect_post_data: RedirectPostData

class CheckoutStatus(RequiredCheckoutStatus, OptionalCheckoutStatus):
    pass
