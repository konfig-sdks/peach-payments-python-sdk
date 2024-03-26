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

from peach_payments_python_sdk.type.entity_id import EntityId
from peach_payments_python_sdk.type.user_id import UserId

class RequiredAuthentication(TypedDict):
    userId: UserId

    # Authentication password.
    password: str

    entityId: EntityId

class OptionalAuthentication(TypedDict, total=False):
    pass

class Authentication(RequiredAuthentication, OptionalAuthentication):
    pass
