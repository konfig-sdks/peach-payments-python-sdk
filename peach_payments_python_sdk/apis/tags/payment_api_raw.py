# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from peach_payments_python_sdk.paths.api_payments_payment_id.delete import CancelLinkRaw
from peach_payments_python_sdk.paths.api_channels_entity_id_payments.post import GenerateLinkRaw
from peach_payments_python_sdk.paths.api_payments.get import GetAllPaymentLinksRaw


class PaymentApiRaw(
    CancelLinkRaw,
    GenerateLinkRaw,
    GetAllPaymentLinksRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
