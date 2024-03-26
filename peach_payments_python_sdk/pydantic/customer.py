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

if TYPE_CHECKING:
    from peach_payments_python_sdk.pydantic.address import Address
from peach_payments_python_sdk.pydantic.customer_browser import CustomerBrowser

class Customer(BaseModel):
    # The customer's first name or given name. Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries.
    given_name: str = Field(alias='givenName')

    # The customer's last name or surname. Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries.
    surname: typing.Optional[str] = Field(None, alias='surname')

    # The customer's email  address.
    email: typing.Optional[str] = Field(None, alias='email')

    # The customer's mobile phone number.
    mobile: typing.Optional[str] = Field(None, alias='mobile')

    # The customer's WhatsApp number. Required for communicating with customers regarding payment. Format should be +27123456789. Required if sendWhatsapp is true.
    whatsapp: typing.Optional[str] = Field(None, alias='whatsapp')

    billing: typing.Optional['Address'] = Field(None, alias='billing')

    # The customer's fax number, if provided.
    fax: typing.Optional[str] = Field(None, alias='fax')

    # The customer's phone number.
    phone: typing.Optional[str] = Field(None, alias='phone')

    # The customer's IP address.
    ip: typing.Optional[str] = Field(None, alias='ip')

    # The language used for the customer on the merchant's site.
    merchant_customer_language: typing.Optional[str] = Field(None, alias='merchantCustomerLanguage')

    # Used to determine if this is a new or returning customer.
    status: typing.Optional[str] = Field(None, alias='status')

    # The customer's ID on the merchant's site.
    merchant_customer_id: typing.Optional[str] = Field(None, alias='merchantCustomerId')

    # The customer's tax ID, if required.
    tax_id: typing.Optional[str] = Field(None, alias='taxId')

    # The customer's tax type, if required.
    tax_type: typing.Optional[str] = Field(None, alias='taxType')

    # The customer's birth date.
    birth_date: typing.Optional[str] = Field(None, alias='birthDate')

    browser: typing.Optional[CustomerBrowser] = Field(None, alias='browser')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
