# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from peach_payments_python_sdk import schemas  # noqa: F401


class Code(
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The unique code that indicates the result status of the request.
    """


    class MetaOapg:
        regex=[{
            'pattern': r'^([0-9]{3}.[0-9]{3}.[0-9]{3})$',
        }]
