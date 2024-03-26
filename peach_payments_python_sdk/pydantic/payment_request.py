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

from peach_payments_python_sdk.pydantic.address import Address
from peach_payments_python_sdk.pydantic.amount import Amount
from peach_payments_python_sdk.pydantic.authentication import Authentication
from peach_payments_python_sdk.pydantic.cart import Cart
from peach_payments_python_sdk.pydantic.currency import Currency
from peach_payments_python_sdk.pydantic.customer import Customer
from peach_payments_python_sdk.pydantic.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.pydantic.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.pydantic.payment_brand import PaymentBrand
from peach_payments_python_sdk.pydantic.payment_type import PaymentType
from peach_payments_python_sdk.pydantic.shopify import Shopify
from peach_payments_python_sdk.pydantic.virtual_account import VirtualAccount

class PaymentRequest(BaseModel):
    authentication: Authentication = Field(alias='authentication')

    merchant_transaction_id: MerchantTransactionId = Field(alias='merchantTransactionId')

    amount: Amount = Field(alias='amount')

    currency: Currency = Field(alias='currency')

    payment_brand: PaymentBrand = Field(alias='paymentBrand')

    payment_type: PaymentType = Field(alias='paymentType')

    virtual_account: typing.Optional[VirtualAccount] = Field(None, alias='virtualAccount')

    shipping: typing.Optional[Address] = Field(None, alias='shipping')

    billing: typing.Optional[Address] = Field(None, alias='billing')

    shopify: typing.Optional[Shopify] = Field(None, alias='shopify')

    customer: typing.Optional[Customer] = Field(None, alias='customer')

    cart: typing.Optional[Cart] = Field(None, alias='cart')

    merchant_invoice_id: typing.Optional[MerchantInvoiceId] = Field(None, alias='merchantInvoiceId')

    # The Payments API redirects the user to this URL after processing the payment request.
    shopper_result_url: typing.Optional[str] = Field(None, alias='shopperResultUrl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
