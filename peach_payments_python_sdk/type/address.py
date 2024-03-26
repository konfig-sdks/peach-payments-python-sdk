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

if TYPE_CHECKING:
    from peach_payments_python_sdk.type.customer import Customer

class RequiredAddress(TypedDict):
    pass

class OptionalAddress(TypedDict, total=False):
    # The door number, floor, building number, building name, and/or street name of the billing or shipping address.
    street1: str

    # The town, district, or city linked to billing or shipping.
    city: str

    # The county, state, or region of the billing address.
    state: str

    # The postal code or ZIP code of the address.
    postalCode: str

    # The country linked to billing or shipping as defined by ISO-3166-1 alpha-2.
    country: str

    # The customer's company name.
    company: str

    # Primary house number of the billing or shipping address.
    houseNumber1: str

    # The postal code or zip code of the billing or shipping address.
    postcode: str

    # Secondary house number of the billing or shipping address. Used when more addresses are bundled to the same primary house number. If present, houseNumber1 is mandatory.
    street2: str

    customer: 'Customer'

class Address(RequiredAddress, OptionalAddress):
    pass
