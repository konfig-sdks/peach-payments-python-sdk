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

from peach_payments_python_sdk.pydantic.amount import Amount
from peach_payments_python_sdk.pydantic.currency import Currency
from peach_payments_python_sdk.pydantic.payment_brand import PaymentBrand
from peach_payments_python_sdk.pydantic.payment_type import PaymentType
from peach_payments_python_sdk.pydantic.result import Result
from peach_payments_python_sdk.pydantic.result_details import ResultDetails
from peach_payments_python_sdk.pydantic.unique_id import UniqueId

class ErrorResponse(BaseModel):
    result: Result = Field(alias='result')

    # The timestamp of the transaction.
    timestamp: datetime = Field(alias='timestamp')

    result_details: typing.Optional[ResultDetails] = Field(None, alias='resultDetails')

    id: typing.Optional[UniqueId] = Field(None, alias='id')

    payment_type: typing.Optional[PaymentType] = Field(None, alias='paymentType')

    payment_brand: typing.Optional[PaymentBrand] = Field(None, alias='paymentBrand')

    # A JSON object depicting custom information sent by the merchant. Echoed back in the response.
    custom_parameters: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='customParameters')

    amount: typing.Optional[Amount] = Field(None, alias='amount')

    currency: typing.Optional[Currency] = Field(None, alias='currency')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
