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

from peach_payments_python_sdk.pydantic.amount import Amount
from peach_payments_python_sdk.pydantic.cart_cart_items import CartCartItems

class Cart(BaseModel):
    cart_items: typing.Optional[CartCartItems] = Field(None, alias='cartItems')

    # The tax percentage or amount applied to the price of the items in the shopping cart.
    tax: typing.Optional[str] = Field(None, alias='tax')

    shipping_amount: typing.Optional[Amount] = Field(None, alias='shippingAmount')

    # The discount percentage applied to the price of the items in the shopping cart.
    discount: typing.Optional[str] = Field(None, alias='discount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
