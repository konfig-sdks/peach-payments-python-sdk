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

from peach_payments_python_sdk.pydantic.checkout_options import CheckoutOptions
from peach_payments_python_sdk.pydantic.customer import Customer
from peach_payments_python_sdk.pydantic.generate_link_payment_payment import GenerateLinkPaymentPayment
from peach_payments_python_sdk.pydantic.payment_options import PaymentOptions

class GenerateLinkPayment(BaseModel):
    payment: GenerateLinkPaymentPayment = Field(alias='payment')

    customer: Customer = Field(alias='customer')

    options: PaymentOptions = Field(alias='options')

    checkout: CheckoutOptions = Field(alias='checkout')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
