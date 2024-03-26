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


RequiredCheckoutBaseWebhook = TypedDict("RequiredCheckoutBaseWebhook", {
    })

OptionalCheckoutBaseWebhook = TypedDict("OptionalCheckoutBaseWebhook", {
    # The amount of the payment request. The period is used as the decimal separator. M-PESA does not support decimal amounts, so Checkout automatically rounds them up.
    "amount": str,

    # Checkout ID.
    "checkoutId": str,

    # The currency code of the payment request amount.
    "currency": str,

    # Merchant-provided reference number unique for your transactions.
    "merchantTransactionId": str,

    # The payment type for the request.
    "paymentType": str,

    # A code representing the checkout state.
    "result.code": str,

    # A friendly message.
    "result.description": str,

    # Token to verify the integrity of the webhook, ensuring the request is coming from Checkout.
    "signature": str,

    # Date and time when the webhook was sent.
    "timestamp": str,
    }, total=False)

class CheckoutBaseWebhook(RequiredCheckoutBaseWebhook, OptionalCheckoutBaseWebhook):
    pass
