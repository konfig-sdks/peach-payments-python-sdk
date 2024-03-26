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


class Mandate(BaseModel):
    # The date the direct debit mandate was signed.
    date_of_signature: typing.Optional[str] = Field(None, alias='dateOfSignature')

    # The ID of the direct debit mandate.
    id: typing.Optional[str] = Field(None, alias='id')

    # The mandate reference for direct debit as a contractual agreement between the creditor and the debtor.
    reference: typing.Optional[str] = Field(None, alias='reference')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
