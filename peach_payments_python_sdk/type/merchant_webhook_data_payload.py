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

from peach_payments_python_sdk.type.address import Address
from peach_payments_python_sdk.type.amount import Amount
from peach_payments_python_sdk.type.card import Card
from peach_payments_python_sdk.type.connector_tx_id1 import ConnectorTxID1
from peach_payments_python_sdk.type.currency import Currency
from peach_payments_python_sdk.type.customer import Customer
from peach_payments_python_sdk.type.merchant_account_id import MerchantAccountId
from peach_payments_python_sdk.type.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.type.merchant_webhook_data_payload_authentication import MerchantWebhookDataPayloadAuthentication
from peach_payments_python_sdk.type.merchant_webhook_data_payload_merchant import MerchantWebhookDataPayloadMerchant
from peach_payments_python_sdk.type.payment_type import PaymentType
from peach_payments_python_sdk.type.recon import Recon
from peach_payments_python_sdk.type.result import Result
from peach_payments_python_sdk.type.result_details import ResultDetails
from peach_payments_python_sdk.type.shopify import Shopify
from peach_payments_python_sdk.type.unique_id import UniqueId

class RequiredMerchantWebhookDataPayload(TypedDict):
    id: UniqueId

    paymentType: PaymentType

    amount: Amount

    merchantInvoiceId: MerchantInvoiceId

    merchantAccountId: MerchantAccountId

    currency: Currency

    presentationAmount: Amount

    result: Result

    resultDetails: ResultDetails

    connectorTxID1: ConnectorTxID1

    authentication: MerchantWebhookDataPayloadAuthentication

    card: Card

    # The timestamp of the transaction.
    timestamp: datetime

    shipping: Address

    billing: Address

    # Bank account data.
    bankAccount: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    referenceId: UniqueId

    shopify: Shopify

class OptionalMerchantWebhookDataPayload(TypedDict, total=False):
    descriptor: str

    customer: Customer

    recon: Recon

    # A JSON object depicting custom information sent by the merchant. Echoed back in the response.
    customParameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    merchant: MerchantWebhookDataPayloadMerchant

class MerchantWebhookDataPayload(RequiredMerchantWebhookDataPayload, OptionalMerchantWebhookDataPayload):
    pass
