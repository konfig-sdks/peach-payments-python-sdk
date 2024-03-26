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


class ResponseCard(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The card data structure holds information regarding a credit or debit card account.
    """


    class MetaOapg:
        
        class properties:
            
            
            class bin(
                schemas.StrSchema
            ):
                pass
            
            
            class last4Digits(
                schemas.StrSchema
            ):
                pass
            
            
            class holder(
                schemas.StrSchema
            ):
                pass
            
            
            class expiryMonth(
                schemas.StrSchema
            ):
                pass
            
            
            class expiryYear(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "bin": bin,
                "last4Digits": last4Digits,
                "holder": holder,
                "expiryMonth": expiryMonth,
                "expiryYear": expiryYear,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin"]) -> MetaOapg.properties.bin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last4Digits"]) -> MetaOapg.properties.last4Digits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holder"]) -> MetaOapg.properties.holder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryMonth"]) -> MetaOapg.properties.expiryMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryYear"]) -> MetaOapg.properties.expiryYear: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bin", "last4Digits", "holder", "expiryMonth", "expiryYear", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin"]) -> typing.Union[MetaOapg.properties.bin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last4Digits"]) -> typing.Union[MetaOapg.properties.last4Digits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holder"]) -> typing.Union[MetaOapg.properties.holder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryMonth"]) -> typing.Union[MetaOapg.properties.expiryMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryYear"]) -> typing.Union[MetaOapg.properties.expiryYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bin", "last4Digits", "holder", "expiryMonth", "expiryYear", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bin: typing.Union[MetaOapg.properties.bin, str, schemas.Unset] = schemas.unset,
        last4Digits: typing.Union[MetaOapg.properties.last4Digits, str, schemas.Unset] = schemas.unset,
        holder: typing.Union[MetaOapg.properties.holder, str, schemas.Unset] = schemas.unset,
        expiryMonth: typing.Union[MetaOapg.properties.expiryMonth, str, schemas.Unset] = schemas.unset,
        expiryYear: typing.Union[MetaOapg.properties.expiryYear, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResponseCard':
        return super().__new__(
            cls,
            *args,
            bin=bin,
            last4Digits=last4Digits,
            holder=holder,
            expiryMonth=expiryMonth,
            expiryYear=expiryYear,
            _configuration=_configuration,
            **kwargs,
        )
