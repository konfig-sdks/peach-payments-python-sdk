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


RequiredCheckout = TypedDict("RequiredCheckout", {
    # The entity for the request. By default, this is the channel ID.
    "authentication.entityId": str,

    # Token to verify the integrity of the payment, ensuring that only the merchant sending the request is accepted.
    "signature": str,

    # Merchant-provided reference number unique for your transactions.
    "merchantTransactionId": str,

    # The amount of the payment request. The period is used as the decimal separator. M-PESA does not support decimal amounts, so Checkout automatically rounds them up.
    "amount": str,

    # The payment type for the request. Accepts `DB`.  Does not accept `RG`, but you can tokenise a card by performing a DB with `createRegistration`.  Refund transactions through the Dashboard or as described in the <a href=\"https://developer.peachpayments.com/docs/checkout-refund\" target=\"_blank\">documentation</a>. 
    "paymentType": str,

    # The currency code of the payment request amount.
    "currency": str,

    # Unique value to represent each request.
    "nonce": str,

    # Checkout uses a POST request to redirect the customer to this URL after the customer completes checkout. Must be a valid URL that can be accessed through a browser.
    "shopperResultUrl": str,
    })

OptionalCheckout = TypedDict("OptionalCheckout", {
    # The preferred payment method which is active in the checkout page at the point of redirecting.
    "defaultPaymentMethod": str,

    # Force the default payment method to be the only payment method.
    "forceDefaultMethod": str,

    # Merchant-provided invoice number unique for your transactions. This identifier is not sent onwards.
    "merchantInvoiceId": str,

    # The customer is redirected to this URL if they cancel checkout. It must be a valid URL that can be reached through a browser.
    "cancelUrl": str,

    # Override the preconfigured webhook URL for this checkout instance, any changes to checkout will send a webhook to this url.
    "notificationUrl": str,

    # A name value pair used for sending custom information.
    "customParameters[name]": str,

    # An identifier for this customer. Typically this is the ID that identifies the shopper in the shop's system.
    "customer.merchantCustomerId": str,

    # The customer's first name or given name.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 
    "customer.givenName": str,

    # The customer's last name or surname.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 
    "customer.surname": str,

    # The customer's mobile number.
    "customer.mobile": str,

    # The customer's email address.
    "customer.email": str,

    # The customer's status. Accepts `NEW` or `EXISTING`.
    "customer.status": str,

    # The customer's birth date in the yyyy-MM-dd format.
    "customer.birthDate": str,

    # The customer's IP address.
    "customer.ip": str,

    # The customer's phone number.
    "customer.phone": str,

    # The customer's ID number, required for high-risk merchants supporting Capitec Pay.
    "customer.idNumber": str,

    # The door number, floor, building number, building name, and/or street name of the billing address.
    "billing.street1": str,

    # The adjoining road or locality, if required, of the billing address.
    "billing.street2": str,

    # The town, district, or city of the billing address.
    "billing.city": str,

    # The company of the billing address.
    "billing.company": str,

    # The country of the billing address (ISO 3166-1).
    "billing.country": str,

    # The county, state, or region of the billing address.
    "billing.state": str,

    # The postal code or ZIP code of the billing address.
    "billing.postcode": str,

    # The door number, floor, building number, building name, and/or street name of the shipping address.
    "shipping.street1": str,

    # The adjoining road or locality, if required, of the shipping address.
    "shipping.street2": str,

    # The town, district, or city of the shipping address.
    "shipping.city": str,

    # The company of the shipping address.
    "shipping.company": str,

    # The postal code or ZIP code of the shipping address.
    "shipping.postcode": str,

    # The country of the shipping address (ISO 3166-1).
    "shipping.country": str,

    # The county, state, or region of the shipping address.
    "shipping.state": str,

    # The tax percentage applied to the price of the item in the shopping cart.
    "cart.tax": str,

    # The total amount of the cart item including quantity.
    "cart.shippingAmount": str,

    # Discount amount applied on order amount.
    "cart.discount": str,

    # Used to enable card tokenisation with COPYandPAY.
    "createRegistration": str,

    # Used to provide a name for the application that is creating the checkout instance.
    "originator": str,

    # Text to display on \"Return to Store\" button on completing checkout.
    "returnTo": str,
    }, total=False)

class Checkout(RequiredCheckout, OptionalCheckout):
    pass
