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

from peach_payments_python_sdk.pydantic.redirect_post_data import RedirectPostData

class CheckoutStatus(BaseModel):
    # The status of the object.
    status: typing.Optional[str] = Field(None, alias='status')

    # The remaining time, in seconds, of the checkout instance.
    timestamp: typing.Optional[str] = Field(None, alias='timestamp')

    # Redirect URL for Checkout.
    redirect_url: typing.Optional[str] = Field(None, alias='redirect_url')

    redirect_post_data: typing.Optional[RedirectPostData] = Field(None, alias='redirect_post_data')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
