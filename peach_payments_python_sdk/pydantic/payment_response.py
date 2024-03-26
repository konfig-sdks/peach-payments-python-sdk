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

from peach_payments_python_sdk.pydantic.amount import Amount
from peach_payments_python_sdk.pydantic.connector_tx_id1 import ConnectorTxID1
from peach_payments_python_sdk.pydantic.connector_tx_id2 import ConnectorTxID2
from peach_payments_python_sdk.pydantic.currency import Currency
from peach_payments_python_sdk.pydantic.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.pydantic.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.pydantic.payment_brand import PaymentBrand
from peach_payments_python_sdk.pydantic.payment_type import PaymentType
from peach_payments_python_sdk.pydantic.redirect import Redirect
from peach_payments_python_sdk.pydantic.result import Result
from peach_payments_python_sdk.pydantic.result_details import ResultDetails
from peach_payments_python_sdk.pydantic.unique_id import UniqueId
from peach_payments_python_sdk.pydantic.virtual_account import VirtualAccount

class PaymentResponse(BaseModel):
    amount: Amount = Field(alias='amount')

    currency: Currency = Field(alias='currency')

    payment_brand: PaymentBrand = Field(alias='paymentBrand')

    payment_type: PaymentType = Field(alias='paymentType')

    result: Result = Field(alias='result')

    # A JSON object depicting custom information sent by the merchant. Echoed back in the response.
    custom_parameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='customParameters')

    # The timestamp of the transaction.
    timestamp: datetime = Field(alias='timestamp')

    id: UniqueId = Field(alias='id')

    result_details: typing.Optional[ResultDetails] = Field(None, alias='resultDetails')

    redirect: typing.Optional[Redirect] = Field(None, alias='redirect')

    connector_tx_i_d1: typing.Optional[ConnectorTxID1] = Field(None, alias='connectorTxID1')

    connector_tx_i_d2: typing.Optional[ConnectorTxID2] = Field(None, alias='connectorTxID2')

    merchant_transaction_id: typing.Optional[MerchantTransactionId] = Field(None, alias='merchantTransactionId')

    merchant_invoice_id: typing.Optional[MerchantInvoiceId] = Field(None, alias='merchantInvoiceId')

    # The Payments API redirects the user to this URL after processing the payment request.
    shopper_result_url: typing.Optional[str] = Field(None, alias='shopperResultUrl')

    virtual_account: typing.Optional[VirtualAccount] = Field(None, alias='virtualAccount')

    # The expiry timestamp of the transaction.
    transaction_expiry_timestamp: typing.Optional[datetime] = Field(None, alias='transactionExpiryTimestamp')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
