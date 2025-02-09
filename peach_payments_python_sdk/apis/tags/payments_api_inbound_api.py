# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from peach_payments_python_sdk.paths.payments.post import InitiateDebitTransaction
from peach_payments_python_sdk.paths.payments_unique_id.get import QueryTransactionById
from peach_payments_python_sdk.paths.payments_unique_id.post import RefundTransaction
from peach_payments_python_sdk.paths.payments.get import Status
from peach_payments_python_sdk.apis.tags.payments_api_inbound_api_raw import PaymentsAPIInboundApiRaw


class PaymentsAPIInboundApi(
    InitiateDebitTransaction,
    QueryTransactionById,
    RefundTransaction,
    Status,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PaymentsAPIInboundApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PaymentsAPIInboundApiRaw(api_client)
