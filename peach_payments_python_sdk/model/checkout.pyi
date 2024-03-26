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


class Checkout(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "amount",
            "signature",
            "authentication.entityId",
            "shopperResultUrl",
            "merchantTransactionId",
            "currency",
            "nonce",
            "paymentType",
        }
        
        class properties:
            
            
            class authentication_entity_id(
                schemas.StrSchema
            ):
                pass
            
            
            class signature(
                schemas.StrSchema
            ):
                pass
            
            
            class merchantTransactionId(
                schemas.StrSchema
            ):
                pass
            amount = schemas.StrSchema
            
            
            class paymentType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DB(cls):
                    return cls("DB")
            
            
            class currency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ZAR(cls):
                    return cls("ZAR")
                
                @schemas.classproperty
                def USD(cls):
                    return cls("USD")
                
                @schemas.classproperty
                def KES(cls):
                    return cls("KES")
                
                @schemas.classproperty
                def MUR(cls):
                    return cls("MUR")
                
                @schemas.classproperty
                def GBP(cls):
                    return cls("GBP")
                
                @schemas.classproperty
                def EUR(cls):
                    return cls("EUR")
            
            
            class nonce(
                schemas.StrSchema
            ):
                pass
            shopperResultUrl = schemas.StrSchema
            
            
            class defaultPaymentMethod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CARD(cls):
                    return cls("CARD")
                
                @schemas.classproperty
                def MASTERPASS(cls):
                    return cls("MASTERPASS")
                
                @schemas.classproperty
                def MOBICRED(cls):
                    return cls("MOBICRED")
                
                @schemas.classproperty
                def EFTSECURE(cls):
                    return cls("EFTSECURE")
                
                @schemas.classproperty
                def MPESA(cls):
                    return cls("MPESA")
                
                @schemas.classproperty
                def _1FORYOU(cls):
                    return cls("1FORYOU")
                
                @schemas.classproperty
                def APLUS(cls):
                    return cls("APLUS")
                
                @schemas.classproperty
                def PAYPAL(cls):
                    return cls("PAYPAL")
                
                @schemas.classproperty
                def ZEROPAY(cls):
                    return cls("ZEROPAY")
                
                @schemas.classproperty
                def PAYFLEX(cls):
                    return cls("PAYFLEX")
                
                @schemas.classproperty
                def FINCHOICEPAY(cls):
                    return cls("FINCHOICEPAY")
                
                @schemas.classproperty
                def BLINKBYEMTEL(cls):
                    return cls("BLINKBYEMTEL")
                
                @schemas.classproperty
                def CAPITECPAY(cls):
                    return cls("CAPITECPAY")
                
                @schemas.classproperty
                def NEDBANKDIRECTEFT(cls):
                    return cls("NEDBANKDIRECTEFT")
                
                @schemas.classproperty
                def PAYBYBANK(cls):
                    return cls("PAYBYBANK")
                
                @schemas.classproperty
                def APPLE_PAY(cls):
                    return cls("APPLE PAY")
                
                @schemas.classproperty
                def MCBJUICE(cls):
                    return cls("MCBJUICE")
            
            
            class forceDefaultMethod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
            
            
            class merchantInvoiceId(
                schemas.StrSchema
            ):
                pass
            cancelUrl = schemas.StrSchema
            notificationUrl = schemas.StrSchema
            custom_parameters_name = schemas.StrSchema
            
            
            class customer_merchant_customer_id(
                schemas.StrSchema
            ):
                pass
            
            
            class customer_given_name(
                schemas.StrSchema
            ):
                pass
            
            
            class customer_surname(
                schemas.StrSchema
            ):
                pass
            
            
            class customer_mobile(
                schemas.StrSchema
            ):
                pass
            
            
            class customer_email(
                schemas.StrSchema
            ):
                pass
            
            
            class customer_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NEW(cls):
                    return cls("NEW")
                
                @schemas.classproperty
                def EXISTING(cls):
                    return cls("EXISTING")
            customer_birth_date = schemas.StrSchema
            
            
            class customer_ip(
                schemas.StrSchema
            ):
                pass
            
            
            class customer_phone(
                schemas.StrSchema
            ):
                pass
            
            
            class customer_id_number(
                schemas.StrSchema
            ):
                pass
            
            
            class billing_street1(
                schemas.StrSchema
            ):
                pass
            
            
            class billing_street2(
                schemas.StrSchema
            ):
                pass
            
            
            class billing_city(
                schemas.StrSchema
            ):
                pass
            
            
            class billing_company(
                schemas.StrSchema
            ):
                pass
            
            
            class billing_country(
                schemas.StrSchema
            ):
                pass
            
            
            class billing_state(
                schemas.StrSchema
            ):
                pass
            
            
            class billing_postcode(
                schemas.StrSchema
            ):
                pass
            
            
            class shipping_street1(
                schemas.StrSchema
            ):
                pass
            
            
            class shipping_street2(
                schemas.StrSchema
            ):
                pass
            
            
            class shipping_city(
                schemas.StrSchema
            ):
                pass
            
            
            class shipping_company(
                schemas.StrSchema
            ):
                pass
            
            
            class shipping_postcode(
                schemas.StrSchema
            ):
                pass
            
            
            class shipping_country(
                schemas.StrSchema
            ):
                pass
            
            
            class shipping_state(
                schemas.StrSchema
            ):
                pass
            cart_tax = schemas.StrSchema
            cart_shipping_amount = schemas.StrSchema
            cart_discount = schemas.StrSchema
            
            
            class createRegistration(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRUE(cls):
                    return cls("true")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
            
            
            class originator(
                schemas.StrSchema
            ):
                pass
            
            
            class returnTo(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STORE(cls):
                    return cls("STORE")
                
                @schemas.classproperty
                def INVOICE(cls):
                    return cls("INVOICE")
            __annotations__ = {
                "authentication.entityId": authentication_entity_id,
                "signature": signature,
                "merchantTransactionId": merchantTransactionId,
                "amount": amount,
                "paymentType": paymentType,
                "currency": currency,
                "nonce": nonce,
                "shopperResultUrl": shopperResultUrl,
                "defaultPaymentMethod": defaultPaymentMethod,
                "forceDefaultMethod": forceDefaultMethod,
                "merchantInvoiceId": merchantInvoiceId,
                "cancelUrl": cancelUrl,
                "notificationUrl": notificationUrl,
                "customParameters[name]": custom_parameters_name,
                "customer.merchantCustomerId": customer_merchant_customer_id,
                "customer.givenName": customer_given_name,
                "customer.surname": customer_surname,
                "customer.mobile": customer_mobile,
                "customer.email": customer_email,
                "customer.status": customer_status,
                "customer.birthDate": customer_birth_date,
                "customer.ip": customer_ip,
                "customer.phone": customer_phone,
                "customer.idNumber": customer_id_number,
                "billing.street1": billing_street1,
                "billing.street2": billing_street2,
                "billing.city": billing_city,
                "billing.company": billing_company,
                "billing.country": billing_country,
                "billing.state": billing_state,
                "billing.postcode": billing_postcode,
                "shipping.street1": shipping_street1,
                "shipping.street2": shipping_street2,
                "shipping.city": shipping_city,
                "shipping.company": shipping_company,
                "shipping.postcode": shipping_postcode,
                "shipping.country": shipping_country,
                "shipping.state": shipping_state,
                "cart.tax": cart_tax,
                "cart.shippingAmount": cart_shipping_amount,
                "cart.discount": cart_discount,
                "createRegistration": createRegistration,
                "originator": originator,
                "returnTo": returnTo,
            }
    
    amount: MetaOapg.properties.amount
    signature: MetaOapg.properties.signature
    shopperResultUrl: MetaOapg.properties.shopperResultUrl
    merchantTransactionId: MetaOapg.properties.merchantTransactionId
    currency: MetaOapg.properties.currency
    nonce: MetaOapg.properties.nonce
    paymentType: MetaOapg.properties.paymentType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication.entityId"]) -> MetaOapg.properties.authentication_entity_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature"]) -> MetaOapg.properties.signature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantTransactionId"]) -> MetaOapg.properties.merchantTransactionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentType"]) -> MetaOapg.properties.paymentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shopperResultUrl"]) -> MetaOapg.properties.shopperResultUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultPaymentMethod"]) -> MetaOapg.properties.defaultPaymentMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forceDefaultMethod"]) -> MetaOapg.properties.forceDefaultMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantInvoiceId"]) -> MetaOapg.properties.merchantInvoiceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancelUrl"]) -> MetaOapg.properties.cancelUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationUrl"]) -> MetaOapg.properties.notificationUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customParameters[name]"]) -> MetaOapg.properties.custom_parameters_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.merchantCustomerId"]) -> MetaOapg.properties.customer_merchant_customer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.givenName"]) -> MetaOapg.properties.customer_given_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.surname"]) -> MetaOapg.properties.customer_surname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.mobile"]) -> MetaOapg.properties.customer_mobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.email"]) -> MetaOapg.properties.customer_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.status"]) -> MetaOapg.properties.customer_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.birthDate"]) -> MetaOapg.properties.customer_birth_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.ip"]) -> MetaOapg.properties.customer_ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.phone"]) -> MetaOapg.properties.customer_phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer.idNumber"]) -> MetaOapg.properties.customer_id_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing.street1"]) -> MetaOapg.properties.billing_street1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing.street2"]) -> MetaOapg.properties.billing_street2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing.city"]) -> MetaOapg.properties.billing_city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing.company"]) -> MetaOapg.properties.billing_company: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing.country"]) -> MetaOapg.properties.billing_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing.state"]) -> MetaOapg.properties.billing_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing.postcode"]) -> MetaOapg.properties.billing_postcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping.street1"]) -> MetaOapg.properties.shipping_street1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping.street2"]) -> MetaOapg.properties.shipping_street2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping.city"]) -> MetaOapg.properties.shipping_city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping.company"]) -> MetaOapg.properties.shipping_company: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping.postcode"]) -> MetaOapg.properties.shipping_postcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping.country"]) -> MetaOapg.properties.shipping_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping.state"]) -> MetaOapg.properties.shipping_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cart.tax"]) -> MetaOapg.properties.cart_tax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cart.shippingAmount"]) -> MetaOapg.properties.cart_shipping_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cart.discount"]) -> MetaOapg.properties.cart_discount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createRegistration"]) -> MetaOapg.properties.createRegistration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originator"]) -> MetaOapg.properties.originator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["returnTo"]) -> MetaOapg.properties.returnTo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authentication.entityId", "signature", "merchantTransactionId", "amount", "paymentType", "currency", "nonce", "shopperResultUrl", "defaultPaymentMethod", "forceDefaultMethod", "merchantInvoiceId", "cancelUrl", "notificationUrl", "customParameters[name]", "customer.merchantCustomerId", "customer.givenName", "customer.surname", "customer.mobile", "customer.email", "customer.status", "customer.birthDate", "customer.ip", "customer.phone", "customer.idNumber", "billing.street1", "billing.street2", "billing.city", "billing.company", "billing.country", "billing.state", "billing.postcode", "shipping.street1", "shipping.street2", "shipping.city", "shipping.company", "shipping.postcode", "shipping.country", "shipping.state", "cart.tax", "cart.shippingAmount", "cart.discount", "createRegistration", "originator", "returnTo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication.entityId"]) -> MetaOapg.properties.authentication_entity_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature"]) -> MetaOapg.properties.signature: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantTransactionId"]) -> MetaOapg.properties.merchantTransactionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentType"]) -> MetaOapg.properties.paymentType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shopperResultUrl"]) -> MetaOapg.properties.shopperResultUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultPaymentMethod"]) -> typing.Union[MetaOapg.properties.defaultPaymentMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forceDefaultMethod"]) -> typing.Union[MetaOapg.properties.forceDefaultMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantInvoiceId"]) -> typing.Union[MetaOapg.properties.merchantInvoiceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancelUrl"]) -> typing.Union[MetaOapg.properties.cancelUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationUrl"]) -> typing.Union[MetaOapg.properties.notificationUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customParameters[name]"]) -> typing.Union[MetaOapg.properties.custom_parameters_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.merchantCustomerId"]) -> typing.Union[MetaOapg.properties.customer_merchant_customer_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.givenName"]) -> typing.Union[MetaOapg.properties.customer_given_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.surname"]) -> typing.Union[MetaOapg.properties.customer_surname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.mobile"]) -> typing.Union[MetaOapg.properties.customer_mobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.email"]) -> typing.Union[MetaOapg.properties.customer_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.status"]) -> typing.Union[MetaOapg.properties.customer_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.birthDate"]) -> typing.Union[MetaOapg.properties.customer_birth_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.ip"]) -> typing.Union[MetaOapg.properties.customer_ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.phone"]) -> typing.Union[MetaOapg.properties.customer_phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer.idNumber"]) -> typing.Union[MetaOapg.properties.customer_id_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing.street1"]) -> typing.Union[MetaOapg.properties.billing_street1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing.street2"]) -> typing.Union[MetaOapg.properties.billing_street2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing.city"]) -> typing.Union[MetaOapg.properties.billing_city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing.company"]) -> typing.Union[MetaOapg.properties.billing_company, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing.country"]) -> typing.Union[MetaOapg.properties.billing_country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing.state"]) -> typing.Union[MetaOapg.properties.billing_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing.postcode"]) -> typing.Union[MetaOapg.properties.billing_postcode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping.street1"]) -> typing.Union[MetaOapg.properties.shipping_street1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping.street2"]) -> typing.Union[MetaOapg.properties.shipping_street2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping.city"]) -> typing.Union[MetaOapg.properties.shipping_city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping.company"]) -> typing.Union[MetaOapg.properties.shipping_company, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping.postcode"]) -> typing.Union[MetaOapg.properties.shipping_postcode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping.country"]) -> typing.Union[MetaOapg.properties.shipping_country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping.state"]) -> typing.Union[MetaOapg.properties.shipping_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cart.tax"]) -> typing.Union[MetaOapg.properties.cart_tax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cart.shippingAmount"]) -> typing.Union[MetaOapg.properties.cart_shipping_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cart.discount"]) -> typing.Union[MetaOapg.properties.cart_discount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createRegistration"]) -> typing.Union[MetaOapg.properties.createRegistration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originator"]) -> typing.Union[MetaOapg.properties.originator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["returnTo"]) -> typing.Union[MetaOapg.properties.returnTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authentication.entityId", "signature", "merchantTransactionId", "amount", "paymentType", "currency", "nonce", "shopperResultUrl", "defaultPaymentMethod", "forceDefaultMethod", "merchantInvoiceId", "cancelUrl", "notificationUrl", "customParameters[name]", "customer.merchantCustomerId", "customer.givenName", "customer.surname", "customer.mobile", "customer.email", "customer.status", "customer.birthDate", "customer.ip", "customer.phone", "customer.idNumber", "billing.street1", "billing.street2", "billing.city", "billing.company", "billing.country", "billing.state", "billing.postcode", "shipping.street1", "shipping.street2", "shipping.city", "shipping.company", "shipping.postcode", "shipping.country", "shipping.state", "cart.tax", "cart.shippingAmount", "cart.discount", "createRegistration", "originator", "returnTo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        signature: typing.Union[MetaOapg.properties.signature, str, ],
        shopperResultUrl: typing.Union[MetaOapg.properties.shopperResultUrl, str, ],
        merchantTransactionId: typing.Union[MetaOapg.properties.merchantTransactionId, str, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        nonce: typing.Union[MetaOapg.properties.nonce, str, ],
        paymentType: typing.Union[MetaOapg.properties.paymentType, str, ],
        defaultPaymentMethod: typing.Union[MetaOapg.properties.defaultPaymentMethod, str, schemas.Unset] = schemas.unset,
        forceDefaultMethod: typing.Union[MetaOapg.properties.forceDefaultMethod, str, schemas.Unset] = schemas.unset,
        merchantInvoiceId: typing.Union[MetaOapg.properties.merchantInvoiceId, str, schemas.Unset] = schemas.unset,
        cancelUrl: typing.Union[MetaOapg.properties.cancelUrl, str, schemas.Unset] = schemas.unset,
        notificationUrl: typing.Union[MetaOapg.properties.notificationUrl, str, schemas.Unset] = schemas.unset,
        createRegistration: typing.Union[MetaOapg.properties.createRegistration, str, schemas.Unset] = schemas.unset,
        originator: typing.Union[MetaOapg.properties.originator, str, schemas.Unset] = schemas.unset,
        returnTo: typing.Union[MetaOapg.properties.returnTo, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Checkout':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            signature=signature,
            shopperResultUrl=shopperResultUrl,
            merchantTransactionId=merchantTransactionId,
            currency=currency,
            nonce=nonce,
            paymentType=paymentType,
            defaultPaymentMethod=defaultPaymentMethod,
            forceDefaultMethod=forceDefaultMethod,
            merchantInvoiceId=merchantInvoiceId,
            cancelUrl=cancelUrl,
            notificationUrl=notificationUrl,
            createRegistration=createRegistration,
            originator=originator,
            returnTo=returnTo,
            _configuration=_configuration,
            **kwargs,
        )
