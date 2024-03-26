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
from peach_payments_python_sdk.model.currency import Currency as CurrencySchema
from peach_payments_python_sdk.model.error400_response import Error400Response as Error400ResponseSchema
from peach_payments_python_sdk.model.payments_api_inbound_refund_transaction_response import PaymentsApiInboundRefundTransactionResponse as PaymentsApiInboundRefundTransactionResponseSchema
from peach_payments_python_sdk.model.payments_api_inbound_refund_transaction502_response import PaymentsApiInboundRefundTransaction502Response as PaymentsApiInboundRefundTransaction502ResponseSchema
from peach_payments_python_sdk.model.unique_id import UniqueId as UniqueIdSchema
from peach_payments_python_sdk.model.refund_request import RefundRequest as RefundRequestSchema
from peach_payments_python_sdk.model.amount import Amount as AmountSchema
from peach_payments_python_sdk.model.authentication import Authentication as AuthenticationSchema
from peach_payments_python_sdk.model.refund_payment_type import RefundPaymentType as RefundPaymentTypeSchema

from peach_payments_python_sdk.type.error_response import ErrorResponse
from peach_payments_python_sdk.type.unique_id import UniqueId
from peach_payments_python_sdk.type.payments_api_inbound_refund_transaction502_response import PaymentsApiInboundRefundTransaction502Response
from peach_payments_python_sdk.type.refund_payment_type import RefundPaymentType
from peach_payments_python_sdk.type.authentication import Authentication
from peach_payments_python_sdk.type.currency import Currency
from peach_payments_python_sdk.type.amount import Amount
from peach_payments_python_sdk.type.payments_api_inbound_refund_transaction_response import PaymentsApiInboundRefundTransactionResponse
from peach_payments_python_sdk.type.refund_request import RefundRequest
from peach_payments_python_sdk.type.error400_response import Error400Response

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.refund_request import RefundRequest as RefundRequestPydantic
from peach_payments_python_sdk.pydantic.authentication import Authentication as AuthenticationPydantic
from peach_payments_python_sdk.pydantic.refund_payment_type import RefundPaymentType as RefundPaymentTypePydantic
from peach_payments_python_sdk.pydantic.amount import Amount as AmountPydantic
from peach_payments_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from peach_payments_python_sdk.pydantic.payments_api_inbound_refund_transaction_response import PaymentsApiInboundRefundTransactionResponse as PaymentsApiInboundRefundTransactionResponsePydantic
from peach_payments_python_sdk.pydantic.error400_response import Error400Response as Error400ResponsePydantic
from peach_payments_python_sdk.pydantic.currency import Currency as CurrencyPydantic
from peach_payments_python_sdk.pydantic.payments_api_inbound_refund_transaction502_response import PaymentsApiInboundRefundTransaction502Response as PaymentsApiInboundRefundTransaction502ResponsePydantic
from peach_payments_python_sdk.pydantic.unique_id import UniqueId as UniqueIdPydantic

from . import path

# Path params
UniqueIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'uniqueId': typing.Union[UniqueIdSchema, ],
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


request_path_unique_id = api_client.PathParameter(
    name="uniqueId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UniqueIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = RefundRequestSchema


request_body_refund_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'BearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = PaymentsApiInboundRefundTransactionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentsApiInboundRefundTransactionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentsApiInboundRefundTransactionResponse


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
SchemaFor502ResponseBodyApplicationJson = PaymentsApiInboundRefundTransaction502ResponseSchema


@dataclass
class ApiResponseFor502(api_client.ApiResponse):
    body: PaymentsApiInboundRefundTransaction502Response


@dataclass
class ApiResponseFor502Async(api_client.AsyncApiResponse):
    body: PaymentsApiInboundRefundTransaction502Response


_response_for_502 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor502,
    response_cls_async=ApiResponseFor502Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor502ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
    '500': _response_for_500,
    '502': _response_for_502,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _refund_transaction_mapped_args(
        self,
        authentication: Authentication,
        amount: Amount,
        currency: Currency,
        payment_type: RefundPaymentType,
        unique_id: UniqueId,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if authentication is not None:
            _body["authentication"] = authentication
        if amount is not None:
            _body["amount"] = amount
        if currency is not None:
            _body["currency"] = currency
        if payment_type is not None:
            _body["paymentType"] = payment_type
        args.body = _body
        if unique_id is not None:
            _path_params["uniqueId"] = unique_id
        args.path = _path_params
        return args

    async def _arefund_transaction_oapg(
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
        Refund
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_unique_id,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payments/{uniqueId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_refund_request.serialize(body, content_type)
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


    def _refund_transaction_oapg(
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
        Refund
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_unique_id,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payments/{uniqueId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_refund_request.serialize(body, content_type)
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


class RefundTransactionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arefund_transaction(
        self,
        authentication: Authentication,
        amount: Amount,
        currency: Currency,
        payment_type: RefundPaymentType,
        unique_id: UniqueId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._refund_transaction_mapped_args(
            authentication=authentication,
            amount=amount,
            currency=currency,
            payment_type=payment_type,
            unique_id=unique_id,
        )
        return await self._arefund_transaction_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def refund_transaction(
        self,
        authentication: Authentication,
        amount: Amount,
        currency: Currency,
        payment_type: RefundPaymentType,
        unique_id: UniqueId,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._refund_transaction_mapped_args(
            authentication=authentication,
            amount=amount,
            currency=currency,
            payment_type=payment_type,
            unique_id=unique_id,
        )
        return self._refund_transaction_oapg(
            body=args.body,
            path_params=args.path,
        )

class RefundTransaction(BaseApi):

    async def arefund_transaction(
        self,
        authentication: Authentication,
        amount: Amount,
        currency: Currency,
        payment_type: RefundPaymentType,
        unique_id: UniqueId,
        validate: bool = False,
        **kwargs,
    ) -> PaymentsApiInboundRefundTransactionResponsePydantic:
        raw_response = await self.raw.arefund_transaction(
            authentication=authentication,
            amount=amount,
            currency=currency,
            payment_type=payment_type,
            unique_id=unique_id,
            **kwargs,
        )
        if validate:
            return RootModel[PaymentsApiInboundRefundTransactionResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PaymentsApiInboundRefundTransactionResponsePydantic, raw_response.body)
    
    
    def refund_transaction(
        self,
        authentication: Authentication,
        amount: Amount,
        currency: Currency,
        payment_type: RefundPaymentType,
        unique_id: UniqueId,
        validate: bool = False,
    ) -> PaymentsApiInboundRefundTransactionResponsePydantic:
        raw_response = self.raw.refund_transaction(
            authentication=authentication,
            amount=amount,
            currency=currency,
            payment_type=payment_type,
            unique_id=unique_id,
        )
        if validate:
            return RootModel[PaymentsApiInboundRefundTransactionResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PaymentsApiInboundRefundTransactionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        authentication: Authentication,
        amount: Amount,
        currency: Currency,
        payment_type: RefundPaymentType,
        unique_id: UniqueId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._refund_transaction_mapped_args(
            authentication=authentication,
            amount=amount,
            currency=currency,
            payment_type=payment_type,
            unique_id=unique_id,
        )
        return await self._arefund_transaction_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        authentication: Authentication,
        amount: Amount,
        currency: Currency,
        payment_type: RefundPaymentType,
        unique_id: UniqueId,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._refund_transaction_mapped_args(
            authentication=authentication,
            amount=amount,
            currency=currency,
            payment_type=payment_type,
            unique_id=unique_id,
        )
        return self._refund_transaction_oapg(
            body=args.body,
            path_params=args.path,
        )

