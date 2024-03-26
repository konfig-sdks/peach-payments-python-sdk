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


class RequiredCheckoutV2Customer(TypedDict):
    pass

class OptionalCheckoutV2Customer(TypedDict, total=False):
    # An identifier for this customer. Typically this is the ID that identifies the shopper in the shop's system.
    merchantCustomerId: str

    # The customer's first name or given name. Required if you send in any other customer parameters, also required for some risk checks and payment providers. Truncated after 48 characters.  Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries. 
    givenName: str

    # The customer's last name or surname. Required if you send in any other customer parameters, also required for some risk checks and payment providers. Truncated after 48 characters.  Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries. 
    surname: str

    # The customer's mobile number.
    mobile: str

    # The customer's email address.
    email: str

    # The customer's ID number, required for high-risk merchants supporting Capitec Pay.
    idNumber: str

class CheckoutV2Customer(RequiredCheckoutV2Customer, OptionalCheckoutV2Customer):
    pass
