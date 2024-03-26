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


class RequiredCard(TypedDict):
    pass

class OptionalCard(TypedDict, total=False):
    # The first six digits of the card number.
    bin: str

    # The last four digits of the card number.
    last4Digits: str

    # The card account holder.
    holder: str

    # The expiry month of the card.
    expiryMonth: str

    # The expiry year of the card.
    expiryYear: str

    # The type of card.
    type: str

class Card(RequiredCard, OptionalCard):
    pass
