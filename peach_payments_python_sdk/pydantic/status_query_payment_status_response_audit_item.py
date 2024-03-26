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


class StatusQueryPaymentStatusResponseAuditItem(BaseModel):
    # The previous status of the payment link.
    old_status: typing.Optional[Literal["none", "initiated", "processing", "expired", "cancelled", "completed"]] = Field(None, alias='oldStatus')

    # The new status of the payment link.
    new_status: typing.Optional[Literal["initiated", "processing", "expired", "cancelled", "completed"]] = Field(None, alias='newStatus')

    # The UTC time that the status changed.
    timestamp: typing.Optional[str] = Field(None, alias='timestamp')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
