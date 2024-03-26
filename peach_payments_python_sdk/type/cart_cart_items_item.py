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


class RequiredCartCartItemsItem(TypedDict):
    pass

class OptionalCartCartItemsItem(TypedDict, total=False):
    # The description of the item in the shopping cart.
    description: str

    # The name of the item in the shopping cart.
    name: str

    # The unique identifier of the item in the shopping cart.
    merchantItemId: str

    # The number of items in the shopping cart.
    quantity: int

    # The price of the item in the shopping cart.
    price: str

    # The weight (in kg) of the item in the shopping cart.
    weightInKg: typing.Union[int, float]

    # The category of the item in the shopping cart.
    category: str

class CartCartItemsItem(RequiredCartCartItemsItem, OptionalCartCartItemsItem):
    pass
