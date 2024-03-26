# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from peach_payments_python_sdk import schemas  # noqa: F401


class MerchantWebhookDataPayload(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The webhook data schema after decryption.
    """


    class MetaOapg:
        required = {
            "bankAccount",
            "amount",
            "presentationAmount",
            "paymentBrand",
            "referenceId",
            "billing",
            "paymentType",
            "result",
            "resultDetails",
            "shopify",
            "shipping",
            "merchantInvoiceId",
            "merchantTransactionId",
            "currency",
            "id",
            "merchantAccountId",
            "card",
            "connectorTxID1",
            "presentationCurrency",
            "authentication",
            "timestamp",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['UniqueId']:
                return UniqueId
        
            @staticmethod
            def paymentType() -> typing.Type['PaymentType']:
                return PaymentType
        
            @staticmethod
            def amount() -> typing.Type['Amount']:
                return Amount
        
            @staticmethod
            def merchantInvoiceId() -> typing.Type['MerchantInvoiceId']:
                return MerchantInvoiceId
        
            @staticmethod
            def merchantAccountId() -> typing.Type['MerchantAccountId']:
                return MerchantAccountId
        
            @staticmethod
            def currency() -> typing.Type['Currency']:
                return Currency
        
            @staticmethod
            def presentationAmount() -> typing.Type['Amount']:
                return Amount
        
            @staticmethod
            def result() -> typing.Type['Result']:
                return Result
        
            @staticmethod
            def resultDetails() -> typing.Type['ResultDetails']:
                return ResultDetails
        
            @staticmethod
            def connectorTxID1() -> typing.Type['ConnectorTxID1']:
                return ConnectorTxID1
        
            @staticmethod
            def authentication() -> typing.Type['MerchantWebhookDataPayloadAuthentication']:
                return MerchantWebhookDataPayloadAuthentication
        
            @staticmethod
            def card() -> typing.Type['Card']:
                return Card
            timestamp = schemas.DateTimeSchema
        
            @staticmethod
            def shipping() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def billing() -> typing.Type['Address']:
                return Address
            
            
            class bankAccount(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    required = {
                        "bankCode",
                        "bankName",
                        "holder",
                    }
                    
                    class properties:
                        
                        
                        class holder(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                regex=[{
                                    'pattern': r'^[\s\S]{4,128}$',
                                }]
                        
                        
                        class code(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                regex=[{
                                    'pattern': r'^[\s\S]{1,12}$',
                                }]
                        
                        
                        class bankName(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                regex=[{
                                    'pattern': r'^[\s\S]{1,255}$',
                                }]
                        __annotations__ = {
                            "holder": holder,
                            "code": code,
                            "bankName": bankName,
                        }
            
                
                bankCode: schemas.AnyTypeSchema
                bankName: MetaOapg.properties.bankName
                holder: MetaOapg.properties.holder
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["holder"]) -> MetaOapg.properties.holder: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["bankName"]) -> MetaOapg.properties.bankName: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["holder", "code", "bankName", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["holder"]) -> MetaOapg.properties.holder: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["bankName"]) -> MetaOapg.properties.bankName: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["holder", "code", "bankName", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    bankCode: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    bankName: typing.Union[MetaOapg.properties.bankName, str, ],
                    holder: typing.Union[MetaOapg.properties.holder, str, ],
                    code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'bankAccount':
                    return super().__new__(
                        cls,
                        *args,
                        bankCode=bankCode,
                        bankName=bankName,
                        holder=holder,
                        code=code,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def referenceId() -> typing.Type['UniqueId']:
                return UniqueId
        
            @staticmethod
            def shopify() -> typing.Type['Shopify']:
                return Shopify
            descriptor = schemas.StrSchema
        
            @staticmethod
            def customer() -> typing.Type['Customer']:
                return Customer
        
            @staticmethod
            def recon() -> typing.Type['Recon']:
                return Recon
            customParameters = schemas.DictSchema
        
            @staticmethod
            def merchant() -> typing.Type['MerchantWebhookDataPayloadMerchant']:
                return MerchantWebhookDataPayloadMerchant
            __annotations__ = {
                "id": id,
                "paymentType": paymentType,
                "amount": amount,
                "merchantInvoiceId": merchantInvoiceId,
                "merchantAccountId": merchantAccountId,
                "currency": currency,
                "presentationAmount": presentationAmount,
                "result": result,
                "resultDetails": resultDetails,
                "connectorTxID1": connectorTxID1,
                "authentication": authentication,
                "card": card,
                "timestamp": timestamp,
                "shipping": shipping,
                "billing": billing,
                "bankAccount": bankAccount,
                "referenceId": referenceId,
                "shopify": shopify,
                "descriptor": descriptor,
                "customer": customer,
                "recon": recon,
                "customParameters": customParameters,
                "merchant": merchant,
            }
    
    bankAccount: MetaOapg.properties.bankAccount
    amount: 'Amount'
    presentationAmount: 'Amount'
    paymentBrand: schemas.AnyTypeSchema
    referenceId: 'UniqueId'
    billing: 'Address'
    paymentType: 'PaymentType'
    result: 'Result'
    resultDetails: 'ResultDetails'
    shopify: 'Shopify'
    shipping: 'Address'
    merchantInvoiceId: 'MerchantInvoiceId'
    merchantTransactionId: schemas.AnyTypeSchema
    currency: 'Currency'
    id: 'UniqueId'
    merchantAccountId: 'MerchantAccountId'
    card: 'Card'
    connectorTxID1: 'ConnectorTxID1'
    presentationCurrency: schemas.AnyTypeSchema
    authentication: 'MerchantWebhookDataPayloadAuthentication'
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'UniqueId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentType"]) -> 'PaymentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'Amount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantInvoiceId"]) -> 'MerchantInvoiceId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantAccountId"]) -> 'MerchantAccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'Currency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["presentationAmount"]) -> 'Amount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> 'Result': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resultDetails"]) -> 'ResultDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectorTxID1"]) -> 'ConnectorTxID1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication"]) -> 'MerchantWebhookDataPayloadAuthentication': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["card"]) -> 'Card': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankAccount"]) -> MetaOapg.properties.bankAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceId"]) -> 'UniqueId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shopify"]) -> 'Shopify': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["descriptor"]) -> MetaOapg.properties.descriptor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'Customer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recon"]) -> 'Recon': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customParameters"]) -> MetaOapg.properties.customParameters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant"]) -> 'MerchantWebhookDataPayloadMerchant': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "paymentType", "amount", "merchantInvoiceId", "merchantAccountId", "currency", "presentationAmount", "result", "resultDetails", "connectorTxID1", "authentication", "card", "timestamp", "shipping", "billing", "bankAccount", "referenceId", "shopify", "descriptor", "customer", "recon", "customParameters", "merchant", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'UniqueId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentType"]) -> 'PaymentType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> 'Amount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantInvoiceId"]) -> 'MerchantInvoiceId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantAccountId"]) -> 'MerchantAccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> 'Currency': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["presentationAmount"]) -> 'Amount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> 'Result': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resultDetails"]) -> 'ResultDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectorTxID1"]) -> 'ConnectorTxID1': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication"]) -> 'MerchantWebhookDataPayloadAuthentication': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["card"]) -> 'Card': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping"]) -> 'Address': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing"]) -> 'Address': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankAccount"]) -> MetaOapg.properties.bankAccount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceId"]) -> 'UniqueId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shopify"]) -> 'Shopify': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["descriptor"]) -> typing.Union[MetaOapg.properties.descriptor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['Customer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recon"]) -> typing.Union['Recon', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customParameters"]) -> typing.Union[MetaOapg.properties.customParameters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant"]) -> typing.Union['MerchantWebhookDataPayloadMerchant', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "paymentType", "amount", "merchantInvoiceId", "merchantAccountId", "currency", "presentationAmount", "result", "resultDetails", "connectorTxID1", "authentication", "card", "timestamp", "shipping", "billing", "bankAccount", "referenceId", "shopify", "descriptor", "customer", "recon", "customParameters", "merchant", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bankAccount: typing.Union[MetaOapg.properties.bankAccount, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        amount: 'Amount',
        presentationAmount: 'Amount',
        paymentBrand: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        referenceId: 'UniqueId',
        billing: 'Address',
        paymentType: 'PaymentType',
        result: 'Result',
        resultDetails: 'ResultDetails',
        shopify: 'Shopify',
        shipping: 'Address',
        merchantInvoiceId: 'MerchantInvoiceId',
        merchantTransactionId: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        currency: 'Currency',
        id: 'UniqueId',
        merchantAccountId: 'MerchantAccountId',
        card: 'Card',
        connectorTxID1: 'ConnectorTxID1',
        presentationCurrency: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        authentication: 'MerchantWebhookDataPayloadAuthentication',
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        descriptor: typing.Union[MetaOapg.properties.descriptor, str, schemas.Unset] = schemas.unset,
        customer: typing.Union['Customer', schemas.Unset] = schemas.unset,
        recon: typing.Union['Recon', schemas.Unset] = schemas.unset,
        customParameters: typing.Union[MetaOapg.properties.customParameters, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        merchant: typing.Union['MerchantWebhookDataPayloadMerchant', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantWebhookDataPayload':
        return super().__new__(
            cls,
            *args,
            bankAccount=bankAccount,
            amount=amount,
            presentationAmount=presentationAmount,
            paymentBrand=paymentBrand,
            referenceId=referenceId,
            billing=billing,
            paymentType=paymentType,
            result=result,
            resultDetails=resultDetails,
            shopify=shopify,
            shipping=shipping,
            merchantInvoiceId=merchantInvoiceId,
            merchantTransactionId=merchantTransactionId,
            currency=currency,
            id=id,
            merchantAccountId=merchantAccountId,
            card=card,
            connectorTxID1=connectorTxID1,
            presentationCurrency=presentationCurrency,
            authentication=authentication,
            timestamp=timestamp,
            descriptor=descriptor,
            customer=customer,
            recon=recon,
            customParameters=customParameters,
            merchant=merchant,
            _configuration=_configuration,
            **kwargs,
        )

from peach_payments_python_sdk.model.address import Address
from peach_payments_python_sdk.model.amount import Amount
from peach_payments_python_sdk.model.card import Card
from peach_payments_python_sdk.model.connector_tx_id1 import ConnectorTxID1
from peach_payments_python_sdk.model.currency import Currency
from peach_payments_python_sdk.model.customer import Customer
from peach_payments_python_sdk.model.merchant_account_id import MerchantAccountId
from peach_payments_python_sdk.model.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.model.merchant_webhook_data_payload_authentication import MerchantWebhookDataPayloadAuthentication
from peach_payments_python_sdk.model.merchant_webhook_data_payload_merchant import MerchantWebhookDataPayloadMerchant
from peach_payments_python_sdk.model.payment_type import PaymentType
from peach_payments_python_sdk.model.recon import Recon
from peach_payments_python_sdk.model.result import Result
from peach_payments_python_sdk.model.result_details import ResultDetails
from peach_payments_python_sdk.model.shopify import Shopify
from peach_payments_python_sdk.model.unique_id import UniqueId
