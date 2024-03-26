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


class RequiredCustomerBrowser(TypedDict):
    pass

class OptionalCustomerBrowser(TypedDict, total=False):
    # The value of the accept header sent from the customer's browser.
    acceptHeader: str

    # The value representing the browser language as defined in IETF BCP47.
    language: str

    # The total height of the customer's screen in pixels.
    screenHeight: str

    # The total width of the customer's screen in pixels.
    screenWidth: str

    # The time-zone offset in minutes between UTC and the local time of the customer's browser.
    timezone: str

    # The exact content of the HTTP user-agent header.
    userAgent: str

    # The boolean that represents the ability of the customer's browser to execute Java.
    javaEnabled: str

    # The boolean that represents the ability of the customer's browser to execute JavaScript.
    javascriptEnabled: str

    # The value representing the bit depth of the colour palette for displaying images in bits per pixel.
    screenColorDepth: str

    # The dimensions of the challenge window that has been displayed to the customer.
    challengeWindow: str

class CustomerBrowser(RequiredCustomerBrowser, OptionalCustomerBrowser):
    pass
