# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from peach_payments_python_sdk.paths.merchant_specs.post import GetPaymentMethods
from peach_payments_python_sdk.apis.tags.helpers_api_raw import HelpersApiRaw


class HelpersApi(
    GetPaymentMethods,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: HelpersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = HelpersApiRaw(api_client)
