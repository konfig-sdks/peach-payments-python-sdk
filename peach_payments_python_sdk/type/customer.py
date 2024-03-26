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

if TYPE_CHECKING:
    from peach_payments_python_sdk.type.address import Address
from peach_payments_python_sdk.type.customer_browser import CustomerBrowser

class RequiredCustomer(TypedDict):
    # The customer's first name or given name. Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries.
    givenName: str

class OptionalCustomer(TypedDict, total=False):
    # The customer's last name or surname. Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries.
    surname: str

    # The customer's email  address.
    email: str

    # The customer's mobile phone number.
    mobile: str

    # The customer's WhatsApp number. Required for communicating with customers regarding payment. Format should be +27123456789. Required if sendWhatsapp is true.
    whatsapp: str

    billing: 'Address'

    # The customer's fax number, if provided.
    fax: str

    # The customer's phone number.
    phone: str

    # The customer's IP address.
    ip: str

    # The language used for the customer on the merchant's site.
    merchantCustomerLanguage: str

    # Used to determine if this is a new or returning customer.
    status: str

    # The customer's ID on the merchant's site.
    merchantCustomerId: str

    # The customer's tax ID, if required.
    taxId: str

    # The customer's tax type, if required.
    taxType: str

    # The customer's birth date.
    birthDate: str

    browser: CustomerBrowser

class Customer(RequiredCustomer, OptionalCustomer):
    pass
