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

from peach_payments_python_sdk.type.error400_result import Error400Result
from peach_payments_python_sdk.type.result_details import ResultDetails

class RequiredError400Response(TypedDict):
    result: Error400Result

    # The timestamp of the transaction.
    timestamp: datetime

class OptionalError400Response(TypedDict, total=False):
    resultDetails: ResultDetails

class Error400Response(RequiredError400Response, OptionalError400Response):
    pass
