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


class BatchResponse(BaseModel):
    # Unique identifier for the payment attempt.
    id: str = Field(alias='id')

    # Timestamp when the batch link was created.
    created_at: str = Field(alias='createdAt')

    # Timestamp when the batch link was updated.
    updated_at: str = Field(alias='updatedAt')

    # The entity for the request.
    entity_id: str = Field(alias='entityId')

    # The name of the file that was uploaded.
    filename: str = Field(alias='filename')

    # Payment link status.
    status: Literal["initiated", "processing", "completed", "error"] = Field(alias='status')

    # The amount of successfully created payment links.
    successful_rows: typing.Union[int, float] = Field(alias='successfulRows')

    # The total amount of rows parsed from file.
    total_rows: typing.Union[int, float] = Field(alias='totalRows')

    # The error code will only be returned if the file fails to upload.
    error_code: typing.Optional[str] = Field(None, alias='errorCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
