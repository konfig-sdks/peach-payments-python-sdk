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


class CustomerBrowser(BaseModel):
    # The value of the accept header sent from the customer's browser.
    accept_header: typing.Optional[str] = Field(None, alias='acceptHeader')

    # The value representing the browser language as defined in IETF BCP47.
    language: typing.Optional[str] = Field(None, alias='language')

    # The total height of the customer's screen in pixels.
    screen_height: typing.Optional[str] = Field(None, alias='screenHeight')

    # The total width of the customer's screen in pixels.
    screen_width: typing.Optional[str] = Field(None, alias='screenWidth')

    # The time-zone offset in minutes between UTC and the local time of the customer's browser.
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # The exact content of the HTTP user-agent header.
    user_agent: typing.Optional[str] = Field(None, alias='userAgent')

    # The boolean that represents the ability of the customer's browser to execute Java.
    java_enabled: typing.Optional[str] = Field(None, alias='javaEnabled')

    # The boolean that represents the ability of the customer's browser to execute JavaScript.
    javascript_enabled: typing.Optional[str] = Field(None, alias='javascriptEnabled')

    # The value representing the bit depth of the colour palette for displaying images in bits per pixel.
    screen_color_depth: typing.Optional[str] = Field(None, alias='screenColorDepth')

    # The dimensions of the challenge window that has been displayed to the customer.
    challenge_window: typing.Optional[str] = Field(None, alias='challengeWindow')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
