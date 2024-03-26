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


class CheckoutOptions(BaseModel):
    # The default payment method to show when Checkout loads.
    default_payment_method: typing.Optional[typing.Optional[str]] = Field(None, alias='defaultPaymentMethod')

    # Force the default payment method to be the only payment method.
    force_default_method: typing.Optional[typing.Optional[bool]] = Field(None, alias='forceDefaultMethod')

    # Tokenise the card number to allow it to be stored.
    tokenise_card: typing.Optional[bool] = Field(None, alias='tokeniseCard')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
