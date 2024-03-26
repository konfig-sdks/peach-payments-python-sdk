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
from peach_payments_python_sdk.pydantic.currency import Currency
from peach_payments_python_sdk.pydantic.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.pydantic.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.pydantic.payment_brand import PaymentBrand
from peach_payments_python_sdk.pydantic.payment_type import PaymentType
from peach_payments_python_sdk.pydantic.recon import Recon
from peach_payments_python_sdk.pydantic.response_card import ResponseCard
from peach_payments_python_sdk.pydantic.result import Result
from peach_payments_python_sdk.pydantic.result_details import ResultDetails
from peach_payments_python_sdk.pydantic.unique_id import UniqueId

class MerchantTransactionIdStatusResponsePaymentsItem(BaseModel):
    id: UniqueId = Field(alias='id')

    payment_type: PaymentType = Field(alias='paymentType')

    payment_brand: PaymentBrand = Field(alias='paymentBrand')

    amount: Amount = Field(alias='amount')

    currency: Currency = Field(alias='currency')

    merchant_transaction_id: MerchantTransactionId = Field(alias='merchantTransactionId')

    result: Result = Field(alias='result')

    result_details: ResultDetails = Field(alias='resultDetails')

    connector_tx_i_d1: ConnectorTxID1 = Field(alias='connectorTxID1')

    # The timestamp of the transaction.
    timestamp: datetime = Field(alias='timestamp')

    # A JSON object depicting custom information sent by the merchant. Echoed back in the response.
    custom_parameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='customParameters')

    card: typing.Optional[ResponseCard] = Field(None, alias='card')

    merchant_invoice_id: typing.Optional[MerchantInvoiceId] = Field(None, alias='merchantInvoiceId')

    recon: typing.Optional[Recon] = Field(None, alias='recon')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
