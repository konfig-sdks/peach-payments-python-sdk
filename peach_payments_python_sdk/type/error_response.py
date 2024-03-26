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
from peach_payments_python_sdk.type.payment_brand import PaymentBrand
from peach_payments_python_sdk.type.payment_type import PaymentType
from peach_payments_python_sdk.type.result import Result
from peach_payments_python_sdk.type.result_details import ResultDetails
from peach_payments_python_sdk.type.unique_id import UniqueId

class RequiredErrorResponse(TypedDict):
    result: Result

    # The timestamp of the transaction.
    timestamp: datetime

class OptionalErrorResponse(TypedDict, total=False):
    resultDetails: ResultDetails

    id: UniqueId

    paymentType: PaymentType

    paymentBrand: PaymentBrand

    # A JSON object depicting custom information sent by the merchant. Echoed back in the response.
    customParameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    amount: Amount

    currency: Currency

class ErrorResponse(RequiredErrorResponse, OptionalErrorResponse):
    pass
