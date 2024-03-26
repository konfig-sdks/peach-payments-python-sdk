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

from peach_payments_python_sdk.pydantic.checkout_state import CheckoutState
from peach_payments_python_sdk.pydantic.customer import Customer
from peach_payments_python_sdk.pydantic.payment_response_options import PaymentResponseOptions
from peach_payments_python_sdk.pydantic.query_status_response_payment import QueryStatusResponsePayment
from peach_payments_python_sdk.pydantic.query_status_response_terms_of_service import QueryStatusResponseTermsOfService

class QueryStatusResponse(BaseModel):
    # Payment ID.
    id: typing.Optional[str] = Field(None, alias='id')

    payment: typing.Optional[QueryStatusResponsePayment] = Field(None, alias='payment')

    # Source of the payment link.
    source: typing.Optional[Literal["API", "Xero", "UI"]] = Field(None, alias='source')

    # Timestamp when the payment link was created.
    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    # Timestamp when the payment link was last modified.
    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    customer: typing.Optional[Customer] = Field(None, alias='customer')

    options: typing.Optional[PaymentResponseOptions] = Field(None, alias='options')

    checkout: typing.Optional[CheckoutState] = Field(None, alias='checkout')

    terms_of_service: typing.Optional[QueryStatusResponseTermsOfService] = Field(None, alias='termsOfService')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
