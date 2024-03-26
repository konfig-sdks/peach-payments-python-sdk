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


class RequiredPaymentGetAllPaymentLinksResponseMeta(TypedDict):
    pass

class OptionalPaymentGetAllPaymentLinksResponseMeta(TypedDict, total=False):
    # The amount of items to retrieve.
    perPage: typing.Union[int, float]

    # The offset from which to read data.
    offset: typing.Union[int, float]

    # The offset from which to read data on a subsequent request.
    nextOffset: typing.Union[int, float]

    # The total number of payment links returned by the filter criteria.
    total: typing.Union[int, float]

class PaymentGetAllPaymentLinksResponseMeta(RequiredPaymentGetAllPaymentLinksResponseMeta, OptionalPaymentGetAllPaymentLinksResponseMeta):
    pass
