# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from peach_payments_python_sdk.paths.api_payments_payment_id.delete import CancelLink
from peach_payments_python_sdk.paths.api_channels_entity_id_payments.post import GenerateLink
from peach_payments_python_sdk.paths.api_payments.get import GetAllPaymentLinks
from peach_payments_python_sdk.apis.tags.payment_api_raw import PaymentApiRaw


class PaymentApi(
    CancelLink,
    GenerateLink,
    GetAllPaymentLinks,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PaymentApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PaymentApiRaw(api_client)
