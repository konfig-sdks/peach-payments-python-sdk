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


class CheckoutState(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    registrationId = schemas.StrSchema
                    checkoutId = schemas.StrSchema
                    transactionUniqueId = schemas.StrSchema
                    resultCode = schemas.StrSchema
                    paymentBrand = schemas.StrSchema
                    __annotations__ = {
                        "registrationId": registrationId,
                        "checkoutId": checkoutId,
                        "transactionUniqueId": transactionUniqueId,
                        "resultCode": resultCode,
                        "paymentBrand": paymentBrand,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["registrationId"]) -> MetaOapg.properties.registrationId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["checkoutId"]) -> MetaOapg.properties.checkoutId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["transactionUniqueId"]) -> MetaOapg.properties.transactionUniqueId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["resultCode"]) -> MetaOapg.properties.resultCode: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["paymentBrand"]) -> MetaOapg.properties.paymentBrand: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["registrationId", "checkoutId", "transactionUniqueId", "resultCode", "paymentBrand", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["registrationId"]) -> typing.Union[MetaOapg.properties.registrationId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["checkoutId"]) -> typing.Union[MetaOapg.properties.checkoutId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["transactionUniqueId"]) -> typing.Union[MetaOapg.properties.transactionUniqueId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["resultCode"]) -> typing.Union[MetaOapg.properties.resultCode, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["paymentBrand"]) -> typing.Union[MetaOapg.properties.paymentBrand, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["registrationId", "checkoutId", "transactionUniqueId", "resultCode", "paymentBrand", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                registrationId: typing.Union[MetaOapg.properties.registrationId, str, schemas.Unset] = schemas.unset,
                checkoutId: typing.Union[MetaOapg.properties.checkoutId, str, schemas.Unset] = schemas.unset,
                transactionUniqueId: typing.Union[MetaOapg.properties.transactionUniqueId, str, schemas.Unset] = schemas.unset,
                resultCode: typing.Union[MetaOapg.properties.resultCode, str, schemas.Unset] = schemas.unset,
                paymentBrand: typing.Union[MetaOapg.properties.paymentBrand, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    registrationId=registrationId,
                    checkoutId=checkoutId,
                    transactionUniqueId=transactionUniqueId,
                    resultCode=resultCode,
                    paymentBrand=paymentBrand,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                CheckoutOptions,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CheckoutState':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from peach_payments_python_sdk.model.checkout_options import CheckoutOptions
