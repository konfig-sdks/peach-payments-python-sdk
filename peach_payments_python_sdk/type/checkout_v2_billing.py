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


class RequiredCheckoutV2Billing(TypedDict):
    pass

class OptionalCheckoutV2Billing(TypedDict, total=False):
    # The door number, floor, building number, building name, and/or street name of the billing address.
    street1: str

    # The adjoining road or locality, if required, of the billing address.
    street2: str

    # The town, district, or city of the billing address.
    city: str

    # The company of the billing address.
    company: str

    # The country of the billing address (ISO 3166-1).
    country: str

    # The county, state, or region of the billing address.
    state: str

    # The postal code or ZIP code of the billing address.
    postcode: str

class CheckoutV2Billing(RequiredCheckoutV2Billing, OptionalCheckoutV2Billing):
    pass
