# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from peach_payments_python_sdk.paths.root.post import Webhook
from peach_payments_python_sdk.apis.tags.payments_api_outbound_api_raw import PaymentsAPIOutboundApiRaw


class PaymentsAPIOutboundApi(
    Webhook,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PaymentsAPIOutboundApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PaymentsAPIOutboundApiRaw(api_client)
