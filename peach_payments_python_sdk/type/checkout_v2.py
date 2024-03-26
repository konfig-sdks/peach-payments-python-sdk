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

from peach_payments_python_sdk.type.checkout_v2_billing import CheckoutV2Billing
from peach_payments_python_sdk.type.checkout_v2_custom_parameters import CheckoutV2CustomParameters
from peach_payments_python_sdk.type.checkout_v2_customer import CheckoutV2Customer
from peach_payments_python_sdk.type.checkout_v2_shipping import CheckoutV2Shipping

RequiredCheckoutV2 = TypedDict("RequiredCheckoutV2", {
    # The entity for the request. By default, this is the channel ID.
    "authentication.entityId": str,

    # Merchant-provided reference number unique for your transactions.
    "merchantTransactionId": str,

    # The amount of the payment request. The period is used as the decimal separator.  M-PESA does not support decimal amounts, so Checkout automatically rounds them up. 
    "amount": typing.Union[int, float],

    # The currency code of the payment request amount.
    "currency": str,

    # Unique value to represent each request.
    "nonce": str,

    # Checkout uses a POST request to redirect the customer to this URL after the customer completes checkout. Must be a valid URL that can be accessed through a browser.
    "shopperResultUrl": str,
    })

OptionalCheckoutV2 = TypedDict("OptionalCheckoutV2", {
    # The preferred payment method which is active in the checkout page at the point of redirecting.
    "defaultPaymentMethod": str,

    # Force the default payment method to be the only payment method.
    "forceDefaultMethod": bool,

    # Merchant-provided invoice number unique for your transactions. This identifier is not sent onwards.
    "merchantInvoiceId": str,

    # The customer is redirected to this URL if they cancel checkout. It must be a valid URL that can be reached through a browser.
    "cancelUrl": str,

    # Override the preconfigured webhook URL for this checkout instance, any changes to checkout send a webhook to this URL.
    "notificationUrl": str,

    "customParameters": CheckoutV2CustomParameters,

    "customer": CheckoutV2Customer,

    "billing": CheckoutV2Billing,

    "shipping": CheckoutV2Shipping,

    # Used to enable card tokenisation with COPYandPAY.
    "createRegistration": bool,

    # Used to provide a name for the application that is creating the checkout instance.
    "originator": str,

    # Text to display on \"Return to Store\" button on completing checkout.
    "returnTo": str,
    }, total=False)

class CheckoutV2(RequiredCheckoutV2, OptionalCheckoutV2):
    pass
