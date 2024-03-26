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

from peach_payments_python_sdk.pydantic.checkout_v2_billing import CheckoutV2Billing
from peach_payments_python_sdk.pydantic.checkout_v2_custom_parameters import CheckoutV2CustomParameters
from peach_payments_python_sdk.pydantic.checkout_v2_customer import CheckoutV2Customer
from peach_payments_python_sdk.pydantic.checkout_v2_shipping import CheckoutV2Shipping

class CheckoutV2(BaseModel):
    # The entity for the request. By default, this is the channel ID.
    authentication.entity_id_: str = Field(alias='authentication.entityId')

    # Merchant-provided reference number unique for your transactions.
    merchant_transaction_id: str = Field(alias='merchantTransactionId')

    # The amount of the payment request. The period is used as the decimal separator.  M-PESA does not support decimal amounts, so Checkout automatically rounds them up. 
    amount: typing.Union[int, float] = Field(alias='amount')

    # The currency code of the payment request amount.
    currency: Literal["ZAR", "USD", "KES", "MUR", "GBP", "EUR"] = Field(alias='currency')

    # Unique value to represent each request.
    nonce: str = Field(alias='nonce')

    # Checkout uses a POST request to redirect the customer to this URL after the customer completes checkout. Must be a valid URL that can be accessed through a browser.
    shopper_result_url: str = Field(alias='shopperResultUrl')

    # The preferred payment method which is active in the checkout page at the point of redirecting.
    default_payment_method: typing.Optional[Literal["CARD", "MASTERPASS", "MOBICRED", "EFTSECURE", "MPESA", "1FORYOU", "APLUS", "PAYPAL", "ZEROPAY", "PAYFLEX", "FINCHOICEPAY", "BLINKBYEMTEL", "CAPITECPAY", "NEDBANKDIRECTEFT", "PAYBYBANK", "MCBJUICE"]] = Field(None, alias='defaultPaymentMethod')

    # Force the default payment method to be the only payment method.
    force_default_method: typing.Optional[bool] = Field(None, alias='forceDefaultMethod')

    # Merchant-provided invoice number unique for your transactions. This identifier is not sent onwards.
    merchant_invoice_id: typing.Optional[str] = Field(None, alias='merchantInvoiceId')

    # The customer is redirected to this URL if they cancel checkout. It must be a valid URL that can be reached through a browser.
    cancel_url: typing.Optional[str] = Field(None, alias='cancelUrl')

    # Override the preconfigured webhook URL for this checkout instance, any changes to checkout send a webhook to this URL.
    notification_url: typing.Optional[str] = Field(None, alias='notificationUrl')

    custom_parameters: typing.Optional[CheckoutV2CustomParameters] = Field(None, alias='customParameters')

    customer: typing.Optional[CheckoutV2Customer] = Field(None, alias='customer')

    billing: typing.Optional[CheckoutV2Billing] = Field(None, alias='billing')

    shipping: typing.Optional[CheckoutV2Shipping] = Field(None, alias='shipping')

    # Used to enable card tokenisation with COPYandPAY.
    create_registration: typing.Optional[bool] = Field(None, alias='createRegistration')

    # Used to provide a name for the application that is creating the checkout instance.
    originator: typing.Optional[str] = Field(None, alias='originator')

    # Text to display on \"Return to Store\" button on completing checkout.
    return_to: typing.Optional[Literal["STORE", "INVOICE"]] = Field(None, alias='returnTo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
