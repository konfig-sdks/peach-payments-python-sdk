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


class Checkout(BaseModel):
    # The entity for the request. By default, this is the channel ID.
    authentication.entity_id_: str = Field(alias='authentication.entityId')

    # Token to verify the integrity of the payment, ensuring that only the merchant sending the request is accepted.
    signature: str = Field(alias='signature')

    # Merchant-provided reference number unique for your transactions.
    merchant_transaction_id: str = Field(alias='merchantTransactionId')

    # The amount of the payment request. The period is used as the decimal separator. M-PESA does not support decimal amounts, so Checkout automatically rounds them up.
    amount: str = Field(alias='amount')

    # The payment type for the request. Accepts `DB`.  Does not accept `RG`, but you can tokenise a card by performing a DB with `createRegistration`.  Refund transactions through the Dashboard or as described in the <a href=\"https://developer.peachpayments.com/docs/checkout-refund\" target=\"_blank\">documentation</a>. 
    payment_type: Literal["DB"] = Field(alias='paymentType')

    # The currency code of the payment request amount.
    currency: Literal["ZAR", "USD", "KES", "MUR", "GBP", "EUR"] = Field(alias='currency')

    # Unique value to represent each request.
    nonce: str = Field(alias='nonce')

    # Checkout uses a POST request to redirect the customer to this URL after the customer completes checkout. Must be a valid URL that can be accessed through a browser.
    shopper_result_url: str = Field(alias='shopperResultUrl')

    # The preferred payment method which is active in the checkout page at the point of redirecting.
    default_payment_method: typing.Optional[Literal["CARD", "MASTERPASS", "MOBICRED", "EFTSECURE", "MPESA", "1FORYOU", "APLUS", "PAYPAL", "ZEROPAY", "PAYFLEX", "FINCHOICEPAY", "BLINKBYEMTEL", "CAPITECPAY", "NEDBANKDIRECTEFT", "PAYBYBANK", "APPLE PAY", "MCBJUICE"]] = Field(None, alias='defaultPaymentMethod')

    # Force the default payment method to be the only payment method.
    force_default_method: typing.Optional[Literal["true", "false"]] = Field(None, alias='forceDefaultMethod')

    # Merchant-provided invoice number unique for your transactions. This identifier is not sent onwards.
    merchant_invoice_id: typing.Optional[str] = Field(None, alias='merchantInvoiceId')

    # The customer is redirected to this URL if they cancel checkout. It must be a valid URL that can be reached through a browser.
    cancel_url: typing.Optional[str] = Field(None, alias='cancelUrl')

    # Override the preconfigured webhook URL for this checkout instance, any changes to checkout will send a webhook to this url.
    notification_url: typing.Optional[str] = Field(None, alias='notificationUrl')

    # A name value pair used for sending custom information.
    custom_parameters[name]_: typing.Optional[str] = Field(None, alias='customParameters[name]')

    # An identifier for this customer. Typically this is the ID that identifies the shopper in the shop's system.
    customer.merchant_customer_id_: typing.Optional[str] = Field(None, alias='customer.merchantCustomerId')

    # The customer's first name or given name.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 
    customer.given_name_: typing.Optional[str] = Field(None, alias='customer.givenName')

    # The customer's last name or surname.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 
    customer.surname_: typing.Optional[str] = Field(None, alias='customer.surname')

    # The customer's mobile number.
    customer.mobile_: typing.Optional[str] = Field(None, alias='customer.mobile')

    # The customer's email address.
    customer.email_: typing.Optional[str] = Field(None, alias='customer.email')

    # The customer's status. Accepts `NEW` or `EXISTING`.
    customer.status_: typing.Optional[Literal["NEW", "EXISTING"]] = Field(None, alias='customer.status')

    # The customer's birth date in the yyyy-MM-dd format.
    customer.birth_date_: typing.Optional[str] = Field(None, alias='customer.birthDate')

    # The customer's IP address.
    customer.ip_: typing.Optional[str] = Field(None, alias='customer.ip')

    # The customer's phone number.
    customer.phone_: typing.Optional[str] = Field(None, alias='customer.phone')

    # The customer's ID number, required for high-risk merchants supporting Capitec Pay.
    customer.id_number_: typing.Optional[str] = Field(None, alias='customer.idNumber')

    # The door number, floor, building number, building name, and/or street name of the billing address.
    billing.street1_: typing.Optional[str] = Field(None, alias='billing.street1')

    # The adjoining road or locality, if required, of the billing address.
    billing.street2_: typing.Optional[str] = Field(None, alias='billing.street2')

    # The town, district, or city of the billing address.
    billing.city_: typing.Optional[str] = Field(None, alias='billing.city')

    # The company of the billing address.
    billing.company_: typing.Optional[str] = Field(None, alias='billing.company')

    # The country of the billing address (ISO 3166-1).
    billing.country_: typing.Optional[str] = Field(None, alias='billing.country')

    # The county, state, or region of the billing address.
    billing.state_: typing.Optional[str] = Field(None, alias='billing.state')

    # The postal code or ZIP code of the billing address.
    billing.postcode_: typing.Optional[str] = Field(None, alias='billing.postcode')

    # The door number, floor, building number, building name, and/or street name of the shipping address.
    shipping.street1_: typing.Optional[str] = Field(None, alias='shipping.street1')

    # The adjoining road or locality, if required, of the shipping address.
    shipping.street2_: typing.Optional[str] = Field(None, alias='shipping.street2')

    # The town, district, or city of the shipping address.
    shipping.city_: typing.Optional[str] = Field(None, alias='shipping.city')

    # The company of the shipping address.
    shipping.company_: typing.Optional[str] = Field(None, alias='shipping.company')

    # The postal code or ZIP code of the shipping address.
    shipping.postcode_: typing.Optional[str] = Field(None, alias='shipping.postcode')

    # The country of the shipping address (ISO 3166-1).
    shipping.country_: typing.Optional[str] = Field(None, alias='shipping.country')

    # The county, state, or region of the shipping address.
    shipping.state_: typing.Optional[str] = Field(None, alias='shipping.state')

    # The tax percentage applied to the price of the item in the shopping cart.
    cart.tax_: typing.Optional[str] = Field(None, alias='cart.tax')

    # The total amount of the cart item including quantity.
    cart.shipping_amount_: typing.Optional[str] = Field(None, alias='cart.shippingAmount')

    # Discount amount applied on order amount.
    cart.discount_: typing.Optional[str] = Field(None, alias='cart.discount')

    # Used to enable card tokenisation with COPYandPAY.
    create_registration: typing.Optional[Literal["true", "false"]] = Field(None, alias='createRegistration')

    # Used to provide a name for the application that is creating the checkout instance.
    originator: typing.Optional[str] = Field(None, alias='originator')

    # Text to display on \"Return to Store\" button on completing checkout.
    return_to: typing.Optional[Literal["STORE", "INVOICE"]] = Field(None, alias='returnTo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
