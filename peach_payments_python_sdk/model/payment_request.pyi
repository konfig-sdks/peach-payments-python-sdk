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


class PaymentRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Initiate a debit transaction.
    """


    class MetaOapg:
        required = {
            "amount",
            "paymentBrand",
            "merchantTransactionId",
            "currency",
            "authentication",
            "paymentType",
        }
        
        class properties:
        
            @staticmethod
            def authentication() -> typing.Type['Authentication']:
                return Authentication
        
            @staticmethod
            def merchantTransactionId() -> typing.Type['MerchantTransactionId']:
                return MerchantTransactionId
        
            @staticmethod
            def amount() -> typing.Type['Amount']:
                return Amount
        
            @staticmethod
            def currency() -> typing.Type['Currency']:
                return Currency
        
            @staticmethod
            def paymentBrand() -> typing.Type['PaymentBrand']:
                return PaymentBrand
        
            @staticmethod
            def paymentType() -> typing.Type['PaymentType']:
                return PaymentType
        
            @staticmethod
            def virtualAccount() -> typing.Type['VirtualAccount']:
                return VirtualAccount
        
            @staticmethod
            def shipping() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def billing() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def shopify() -> typing.Type['Shopify']:
                return Shopify
        
            @staticmethod
            def customer() -> typing.Type['Customer']:
                return Customer
        
            @staticmethod
            def cart() -> typing.Type['Cart']:
                return Cart
        
            @staticmethod
            def merchantInvoiceId() -> typing.Type['MerchantInvoiceId']:
                return MerchantInvoiceId
            shopperResultUrl = schemas.StrSchema
            __annotations__ = {
                "authentication": authentication,
                "merchantTransactionId": merchantTransactionId,
                "amount": amount,
                "currency": currency,
                "paymentBrand": paymentBrand,
                "paymentType": paymentType,
                "virtualAccount": virtualAccount,
                "shipping": shipping,
                "billing": billing,
                "shopify": shopify,
                "customer": customer,
                "cart": cart,
                "merchantInvoiceId": merchantInvoiceId,
                "shopperResultUrl": shopperResultUrl,
            }
    
    amount: 'Amount'
    paymentBrand: 'PaymentBrand'
    merchantTransactionId: 'MerchantTransactionId'
    currency: 'Currency'
    authentication: 'Authentication'
    paymentType: 'PaymentType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication"]) -> 'Authentication': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantTransactionId"]) -> 'MerchantTransactionId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'Amount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'Currency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentBrand"]) -> 'PaymentBrand': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentType"]) -> 'PaymentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["virtualAccount"]) -> 'VirtualAccount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shopify"]) -> 'Shopify': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'Customer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cart"]) -> 'Cart': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantInvoiceId"]) -> 'MerchantInvoiceId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shopperResultUrl"]) -> MetaOapg.properties.shopperResultUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authentication", "merchantTransactionId", "amount", "currency", "paymentBrand", "paymentType", "virtualAccount", "shipping", "billing", "shopify", "customer", "cart", "merchantInvoiceId", "shopperResultUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication"]) -> 'Authentication': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantTransactionId"]) -> 'MerchantTransactionId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> 'Amount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> 'Currency': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentBrand"]) -> 'PaymentBrand': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentType"]) -> 'PaymentType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["virtualAccount"]) -> typing.Union['VirtualAccount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shopify"]) -> typing.Union['Shopify', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['Customer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cart"]) -> typing.Union['Cart', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantInvoiceId"]) -> typing.Union['MerchantInvoiceId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shopperResultUrl"]) -> typing.Union[MetaOapg.properties.shopperResultUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authentication", "merchantTransactionId", "amount", "currency", "paymentBrand", "paymentType", "virtualAccount", "shipping", "billing", "shopify", "customer", "cart", "merchantInvoiceId", "shopperResultUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: 'Amount',
        paymentBrand: 'PaymentBrand',
        merchantTransactionId: 'MerchantTransactionId',
        currency: 'Currency',
        authentication: 'Authentication',
        paymentType: 'PaymentType',
        virtualAccount: typing.Union['VirtualAccount', schemas.Unset] = schemas.unset,
        shipping: typing.Union['Address', schemas.Unset] = schemas.unset,
        billing: typing.Union['Address', schemas.Unset] = schemas.unset,
        shopify: typing.Union['Shopify', schemas.Unset] = schemas.unset,
        customer: typing.Union['Customer', schemas.Unset] = schemas.unset,
        cart: typing.Union['Cart', schemas.Unset] = schemas.unset,
        merchantInvoiceId: typing.Union['MerchantInvoiceId', schemas.Unset] = schemas.unset,
        shopperResultUrl: typing.Union[MetaOapg.properties.shopperResultUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentRequest':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            paymentBrand=paymentBrand,
            merchantTransactionId=merchantTransactionId,
            currency=currency,
            authentication=authentication,
            paymentType=paymentType,
            virtualAccount=virtualAccount,
            shipping=shipping,
            billing=billing,
            shopify=shopify,
            customer=customer,
            cart=cart,
            merchantInvoiceId=merchantInvoiceId,
            shopperResultUrl=shopperResultUrl,
            _configuration=_configuration,
            **kwargs,
        )

from peach_payments_python_sdk.model.address import Address
from peach_payments_python_sdk.model.amount import Amount
from peach_payments_python_sdk.model.authentication import Authentication
from peach_payments_python_sdk.model.cart import Cart
from peach_payments_python_sdk.model.currency import Currency
from peach_payments_python_sdk.model.customer import Customer
from peach_payments_python_sdk.model.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.model.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.model.payment_brand import PaymentBrand
from peach_payments_python_sdk.model.payment_type import PaymentType
from peach_payments_python_sdk.model.shopify import Shopify
from peach_payments_python_sdk.model.virtual_account import VirtualAccount
