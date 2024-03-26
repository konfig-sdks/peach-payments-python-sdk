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

from peach_payments_python_sdk.type.amount import Amount
from peach_payments_python_sdk.type.bank import Bank
from peach_payments_python_sdk.type.connector_tx_id1 import ConnectorTxID1
from peach_payments_python_sdk.type.currency import Currency
from peach_payments_python_sdk.type.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.type.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.type.payment_brand import PaymentBrand
from peach_payments_python_sdk.type.payment_type import PaymentType
from peach_payments_python_sdk.type.recon import Recon
from peach_payments_python_sdk.type.response_card import ResponseCard
from peach_payments_python_sdk.type.result import Result
from peach_payments_python_sdk.type.result_details import ResultDetails
from peach_payments_python_sdk.type.unique_id import UniqueId

class RequiredTransactionIdStatusResponse(TypedDict):
    id: UniqueId

    merchantTransactionId: MerchantTransactionId

    amount: Amount

    currency: Currency

    paymentBrand: PaymentBrand

    paymentType: PaymentType

    result: Result

    connectorTxID1: ConnectorTxID1

    # The timestamp of the transaction.
    timestamp: datetime

    # A JSON object depicting custom information sent by the merchant. Echoed back in the response.
    customParameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalTransactionIdStatusResponse(TypedDict, total=False):
    resultDetails: ResultDetails

    merchantInvoiceId: MerchantInvoiceId

    bank: Bank

    card: ResponseCard

    recon: Recon

class TransactionIdStatusResponse(RequiredTransactionIdStatusResponse, OptionalTransactionIdStatusResponse):
    pass
