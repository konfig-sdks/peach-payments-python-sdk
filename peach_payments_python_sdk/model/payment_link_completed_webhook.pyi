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


class PaymentLinkCompletedWebhook(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Payment link completed.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    status = schemas.StrSchema
                    
                    
                    class paymentBrand(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def VISA(cls):
                            return cls("VISA")
                        
                        @schemas.classproperty
                        def MASTERCARD(cls):
                            return cls("MASTERCARD")
                        
                        @schemas.classproperty
                        def DINERS_CLUB(cls):
                            return cls("DINERS CLUB")
                        
                        @schemas.classproperty
                        def AMERICAN_EXPRESS(cls):
                            return cls("AMERICAN EXPRESS")
                        
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
                        def STITCHEFT(cls):
                            return cls("STITCHEFT")
                        
                        @schemas.classproperty
                        def FINCHOICEPAY(cls):
                            return cls("FINCHOICEPAY")
                        
                        @schemas.classproperty
                        def BLINKBYEMTEL(cls):
                            return cls("BLINKBYEMTEL")
                        
                        @schemas.classproperty
                        def CAPITECPAY(cls):
                            return cls("CAPITECPAY")
                    registrationId = schemas.StrSchema
                    __annotations__ = {
                        "status": status,
                        "paymentBrand": paymentBrand,
                        "registrationId": registrationId,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["paymentBrand"]) -> MetaOapg.properties.paymentBrand: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["registrationId"]) -> MetaOapg.properties.registrationId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "paymentBrand", "registrationId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["paymentBrand"]) -> typing.Union[MetaOapg.properties.paymentBrand, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["registrationId"]) -> typing.Union[MetaOapg.properties.registrationId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "paymentBrand", "registrationId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                paymentBrand: typing.Union[MetaOapg.properties.paymentBrand, str, schemas.Unset] = schemas.unset,
                registrationId: typing.Union[MetaOapg.properties.registrationId, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    status=status,
                    paymentBrand=paymentBrand,
                    registrationId=registrationId,
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
                PaymentLinkBaseWebhook,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentLinkCompletedWebhook':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from peach_payments_python_sdk.model.payment_link_base_webhook import PaymentLinkBaseWebhook
