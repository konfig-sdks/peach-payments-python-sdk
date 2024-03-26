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

if TYPE_CHECKING:
    from peach_payments_python_sdk.pydantic.customer import Customer

class Address(BaseModel):
    # The door number, floor, building number, building name, and/or street name of the billing or shipping address.
    street1: typing.Optional[str] = Field(None, alias='street1')

    # The town, district, or city linked to billing or shipping.
    city: typing.Optional[str] = Field(None, alias='city')

    # The county, state, or region of the billing address.
    state: typing.Optional[str] = Field(None, alias='state')

    # The postal code or ZIP code of the address.
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    # The country linked to billing or shipping as defined by ISO-3166-1 alpha-2.
    country: typing.Optional[str] = Field(None, alias='country')

    # The customer's company name.
    company: typing.Optional[str] = Field(None, alias='company')

    # Primary house number of the billing or shipping address.
    house_number1: typing.Optional[str] = Field(None, alias='houseNumber1')

    # The postal code or zip code of the billing or shipping address.
    postcode: typing.Optional[str] = Field(None, alias='postcode')

    # Secondary house number of the billing or shipping address. Used when more addresses are bundled to the same primary house number. If present, houseNumber1 is mandatory.
    street2: typing.Optional[str] = Field(None, alias='street2')

    customer: typing.Optional['Customer'] = Field(None, alias='customer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
