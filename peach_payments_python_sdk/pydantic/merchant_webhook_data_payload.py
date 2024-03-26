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

from peach_payments_python_sdk.pydantic.address import Address
from peach_payments_python_sdk.pydantic.amount import Amount
from peach_payments_python_sdk.pydantic.card import Card
from peach_payments_python_sdk.pydantic.connector_tx_id1 import ConnectorTxID1
from peach_payments_python_sdk.pydantic.currency import Currency
from peach_payments_python_sdk.pydantic.customer import Customer
from peach_payments_python_sdk.pydantic.merchant_account_id import MerchantAccountId
from peach_payments_python_sdk.pydantic.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.pydantic.merchant_webhook_data_payload_authentication import MerchantWebhookDataPayloadAuthentication
from peach_payments_python_sdk.pydantic.merchant_webhook_data_payload_merchant import MerchantWebhookDataPayloadMerchant
from peach_payments_python_sdk.pydantic.payment_type import PaymentType
from peach_payments_python_sdk.pydantic.recon import Recon
from peach_payments_python_sdk.pydantic.result import Result
from peach_payments_python_sdk.pydantic.result_details import ResultDetails
from peach_payments_python_sdk.pydantic.shopify import Shopify
from peach_payments_python_sdk.pydantic.unique_id import UniqueId

class MerchantWebhookDataPayload(BaseModel):
    id: UniqueId = Field(alias='id')

    payment_type: PaymentType = Field(alias='paymentType')

    amount: Amount = Field(alias='amount')

    merchant_invoice_id: MerchantInvoiceId = Field(alias='merchantInvoiceId')

    merchant_account_id: MerchantAccountId = Field(alias='merchantAccountId')

    currency: Currency = Field(alias='currency')

    presentation_amount: Amount = Field(alias='presentationAmount')

    result: Result = Field(alias='result')

    result_details: ResultDetails = Field(alias='resultDetails')

    connector_tx_i_d1: ConnectorTxID1 = Field(alias='connectorTxID1')

    authentication: MerchantWebhookDataPayloadAuthentication = Field(alias='authentication')

    card: Card = Field(alias='card')

    # The timestamp of the transaction.
    timestamp: datetime = Field(alias='timestamp')

    shipping: Address = Field(alias='shipping')

    billing: Address = Field(alias='billing')

    # Bank account data.
    bank_account: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='bankAccount')

    reference_id: UniqueId = Field(alias='referenceId')

    shopify: Shopify = Field(alias='shopify')

    descriptor: typing.Optional[str] = Field(None, alias='descriptor')

    customer: typing.Optional[Customer] = Field(None, alias='customer')

    recon: typing.Optional[Recon] = Field(None, alias='recon')

    # A JSON object depicting custom information sent by the merchant. Echoed back in the response.
    custom_parameters: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='customParameters')

    merchant: typing.Optional[MerchantWebhookDataPayloadMerchant] = Field(None, alias='merchant')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
