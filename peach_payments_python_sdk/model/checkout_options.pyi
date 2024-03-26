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


class CheckoutOptions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The checkout object contains the default payment method and whether to tokenise the card number.
    """


    class MetaOapg:
        
        class properties:
            
            
            class defaultPaymentMethod(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'defaultPaymentMethod':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class forceDefaultMethod(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'forceDefaultMethod':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            tokeniseCard = schemas.BoolSchema
            __annotations__ = {
                "defaultPaymentMethod": defaultPaymentMethod,
                "forceDefaultMethod": forceDefaultMethod,
                "tokeniseCard": tokeniseCard,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultPaymentMethod"]) -> MetaOapg.properties.defaultPaymentMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forceDefaultMethod"]) -> MetaOapg.properties.forceDefaultMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokeniseCard"]) -> MetaOapg.properties.tokeniseCard: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["defaultPaymentMethod", "forceDefaultMethod", "tokeniseCard", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultPaymentMethod"]) -> typing.Union[MetaOapg.properties.defaultPaymentMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forceDefaultMethod"]) -> typing.Union[MetaOapg.properties.forceDefaultMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokeniseCard"]) -> typing.Union[MetaOapg.properties.tokeniseCard, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["defaultPaymentMethod", "forceDefaultMethod", "tokeniseCard", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        defaultPaymentMethod: typing.Union[MetaOapg.properties.defaultPaymentMethod, None, str, schemas.Unset] = schemas.unset,
        forceDefaultMethod: typing.Union[MetaOapg.properties.forceDefaultMethod, None, bool, schemas.Unset] = schemas.unset,
        tokeniseCard: typing.Union[MetaOapg.properties.tokeniseCard, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CheckoutOptions':
        return super().__new__(
            cls,
            *args,
            defaultPaymentMethod=defaultPaymentMethod,
            forceDefaultMethod=forceDefaultMethod,
            tokeniseCard=tokeniseCard,
            _configuration=_configuration,
            **kwargs,
        )
