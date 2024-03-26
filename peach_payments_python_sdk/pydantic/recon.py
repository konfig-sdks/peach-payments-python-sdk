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


class Recon(BaseModel):
    # The payment service provider merchant number.
    ci_merchant_number: typing.Optional[str] = Field(None, alias='ciMerchantNumber')

    # The reconciliation reference number from the payment service provider.
    rrn: typing.Optional[str] = Field(None, alias='rrn')

    # The authorisation code from the payment service provider.
    auth_code: typing.Optional[str] = Field(None, alias='authCode')

    # The result code from the payment service provider.
    result_code: typing.Optional[str] = Field(None, alias='resultCode')

    # The STAN reference number from the payment service provider.
    stan: typing.Optional[str] = Field(None, alias='stan')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
