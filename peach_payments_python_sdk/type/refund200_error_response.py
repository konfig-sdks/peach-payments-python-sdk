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
from peach_payments_python_sdk.type.currency import Currency
from peach_payments_python_sdk.type.refund_payment_type import RefundPaymentType
from peach_payments_python_sdk.type.result import Result
from peach_payments_python_sdk.type.unique_id import UniqueId

class RequiredRefund200ErrorResponse(TypedDict):
    id: UniqueId

    amount: Amount

    currency: Currency

    paymentType: RefundPaymentType

    result: Result

    # The timestamp of the transaction.
    timestamp: datetime

class OptionalRefund200ErrorResponse(TypedDict, total=False):
    pass

class Refund200ErrorResponse(RequiredRefund200ErrorResponse, OptionalRefund200ErrorResponse):
    pass
