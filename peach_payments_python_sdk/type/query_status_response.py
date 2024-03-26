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

from peach_payments_python_sdk.type.checkout_state import CheckoutState
from peach_payments_python_sdk.type.customer import Customer
from peach_payments_python_sdk.type.payment_response_options import PaymentResponseOptions
from peach_payments_python_sdk.type.query_status_response_payment import QueryStatusResponsePayment
from peach_payments_python_sdk.type.query_status_response_terms_of_service import QueryStatusResponseTermsOfService

class RequiredQueryStatusResponse(TypedDict):
    pass

class OptionalQueryStatusResponse(TypedDict, total=False):
    # Payment ID.
    id: str

    payment: QueryStatusResponsePayment

    # Source of the payment link.
    source: str

    # Timestamp when the payment link was created.
    createdAt: str

    # Timestamp when the payment link was last modified.
    updatedAt: str

    customer: Customer

    options: PaymentResponseOptions

    checkout: CheckoutState

    termsOfService: QueryStatusResponseTermsOfService

class QueryStatusResponse(RequiredQueryStatusResponse, OptionalQueryStatusResponse):
    pass
