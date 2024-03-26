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


class RequiredFilesUploadFileResponse(TypedDict):
    pass

class OptionalFilesUploadFileResponse(TypedDict, total=False):
    # A file ID that should be used in the files property on a create link call.
    fileId: str

class FilesUploadFileResponse(RequiredFilesUploadFileResponse, OptionalFilesUploadFileResponse):
    pass
