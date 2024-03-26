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
from peach_payments_python_sdk.pydantic.authentication import Authentication
from peach_payments_python_sdk.pydantic.currency import Currency
from peach_payments_python_sdk.pydantic.refund_payment_type import RefundPaymentType

class RefundRequest(BaseModel):
    authentication: Authentication = Field(alias='authentication')

    amount: Amount = Field(alias='amount')

    currency: Currency = Field(alias='currency')

    payment_type: RefundPaymentType = Field(alias='paymentType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
