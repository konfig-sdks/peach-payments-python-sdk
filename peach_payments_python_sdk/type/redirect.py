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

from peach_payments_python_sdk.type.redirect_parameters import RedirectParameters

class RequiredRedirect(TypedDict):
    parameters: RedirectParameters

    # The URL that the shopper must be redirected to in order to proceed.
    url: str

    # REST method used for redirection.
    method: str

class OptionalRedirect(TypedDict, total=False):
    pass

class Redirect(RequiredRedirect, OptionalRedirect):
    pass
