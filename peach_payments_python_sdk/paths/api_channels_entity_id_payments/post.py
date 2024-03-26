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

from peach_payments_python_sdk.model.checkout_options import CheckoutOptions as CheckoutOptionsSchema
from peach_payments_python_sdk.model.message_response import MessageResponse as MessageResponseSchema
from peach_payments_python_sdk.model.generate_link_payment_payment import GenerateLinkPaymentPayment as GenerateLinkPaymentPaymentSchema
from peach_payments_python_sdk.model.customer import Customer as CustomerSchema
from peach_payments_python_sdk.model.generate_link_payment import GenerateLinkPayment as GenerateLinkPaymentSchema
from peach_payments_python_sdk.model.generate_link_error_response import GenerateLinkErrorResponse as GenerateLinkErrorResponseSchema
from peach_payments_python_sdk.model.payment_options import PaymentOptions as PaymentOptionsSchema
from peach_payments_python_sdk.model.generate_link_response import GenerateLinkResponse as GenerateLinkResponseSchema

from peach_payments_python_sdk.type.customer import Customer
from peach_payments_python_sdk.type.generate_link_response import GenerateLinkResponse
from peach_payments_python_sdk.type.checkout_options import CheckoutOptions
from peach_payments_python_sdk.type.message_response import MessageResponse
from peach_payments_python_sdk.type.payment_options import PaymentOptions
from peach_payments_python_sdk.type.generate_link_error_response import GenerateLinkErrorResponse
from peach_payments_python_sdk.type.generate_link_payment_payment import GenerateLinkPaymentPayment
from peach_payments_python_sdk.type.generate_link_payment import GenerateLinkPayment

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.checkout_options import CheckoutOptions as CheckoutOptionsPydantic
from peach_payments_python_sdk.pydantic.generate_link_payment_payment import GenerateLinkPaymentPayment as GenerateLinkPaymentPaymentPydantic
from peach_payments_python_sdk.pydantic.generate_link_payment import GenerateLinkPayment as GenerateLinkPaymentPydantic
from peach_payments_python_sdk.pydantic.generate_link_response import GenerateLinkResponse as GenerateLinkResponsePydantic
from peach_payments_python_sdk.pydantic.payment_options import PaymentOptions as PaymentOptionsPydantic
from peach_payments_python_sdk.pydantic.customer import Customer as CustomerPydantic
from peach_payments_python_sdk.pydantic.message_response import MessageResponse as MessageResponsePydantic
from peach_payments_python_sdk.pydantic.generate_link_error_response import GenerateLinkErrorResponse as GenerateLinkErrorResponsePydantic

from . import path

# Path params
EntityIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'entityId': typing.Union[EntityIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_entity_id = api_client.PathParameter(
    name="entityId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EntityIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = GenerateLinkPaymentSchema


request_body_generate_link_payment = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'BearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = GenerateLinkResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GenerateLinkResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GenerateLinkResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = GenerateLinkErrorResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: GenerateLinkErrorResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: GenerateLinkErrorResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = MessageResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: MessageResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: MessageResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _generate_link_mapped_args(
        self,
        payment: GenerateLinkPaymentPayment,
        customer: Customer,
        options: PaymentOptions,
        checkout: CheckoutOptions,
        entity_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if payment is not None:
            _body["payment"] = payment
        if customer is not None:
            _body["customer"] = customer
        if options is not None:
            _body["options"] = options
        if checkout is not None:
            _body["checkout"] = checkout
        args.body = _body
        if entity_id is not None:
            _path_params["entityId"] = entity_id
        args.path = _path_params
        return args

    async def _agenerate_link_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Generate link
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_entity_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/channels/{entityId}/payments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_generate_link_payment.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _generate_link_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Generate link
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_entity_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/channels/{entityId}/payments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_generate_link_payment.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class GenerateLinkRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agenerate_link(
        self,
        payment: GenerateLinkPaymentPayment,
        customer: Customer,
        options: PaymentOptions,
        checkout: CheckoutOptions,
        entity_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_link_mapped_args(
            payment=payment,
            customer=customer,
            options=options,
            checkout=checkout,
            entity_id=entity_id,
        )
        return await self._agenerate_link_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def generate_link(
        self,
        payment: GenerateLinkPaymentPayment,
        customer: Customer,
        options: PaymentOptions,
        checkout: CheckoutOptions,
        entity_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_link_mapped_args(
            payment=payment,
            customer=customer,
            options=options,
            checkout=checkout,
            entity_id=entity_id,
        )
        return self._generate_link_oapg(
            body=args.body,
            path_params=args.path,
        )

class GenerateLink(BaseApi):

    async def agenerate_link(
        self,
        payment: GenerateLinkPaymentPayment,
        customer: Customer,
        options: PaymentOptions,
        checkout: CheckoutOptions,
        entity_id: str,
        validate: bool = False,
        **kwargs,
    ) -> GenerateLinkResponsePydantic:
        raw_response = await self.raw.agenerate_link(
            payment=payment,
            customer=customer,
            options=options,
            checkout=checkout,
            entity_id=entity_id,
            **kwargs,
        )
        if validate:
            return GenerateLinkResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GenerateLinkResponsePydantic, raw_response.body)
    
    
    def generate_link(
        self,
        payment: GenerateLinkPaymentPayment,
        customer: Customer,
        options: PaymentOptions,
        checkout: CheckoutOptions,
        entity_id: str,
        validate: bool = False,
    ) -> GenerateLinkResponsePydantic:
        raw_response = self.raw.generate_link(
            payment=payment,
            customer=customer,
            options=options,
            checkout=checkout,
            entity_id=entity_id,
        )
        if validate:
            return GenerateLinkResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GenerateLinkResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        payment: GenerateLinkPaymentPayment,
        customer: Customer,
        options: PaymentOptions,
        checkout: CheckoutOptions,
        entity_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_link_mapped_args(
            payment=payment,
            customer=customer,
            options=options,
            checkout=checkout,
            entity_id=entity_id,
        )
        return await self._agenerate_link_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        payment: GenerateLinkPaymentPayment,
        customer: Customer,
        options: PaymentOptions,
        checkout: CheckoutOptions,
        entity_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_link_mapped_args(
            payment=payment,
            customer=customer,
            options=options,
            checkout=checkout,
            entity_id=entity_id,
        )
        return self._generate_link_oapg(
            body=args.body,
            path_params=args.path,
        )

