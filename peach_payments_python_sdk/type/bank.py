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

from peach_payments_python_sdk.type.mandate import Mandate

class RequiredBank(TypedDict):
    pass

class OptionalBank(TypedDict, total=False):
    # The bank account holder.
    holder: str

    # The name of the bank which holds the account.
    bankName: str

    # The bank account number.
    number: str

    # The IBAN (International Bank Account Number) associated with the bank account.
    iban: str

    # The BIC (Bank Identifier Code (SWIFT)) of the bank account.
    bic: str

    # The code associated with the bank account.
    bankCode: str

    # The country code of the bank account (ISO 3166-1).
    country: str

    mandate: Mandate

    # The due date of the transaction of the direct debit.
    transactionDueDate: str

class Bank(RequiredBank, OptionalBank):
    pass
