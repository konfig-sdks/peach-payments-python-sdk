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

from peach_payments_python_sdk.pydantic.mandate import Mandate

class Bank(BaseModel):
    # The bank account holder.
    holder: typing.Optional[str] = Field(None, alias='holder')

    # The name of the bank which holds the account.
    bank_name: typing.Optional[str] = Field(None, alias='bankName')

    # The bank account number.
    number: typing.Optional[str] = Field(None, alias='number')

    # The IBAN (International Bank Account Number) associated with the bank account.
    iban: typing.Optional[str] = Field(None, alias='iban')

    # The BIC (Bank Identifier Code (SWIFT)) of the bank account.
    bic: typing.Optional[str] = Field(None, alias='bic')

    # The code associated with the bank account.
    bank_code: typing.Optional[str] = Field(None, alias='bankCode')

    # The country code of the bank account (ISO 3166-1).
    country: typing.Optional[str] = Field(None, alias='country')

    mandate: typing.Optional[Mandate] = Field(None, alias='mandate')

    # The due date of the transaction of the direct debit.
    transaction_due_date: typing.Optional[str] = Field(None, alias='transactionDueDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
