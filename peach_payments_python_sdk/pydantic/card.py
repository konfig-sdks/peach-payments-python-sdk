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


class Card(BaseModel):
    # The first six digits of the card number.
    bin: typing.Optional[str] = Field(None, alias='bin')

    # The last four digits of the card number.
    last4_digits: typing.Optional[str] = Field(None, alias='last4Digits')

    # The card account holder.
    holder: typing.Optional[str] = Field(None, alias='holder')

    # The expiry month of the card.
    expiry_month: typing.Optional[str] = Field(None, alias='expiryMonth')

    # The expiry year of the card.
    expiry_year: typing.Optional[str] = Field(None, alias='expiryYear')

    # The type of card.
    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
