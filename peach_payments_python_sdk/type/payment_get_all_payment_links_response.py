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

from peach_payments_python_sdk.type.payment_get_all_payment_links_response_meta import PaymentGetAllPaymentLinksResponseMeta
from peach_payments_python_sdk.type.query_status_response import QueryStatusResponse

class RequiredPaymentGetAllPaymentLinksResponse(TypedDict):
    pass

class OptionalPaymentGetAllPaymentLinksResponse(TypedDict, total=False):
    payments: typing.List[QueryStatusResponse]

    meta: PaymentGetAllPaymentLinksResponseMeta

class PaymentGetAllPaymentLinksResponse(RequiredPaymentGetAllPaymentLinksResponse, OptionalPaymentGetAllPaymentLinksResponse):
    pass
