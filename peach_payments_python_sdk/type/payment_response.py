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
from peach_payments_python_sdk.type.connector_tx_id1 import ConnectorTxID1
from peach_payments_python_sdk.type.connector_tx_id2 import ConnectorTxID2
from peach_payments_python_sdk.type.currency import Currency
from peach_payments_python_sdk.type.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.type.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.type.payment_brand import PaymentBrand
from peach_payments_python_sdk.type.payment_type import PaymentType
from peach_payments_python_sdk.type.redirect import Redirect
from peach_payments_python_sdk.type.result import Result
from peach_payments_python_sdk.type.result_details import ResultDetails
from peach_payments_python_sdk.type.unique_id import UniqueId
from peach_payments_python_sdk.type.virtual_account import VirtualAccount

class RequiredPaymentResponse(TypedDict):
    amount: Amount

    currency: Currency

    paymentBrand: PaymentBrand

    paymentType: PaymentType

    result: Result

    # A JSON object depicting custom information sent by the merchant. Echoed back in the response.
    customParameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The timestamp of the transaction.
    timestamp: datetime

    id: UniqueId

class OptionalPaymentResponse(TypedDict, total=False):
    resultDetails: ResultDetails

    redirect: Redirect

    connectorTxID1: ConnectorTxID1

    connectorTxID2: ConnectorTxID2

    merchantTransactionId: MerchantTransactionId

    merchantInvoiceId: MerchantInvoiceId

    # The Payments API redirects the user to this URL after processing the payment request.
    shopperResultUrl: str

    virtualAccount: VirtualAccount

    # The expiry timestamp of the transaction.
    transactionExpiryTimestamp: datetime

class PaymentResponse(RequiredPaymentResponse, OptionalPaymentResponse):
    pass
