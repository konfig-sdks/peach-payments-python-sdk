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


class CheckoutV2Shipping(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class street1(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = '[\s\S]{1,100}'
                    max_length = 100
                    min_length = 1
            
            
            class street2(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = '[\s\S]{1,100}'
                    max_length = 100
                    min_length = 1
            
            
            class city(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = '[\s\S]{1,80}'
                    max_length = 80
                    min_length = 1
            
            
            class company(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = '[\s\S]{1,64}'
                    max_length = 64
                    min_length = 1
            
            
            class postcode(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = '[\s\S]{1,30}'
                    max_length = 30
                    min_length = 1
            
            
            class country(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'ISO 3166-1'
                    max_length = 2
                    min_length = 2
            
            
            class state(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = '[\s\S]{1,50}'
                    max_length = 50
                    min_length = 1
            __annotations__ = {
                "street1": street1,
                "street2": street2,
                "city": city,
                "company": company,
                "postcode": postcode,
                "country": country,
                "state": state,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street1"]) -> MetaOapg.properties.street1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street2"]) -> MetaOapg.properties.street2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company"]) -> MetaOapg.properties.company: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postcode"]) -> MetaOapg.properties.postcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["street1", "street2", "city", "company", "postcode", "country", "state", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street1"]) -> typing.Union[MetaOapg.properties.street1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street2"]) -> typing.Union[MetaOapg.properties.street2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> typing.Union[MetaOapg.properties.company, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postcode"]) -> typing.Union[MetaOapg.properties.postcode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["street1", "street2", "city", "company", "postcode", "country", "state", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        street1: typing.Union[MetaOapg.properties.street1, str, schemas.Unset] = schemas.unset,
        street2: typing.Union[MetaOapg.properties.street2, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        company: typing.Union[MetaOapg.properties.company, str, schemas.Unset] = schemas.unset,
        postcode: typing.Union[MetaOapg.properties.postcode, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CheckoutV2Shipping':
        return super().__new__(
            cls,
            *args,
            street1=street1,
            street2=street2,
            city=city,
            company=company,
            postcode=postcode,
            country=country,
            state=state,
            _configuration=_configuration,
            **kwargs,
        )
