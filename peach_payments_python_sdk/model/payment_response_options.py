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


class PaymentResponseOptions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            sendEmail = schemas.BoolSchema
            sendSms = schemas.BoolSchema
            sendWhatsapp = schemas.BoolSchema
            
            
            class emailCc(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'emailCc':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class emailBcc(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'emailBcc':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            notificationUrl = schemas.StrSchema
            __annotations__ = {
                "sendEmail": sendEmail,
                "sendSms": sendSms,
                "sendWhatsapp": sendWhatsapp,
                "emailCc": emailCc,
                "emailBcc": emailBcc,
                "notificationUrl": notificationUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sendEmail"]) -> MetaOapg.properties.sendEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sendSms"]) -> MetaOapg.properties.sendSms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sendWhatsapp"]) -> MetaOapg.properties.sendWhatsapp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailCc"]) -> MetaOapg.properties.emailCc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailBcc"]) -> MetaOapg.properties.emailBcc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationUrl"]) -> MetaOapg.properties.notificationUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sendEmail", "sendSms", "sendWhatsapp", "emailCc", "emailBcc", "notificationUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sendEmail"]) -> typing.Union[MetaOapg.properties.sendEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sendSms"]) -> typing.Union[MetaOapg.properties.sendSms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sendWhatsapp"]) -> typing.Union[MetaOapg.properties.sendWhatsapp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailCc"]) -> typing.Union[MetaOapg.properties.emailCc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailBcc"]) -> typing.Union[MetaOapg.properties.emailBcc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationUrl"]) -> typing.Union[MetaOapg.properties.notificationUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sendEmail", "sendSms", "sendWhatsapp", "emailCc", "emailBcc", "notificationUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sendEmail: typing.Union[MetaOapg.properties.sendEmail, bool, schemas.Unset] = schemas.unset,
        sendSms: typing.Union[MetaOapg.properties.sendSms, bool, schemas.Unset] = schemas.unset,
        sendWhatsapp: typing.Union[MetaOapg.properties.sendWhatsapp, bool, schemas.Unset] = schemas.unset,
        emailCc: typing.Union[MetaOapg.properties.emailCc, None, str, schemas.Unset] = schemas.unset,
        emailBcc: typing.Union[MetaOapg.properties.emailBcc, None, str, schemas.Unset] = schemas.unset,
        notificationUrl: typing.Union[MetaOapg.properties.notificationUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentResponseOptions':
        return super().__new__(
            cls,
            *args,
            sendEmail=sendEmail,
            sendSms=sendSms,
            sendWhatsapp=sendWhatsapp,
            emailCc=emailCc,
            emailBcc=emailBcc,
            notificationUrl=notificationUrl,
            _configuration=_configuration,
            **kwargs,
        )
