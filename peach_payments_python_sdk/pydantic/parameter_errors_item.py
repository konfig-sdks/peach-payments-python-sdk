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


class ParameterErrorsItem(BaseModel):
    # The value of the parameter which failed validation. Can be any value - string, number, boolean, array, or object.
    value: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='value')

    # The name of the parameter.
    name: str = Field(alias='name')

    # A message describing the error.
    message: str = Field(alias='message')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
