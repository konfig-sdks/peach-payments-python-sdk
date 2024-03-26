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

from peach_payments_python_sdk.type.amount import Amount
from peach_payments_python_sdk.type.cart_cart_items import CartCartItems

class RequiredCart(TypedDict):
    pass

class OptionalCart(TypedDict, total=False):
    cartItems: CartCartItems

    # The tax percentage or amount applied to the price of the items in the shopping cart.
    tax: str

    shippingAmount: Amount

    # The discount percentage applied to the price of the items in the shopping cart.
    discount: str

class Cart(RequiredCart, OptionalCart):
    pass
