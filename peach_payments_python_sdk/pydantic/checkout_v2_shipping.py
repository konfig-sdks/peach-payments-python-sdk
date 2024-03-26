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


class CheckoutV2Shipping(BaseModel):
    # The door number, floor, building number, building name, and/or street name of the shipping address.
    street1: typing.Optional[str] = Field(None, alias='street1')

    # The adjoining road or locality, if required, of the shipping address.
    street2: typing.Optional[str] = Field(None, alias='street2')

    # The town, district, or city of the shipping address.
    city: typing.Optional[str] = Field(None, alias='city')

    # The company of the shipping address.
    company: typing.Optional[str] = Field(None, alias='company')

    # The postal code or ZIP code of the shipping address.
    postcode: typing.Optional[str] = Field(None, alias='postcode')

    # The country of the shipping address (ISO 3166-1).
    country: typing.Optional[str] = Field(None, alias='country')

    # The county, state, or region of the shipping address.
    state: typing.Optional[str] = Field(None, alias='state')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
