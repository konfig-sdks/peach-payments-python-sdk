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


class CheckoutV2Customer(BaseModel):
    # An identifier for this customer. Typically this is the ID that identifies the shopper in the shop's system.
    merchant_customer_id: typing.Optional[str] = Field(None, alias='merchantCustomerId')

    # The customer's first name or given name. Required if you send in any other customer parameters, also required for some risk checks and payment providers. Truncated after 48 characters.  Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries. 
    given_name: typing.Optional[str] = Field(None, alias='givenName')

    # The customer's last name or surname. Required if you send in any other customer parameters, also required for some risk checks and payment providers. Truncated after 48 characters.  Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries. 
    surname: typing.Optional[str] = Field(None, alias='surname')

    # The customer's mobile number.
    mobile: typing.Optional[str] = Field(None, alias='mobile')

    # The customer's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # The customer's ID number, required for high-risk merchants supporting Capitec Pay.
    id_number: typing.Optional[str] = Field(None, alias='idNumber')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
