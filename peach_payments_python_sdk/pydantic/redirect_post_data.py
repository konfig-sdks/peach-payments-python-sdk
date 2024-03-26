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


class RedirectPostData(BaseModel):
    # The checkout amount.
    amount: typing.Optional[str] = Field(None, alias='amount')

    checkout_id: typing.Optional[str] = Field(None, alias='checkoutId')

    # The currency code of the payment request amount.
    currency: typing.Optional[Literal["ZAR", "USD", "KES", "MUR", "GBP", "EUR"]] = Field(None, alias='currency')

    # The merchant transaction ID set when creating the checkout.
    merchant_transaction_id: typing.Optional[str] = Field(None, alias='merchantTransactionId')

    payment_type: typing.Optional[Literal["DB"]] = Field(None, alias='paymentType')

    # A code representing the transaction state.
    result.code_: typing.Optional[str] = Field(None, alias='result.code')

    # A friendly message.
    result.description_: typing.Optional[str] = Field(None, alias='result.description')

    # Date and time when the checkout was created.
    timestamp: typing.Optional[str] = Field(None, alias='timestamp')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
