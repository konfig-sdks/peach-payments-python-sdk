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


class BatchResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "createdAt",
            "successfulRows",
            "filename",
            "entityId",
            "id",
            "totalRows",
            "status",
            "updatedAt",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            
            
            class entityId(
                schemas.StrSchema
            ):
                pass
            
            
            class filename(
                schemas.StrSchema
            ):
                pass
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INITIATED(cls):
                    return cls("initiated")
                
                @schemas.classproperty
                def PROCESSING(cls):
                    return cls("processing")
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("completed")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("error")
            successfulRows = schemas.NumberSchema
            totalRows = schemas.NumberSchema
            errorCode = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "entityId": entityId,
                "filename": filename,
                "status": status,
                "successfulRows": successfulRows,
                "totalRows": totalRows,
                "errorCode": errorCode,
            }
    
    createdAt: MetaOapg.properties.createdAt
    successfulRows: MetaOapg.properties.successfulRows
    filename: MetaOapg.properties.filename
    entityId: MetaOapg.properties.entityId
    id: MetaOapg.properties.id
    totalRows: MetaOapg.properties.totalRows
    status: MetaOapg.properties.status
    updatedAt: MetaOapg.properties.updatedAt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["successfulRows"]) -> MetaOapg.properties.successfulRows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalRows"]) -> MetaOapg.properties.totalRows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorCode"]) -> MetaOapg.properties.errorCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "createdAt", "updatedAt", "entityId", "filename", "status", "successfulRows", "totalRows", "errorCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityId"]) -> MetaOapg.properties.entityId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["successfulRows"]) -> MetaOapg.properties.successfulRows: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalRows"]) -> MetaOapg.properties.totalRows: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorCode"]) -> typing.Union[MetaOapg.properties.errorCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "createdAt", "updatedAt", "entityId", "filename", "status", "successfulRows", "totalRows", "errorCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, ],
        successfulRows: typing.Union[MetaOapg.properties.successfulRows, decimal.Decimal, int, float, ],
        filename: typing.Union[MetaOapg.properties.filename, str, ],
        entityId: typing.Union[MetaOapg.properties.entityId, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        totalRows: typing.Union[MetaOapg.properties.totalRows, decimal.Decimal, int, float, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, ],
        errorCode: typing.Union[MetaOapg.properties.errorCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BatchResponse':
        return super().__new__(
            cls,
            *args,
            createdAt=createdAt,
            successfulRows=successfulRows,
            filename=filename,
            entityId=entityId,
            id=id,
            totalRows=totalRows,
            status=status,
            updatedAt=updatedAt,
            errorCode=errorCode,
            _configuration=_configuration,
            **kwargs,
        )
