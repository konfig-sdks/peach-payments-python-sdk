# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from peach_payments_python_sdk.paths.checkout.post import InitiatePaymentRaw
from peach_payments_python_sdk.paths.checkout_initiate.post import InitiateRedirectCheckoutRaw
from peach_payments_python_sdk.paths.checkout_validate.post import ValidateRequestRaw


class CheckoutGenerationApiRaw(
    InitiatePaymentRaw,
    InitiateRedirectCheckoutRaw,
    ValidateRequestRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
