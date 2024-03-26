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


class CartCartItemsItem(BaseModel):
    # The description of the item in the shopping cart.
    description: typing.Optional[str] = Field(None, alias='description')

    # The name of the item in the shopping cart.
    name: typing.Optional[str] = Field(None, alias='name')

    # The unique identifier of the item in the shopping cart.
    merchant_item_id: typing.Optional[str] = Field(None, alias='merchantItemId')

    # The number of items in the shopping cart.
    quantity: typing.Optional[int] = Field(None, alias='quantity')

    # The price of the item in the shopping cart.
    price: typing.Optional[str] = Field(None, alias='price')

    # The weight (in kg) of the item in the shopping cart.
    weight_in_kg: typing.Optional[typing.Union[int, float]] = Field(None, alias='weightInKg')

    # The category of the item in the shopping cart.
    category: typing.Optional[str] = Field(None, alias='category')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
