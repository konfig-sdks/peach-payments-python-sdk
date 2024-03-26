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


class RequiredCheckoutV2Shipping(TypedDict):
    pass

class OptionalCheckoutV2Shipping(TypedDict, total=False):
    # The door number, floor, building number, building name, and/or street name of the shipping address.
    street1: str

    # The adjoining road or locality, if required, of the shipping address.
    street2: str

    # The town, district, or city of the shipping address.
    city: str

    # The company of the shipping address.
    company: str

    # The postal code or ZIP code of the shipping address.
    postcode: str

    # The country of the shipping address (ISO 3166-1).
    country: str

    # The county, state, or region of the shipping address.
    state: str

class CheckoutV2Shipping(RequiredCheckoutV2Shipping, OptionalCheckoutV2Shipping):
    pass
