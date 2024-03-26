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

from peach_payments_python_sdk.model.checkout_error import CheckoutError as CheckoutErrorSchema
from peach_payments_python_sdk.model.checkout_status import CheckoutStatus as CheckoutStatusSchema

from peach_payments_python_sdk.type.checkout_status import CheckoutStatus
from peach_payments_python_sdk.type.checkout_error import CheckoutError

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.checkout_status import CheckoutStatus as CheckoutStatusPydantic
from peach_payments_python_sdk.pydantic.checkout_error import CheckoutError as CheckoutErrorPydantic

from . import path

# Query params


class AuthenticationEntityIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 64


class CheckoutIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 64


class MerchantTransactionIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 64


class SignatureSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 64
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'authentication.entityId': typing.Union[AuthenticationEntityIdSchema, str, ],
        'signature': typing.Union[SignatureSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'checkoutId': typing.Union[CheckoutIdSchema, str, ],
        'merchantTransactionId': typing.Union[MerchantTransactionIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_authentication_entity_id = api_client.QueryParameter(
    name="authentication.entityId",
    style=api_client.ParameterStyle.FORM,
    schema=AuthenticationEntityIdSchema,
    required=True,
    explode=True,
)
request_query_checkout_id = api_client.QueryParameter(
    name="checkoutId",
    style=api_client.ParameterStyle.FORM,
    schema=CheckoutIdSchema,
    explode=True,
)
request_query_merchant_transaction_id = api_client.QueryParameter(
    name="merchantTransactionId",
    style=api_client.ParameterStyle.FORM,
    schema=MerchantTransactionIdSchema,
    explode=True,
)
request_query_signature = api_client.QueryParameter(
    name="signature",
    style=api_client.ParameterStyle.FORM,
    schema=SignatureSchema,
    required=True,
    explode=True,
)
_auth = [
    'BearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = CheckoutStatusSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CheckoutStatus


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CheckoutStatus


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = CheckoutErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: CheckoutError


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: CheckoutError


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _checkout_status_get_mapped_args(
        self,
        authentication_entity_id: str,
        signature: str,
        checkout_id: typing.Optional[str] = None,
        merchant_transaction_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if authentication_entity_id is not None:
            _query_params["authentication.entityId"] = authentication_entity_id
        if checkout_id is not None:
            _query_params["checkoutId"] = checkout_id
        if merchant_transaction_id is not None:
            _query_params["merchantTransactionId"] = merchant_transaction_id
        if signature is not None:
            _query_params["signature"] = signature
        args.query = _query_params
        return args

    async def _acheckout_status_get_oapg(
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
        Query Checkout status
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_authentication_entity_id,
            request_query_checkout_id,
            request_query_merchant_transaction_id,
            request_query_signature,
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
            path_template='/status',
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


    def _checkout_status_get_oapg(
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
        Query Checkout status
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_authentication_entity_id,
            request_query_checkout_id,
            request_query_merchant_transaction_id,
            request_query_signature,
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
            path_template='/status',
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


class CheckoutStatusGetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acheckout_status_get(
        self,
        authentication_entity_id: str,
        signature: str,
        checkout_id: typing.Optional[str] = None,
        merchant_transaction_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._checkout_status_get_mapped_args(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            checkout_id=checkout_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        return await self._acheckout_status_get_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def checkout_status_get(
        self,
        authentication_entity_id: str,
        signature: str,
        checkout_id: typing.Optional[str] = None,
        merchant_transaction_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._checkout_status_get_mapped_args(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            checkout_id=checkout_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        return self._checkout_status_get_oapg(
            query_params=args.query,
        )

class CheckoutStatusGet(BaseApi):

    async def acheckout_status_get(
        self,
        authentication_entity_id: str,
        signature: str,
        checkout_id: typing.Optional[str] = None,
        merchant_transaction_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CheckoutStatusPydantic:
        raw_response = await self.raw.acheckout_status_get(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            checkout_id=checkout_id,
            merchant_transaction_id=merchant_transaction_id,
            **kwargs,
        )
        if validate:
            return CheckoutStatusPydantic(**raw_response.body)
        return api_client.construct_model_instance(CheckoutStatusPydantic, raw_response.body)
    
    
    def checkout_status_get(
        self,
        authentication_entity_id: str,
        signature: str,
        checkout_id: typing.Optional[str] = None,
        merchant_transaction_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CheckoutStatusPydantic:
        raw_response = self.raw.checkout_status_get(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            checkout_id=checkout_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        if validate:
            return CheckoutStatusPydantic(**raw_response.body)
        return api_client.construct_model_instance(CheckoutStatusPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        authentication_entity_id: str,
        signature: str,
        checkout_id: typing.Optional[str] = None,
        merchant_transaction_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._checkout_status_get_mapped_args(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            checkout_id=checkout_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        return await self._acheckout_status_get_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        authentication_entity_id: str,
        signature: str,
        checkout_id: typing.Optional[str] = None,
        merchant_transaction_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._checkout_status_get_mapped_args(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            checkout_id=checkout_id,
            merchant_transaction_id=merchant_transaction_id,
        )
        return self._checkout_status_get_oapg(
            query_params=args.query,
        )

