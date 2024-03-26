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


class BatchGenerateLinkRequest(BaseModel):
    # The name of the CSV to be uploaded.
    filename: str = Field(alias='filename')

    # Webhooks are sent to this URL. It overrides the generic merchant webhook URL.
    notification_url: typing.Optional[typing.Optional[str]] = Field(None, alias='notificationUrl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
