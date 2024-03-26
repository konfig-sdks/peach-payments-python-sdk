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

from peach_payments_python_sdk.type.query_status_response import QueryStatusResponse
from peach_payments_python_sdk.type.status_query_payment_status_response_audit import StatusQueryPaymentStatusResponseAudit

class RequiredStatusQueryPaymentStatusResponse(TypedDict):
    pass

class OptionalStatusQueryPaymentStatusResponse(TypedDict, total=False):
    payment: QueryStatusResponse

    audit: StatusQueryPaymentStatusResponseAudit

class StatusQueryPaymentStatusResponse(RequiredStatusQueryPaymentStatusResponse, OptionalStatusQueryPaymentStatusResponse):
    pass
