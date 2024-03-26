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


class Error400Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Error object describing the 400 status code error.
    """


    class MetaOapg:
        required = {
            "result",
            "timestamp",
        }
        
        class properties:
        
            @staticmethod
            def result() -> typing.Type['Error400Result']:
                return Error400Result
            timestamp = schemas.DateTimeSchema
        
            @staticmethod
            def resultDetails() -> typing.Type['ResultDetails']:
                return ResultDetails
            __annotations__ = {
                "result": result,
                "timestamp": timestamp,
                "resultDetails": resultDetails,
            }
    
    result: 'Error400Result'
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> 'Error400Result': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resultDetails"]) -> 'ResultDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["result", "timestamp", "resultDetails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> 'Error400Result': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resultDetails"]) -> typing.Union['ResultDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["result", "timestamp", "resultDetails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        result: 'Error400Result',
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        resultDetails: typing.Union['ResultDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Error400Response':
        return super().__new__(
            cls,
            *args,
            result=result,
            timestamp=timestamp,
            resultDetails=resultDetails,
            _configuration=_configuration,
            **kwargs,
        )

from peach_payments_python_sdk.model.error400_result import Error400Result
from peach_payments_python_sdk.model.result_details import ResultDetails
