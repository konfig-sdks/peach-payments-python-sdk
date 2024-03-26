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


class QueryStatusResponseTermsOfService(BaseModel):
    # The id of the terms of service that was agreed to.
    id: typing.Optional[str] = Field(None, alias='id')

    # Whether the user agreed to the terms of service.
    accepted: typing.Optional[bool] = Field(None, alias='accepted')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
