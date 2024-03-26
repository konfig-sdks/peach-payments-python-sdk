# coding: utf-8

# flake8: noqa

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

__version__ = "2.0.0"

# import ApiClient
from peach_payments_python_sdk.api_client import ApiClient

# import Configuration
from peach_payments_python_sdk.configuration import Configuration

# import exceptions
from peach_payments_python_sdk.exceptions import OpenApiException
from peach_payments_python_sdk.exceptions import ApiAttributeError
from peach_payments_python_sdk.exceptions import ApiTypeError
from peach_payments_python_sdk.exceptions import ApiValueError
from peach_payments_python_sdk.exceptions import ApiKeyError
from peach_payments_python_sdk.exceptions import ApiException

from peach_payments_python_sdk.client import PeachPayments
