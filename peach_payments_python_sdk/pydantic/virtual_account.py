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


class VirtualAccount(BaseModel):
    # The account ID.
    account_id: typing.Optional[str] = Field(None, alias='accountId')

    # The virtual account password.
    password: typing.Optional[str] = Field(None, alias='password')

    # The virtual account token.
    token: typing.Optional[str] = Field(None, alias='token')

    # The virtual account type.
    type: typing.Optional[Literal["CELLPHONE", "IDNUMBER", "ACCOUNTNUMBER"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
