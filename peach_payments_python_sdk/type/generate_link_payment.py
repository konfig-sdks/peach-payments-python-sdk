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

from peach_payments_python_sdk.type.checkout_options import CheckoutOptions
from peach_payments_python_sdk.type.customer import Customer
from peach_payments_python_sdk.type.generate_link_payment_payment import GenerateLinkPaymentPayment
from peach_payments_python_sdk.type.payment_options import PaymentOptions

class RequiredGenerateLinkPayment(TypedDict):
    payment: GenerateLinkPaymentPayment

    customer: Customer

    options: PaymentOptions

    checkout: CheckoutOptions

class OptionalGenerateLinkPayment(TypedDict, total=False):
    pass

class GenerateLinkPayment(RequiredGenerateLinkPayment, OptionalGenerateLinkPayment):
    pass
