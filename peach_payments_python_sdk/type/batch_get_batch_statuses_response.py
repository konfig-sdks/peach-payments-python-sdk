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

from peach_payments_python_sdk.type.batch_get_batch_statuses_response_meta import BatchGetBatchStatusesResponseMeta

class RequiredBatchGetBatchStatusesResponse(TypedDict):
    pass

class OptionalBatchGetBatchStatusesResponse(TypedDict, total=False):
    batches: typing.List[BatchResponse]

    meta: BatchGetBatchStatusesResponseMeta

class BatchGetBatchStatusesResponse(RequiredBatchGetBatchStatusesResponse, OptionalBatchGetBatchStatusesResponse):
    pass
