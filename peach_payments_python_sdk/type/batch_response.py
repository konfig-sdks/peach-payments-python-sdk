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


class RequiredBatchResponse(TypedDict):
    # Unique identifier for the payment attempt.
    id: str

    # Timestamp when the batch link was created.
    createdAt: str

    # Timestamp when the batch link was updated.
    updatedAt: str

    # The entity for the request.
    entityId: str

    # The name of the file that was uploaded.
    filename: str

    # Payment link status.
    status: str

    # The amount of successfully created payment links.
    successfulRows: typing.Union[int, float]

    # The total amount of rows parsed from file.
    totalRows: typing.Union[int, float]

class OptionalBatchResponse(TypedDict, total=False):
    # The error code will only be returned if the file fails to upload.
    errorCode: str

class BatchResponse(RequiredBatchResponse, OptionalBatchResponse):
    pass
