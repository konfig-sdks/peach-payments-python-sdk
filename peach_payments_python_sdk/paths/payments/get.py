# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from peach_payments_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from peach_payments_python_sdk.api_response import AsyncGeneratorResponse
from peach_payments_python_sdk import api_client, exceptions
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

from peach_payments_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema
from peach_payments_python_sdk.model.user_id import UserId as UserIdSchema
from peach_payments_python_sdk.model.error400_response import Error400Response as Error400ResponseSchema
from peach_payments_python_sdk.model.merchant_transaction_id import MerchantTransactionId as MerchantTransactionIdSchema
from peach_payments_python_sdk.model.entity_id import EntityId as EntityIdSchema
from peach_payments_python_sdk.model.merchant_transaction_id_status_response import MerchantTransactionIdStatusResponse as MerchantTransactionIdStatusResponseSchema

from peach_payments_python_sdk.type.user_id import UserId
from peach_payments_python_sdk.type.error_response import ErrorResponse
from peach_payments_python_sdk.type.entity_id import EntityId
from peach_payments_python_sdk.type.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.type.error400_response import Error400Response
from peach_payments_python_sdk.type.merchant_transaction_id_status_response import MerchantTransactionIdStatusResponse

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.user_id import UserId as UserIdPydantic
from peach_payments_python_sdk.pydantic.merchant_transaction_id_status_response import MerchantTransactionIdStatusResponse as MerchantTransactionIdStatusResponsePydantic
from peach_payments_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from peach_payments_python_sdk.pydantic.error400_response import Error400Response as Error400ResponsePydantic
from peach_payments_python_sdk.pydantic.merchant_transaction_id import MerchantTransactionId as MerchantTransactionIdPydantic
from peach_payments_python_sdk.pydantic.entity_id import EntityId as EntityIdPydantic

from . import path

# Query params
AuthenticationUserIdSchema = schemas.Schema
AuthenticationPasswordSchema = schemas.StrSchema
AuthenticationEntityIdSchema = schemas.Schema
MerchantTransactionIdSchema = schemas.Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'authentication.userId': typing.Union[UserIdSchema, ],
        'authentication.password': typing.Union[AuthenticationPasswordSchema, str, ],
        'authentication.entityId': typing.Union[EntityIdSchema, ],
        'merchantTransactionId': typing.Union[MerchantTransactionIdSchema, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_authentication_user_id = api_client.QueryParameter(
    name="authentication.userId",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdSchema,
    required=True,
    explode=True,
)
request_query_authentication_password = api_client.QueryParameter(
    name="authentication.password",
    style=api_client.ParameterStyle.FORM,
    schema=AuthenticationPasswordSchema,
    required=True,
    explode=True,
)
request_query_authentication_entity_id = api_client.QueryParameter(
    name="authentication.entityId",
    style=api_client.ParameterStyle.FORM,
    schema=EntityIdSchema,
    required=True,
    explode=True,
)
request_query_merchant_transaction_id = api_client.QueryParameter(
    name="merchantTransactionId",
    style=api_client.ParameterStyle.FORM,
    schema=MerchantTransactionIdSchema,
    required=True,
    explode=True,
)
_auth = [
    'BearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = MerchantTransactionIdStatusResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: MerchantTransactionIdStatusResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: MerchantTransactionIdStatusResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = Error400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Error400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Error400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _status_mapped_args(
        self,
        authentication_user_id: UserId,
        authentication_password: str,
        authentication_entity_id: EntityId,
        merchant_transaction_id: MerchantTransactionId,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if authentication_user_id is not None:
            _query_params["authentication.userId"] = authentication_user_id
        if authentication_password is not None:
            _query_params["authentication.password"] = authentication_password
        if authentication_entity_id is not None:
            _query_params["authentication.entityId"] = authentication_entity_id
        if merchant_transaction_id is not None:
            _query_params["merchantTransactionId"] = merchant_transaction_id
        args.query = _query_params
        return args

    async def _astatus_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Query a transaction by merchantTransactionId
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_authentication_user_id,
            request_query_authentication_password,
            request_query_authentication_entity_id,
            request_query_merchant_transaction_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payments',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _status_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Query a transaction by merchantTransactionId
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_authentication_user_id,
            request_query_authentication_password,
            request_query_authentication_entity_id,
            request_query_merchant_transaction_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payments',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class StatusRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def astatus(
        self,
        authentication_user_id: UserId,
        authentication_password: str,
        authentication_entity_id: EntityId,
        merchant_transaction_id: MerchantTransactionId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._status_mapped_args(
            authentication_user_id=authentication_user_id,
            authentication_password=authentication_password,
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        return await self._astatus_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def status(
        self,
        authentication_user_id: UserId,
        authentication_password: str,
        authentication_entity_id: EntityId,
        merchant_transaction_id: MerchantTransactionId,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._status_mapped_args(
            authentication_user_id=authentication_user_id,
            authentication_password=authentication_password,
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        return self._status_oapg(
            query_params=args.query,
        )

class Status(BaseApi):

    async def astatus(
        self,
        authentication_user_id: UserId,
        authentication_password: str,
        authentication_entity_id: EntityId,
        merchant_transaction_id: MerchantTransactionId,
        validate: bool = False,
        **kwargs,
    ) -> MerchantTransactionIdStatusResponsePydantic:
        raw_response = await self.raw.astatus(
            authentication_user_id=authentication_user_id,
            authentication_password=authentication_password,
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
            **kwargs,
        )
        if validate:
            return MerchantTransactionIdStatusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MerchantTransactionIdStatusResponsePydantic, raw_response.body)
    
    
    def status(
        self,
        authentication_user_id: UserId,
        authentication_password: str,
        authentication_entity_id: EntityId,
        merchant_transaction_id: MerchantTransactionId,
        validate: bool = False,
    ) -> MerchantTransactionIdStatusResponsePydantic:
        raw_response = self.raw.status(
            authentication_user_id=authentication_user_id,
            authentication_password=authentication_password,
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        if validate:
            return MerchantTransactionIdStatusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MerchantTransactionIdStatusResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        authentication_user_id: UserId,
        authentication_password: str,
        authentication_entity_id: EntityId,
        merchant_transaction_id: MerchantTransactionId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._status_mapped_args(
            authentication_user_id=authentication_user_id,
            authentication_password=authentication_password,
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        return await self._astatus_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        authentication_user_id: UserId,
        authentication_password: str,
        authentication_entity_id: EntityId,
        merchant_transaction_id: MerchantTransactionId,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._status_mapped_args(
            authentication_user_id=authentication_user_id,
            authentication_password=authentication_password,
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        return self._status_oapg(
            query_params=args.query,
        )

