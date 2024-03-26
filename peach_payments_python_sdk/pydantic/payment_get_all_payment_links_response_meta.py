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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class PaymentGetAllPaymentLinksResponseMeta(BaseModel):
    # The amount of items to retrieve.
    per_page: typing.Optional[typing.Union[int, float]] = Field(None, alias='perPage')

    # The offset from which to read data.
    offset: typing.Optional[typing.Union[int, float]] = Field(None, alias='offset')

    # The offset from which to read data on a subsequent request.
    next_offset: typing.Optional[typing.Union[int, float]] = Field(None, alias='nextOffset')

    # The total number of payment links returned by the filter criteria.
    total: typing.Optional[typing.Union[int, float]] = Field(None, alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
