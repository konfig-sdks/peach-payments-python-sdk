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


class CartCartItemsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[\s\S]{1,2048}$',
                    }]
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[\s\S]{1,255}$',
                    }]
            
            
            class merchantItemId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[\s\S]{1,255}$',
                    }]
            
            
            class quantity(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 999999
                    inclusive_minimum = 1
            
            
            class price(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[0-9]{1,10}\.[0-9]{2}$',
                    }]
            
            
            class weightInKg(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 999999.99
                    inclusive_minimum = 0.01
            
            
            class category(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[\s\S]{1,256}$',
                    }]
            __annotations__ = {
                "description": description,
                "name": name,
                "merchantItemId": merchantItemId,
                "quantity": quantity,
                "price": price,
                "weightInKg": weightInKg,
                "category": category,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantItemId"]) -> MetaOapg.properties.merchantItemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weightInKg"]) -> MetaOapg.properties.weightInKg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "merchantItemId", "quantity", "price", "weightInKg", "category", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantItemId"]) -> typing.Union[MetaOapg.properties.merchantItemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> typing.Union[MetaOapg.properties.quantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weightInKg"]) -> typing.Union[MetaOapg.properties.weightInKg, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "merchantItemId", "quantity", "price", "weightInKg", "category", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        merchantItemId: typing.Union[MetaOapg.properties.merchantItemId, str, schemas.Unset] = schemas.unset,
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, str, schemas.Unset] = schemas.unset,
        weightInKg: typing.Union[MetaOapg.properties.weightInKg, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CartCartItemsItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            name=name,
            merchantItemId=merchantItemId,
            quantity=quantity,
            price=price,
            weightInKg=weightInKg,
            category=category,
            _configuration=_configuration,
            **kwargs,
        )
