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

from peach_payments_python_sdk.type.address import Address
from peach_payments_python_sdk.type.amount import Amount
from peach_payments_python_sdk.type.authentication import Authentication
from peach_payments_python_sdk.type.cart import Cart
from peach_payments_python_sdk.type.currency import Currency
from peach_payments_python_sdk.type.customer import Customer
from peach_payments_python_sdk.type.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.type.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.type.payment_brand import PaymentBrand
from peach_payments_python_sdk.type.payment_type import PaymentType
from peach_payments_python_sdk.type.shopify import Shopify
from peach_payments_python_sdk.type.virtual_account import VirtualAccount

class RequiredPaymentRequest(TypedDict):
    authentication: Authentication

    merchantTransactionId: MerchantTransactionId

    amount: Amount

    currency: Currency

    paymentBrand: PaymentBrand

    paymentType: PaymentType

class OptionalPaymentRequest(TypedDict, total=False):
    virtualAccount: VirtualAccount

    shipping: Address

    billing: Address

    shopify: Shopify

    customer: Customer

    cart: Cart

    merchantInvoiceId: MerchantInvoiceId

    # The Payments API redirects the user to this URL after processing the payment request.
    shopperResultUrl: str

class PaymentRequest(RequiredPaymentRequest, OptionalPaymentRequest):
    pass
