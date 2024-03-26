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

from peach_payments_python_sdk.pydantic.merchant_transaction_id_status_response_payments import MerchantTransactionIdStatusResponsePayments
from peach_payments_python_sdk.pydantic.result import Result

class MerchantTransactionIdStatusResponse(BaseModel):
    result: Result = Field(alias='result')

    # The timestamp of the transaction.
    timestamp: datetime = Field(alias='timestamp')

    payments: MerchantTransactionIdStatusResponsePayments = Field(alias='payments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
