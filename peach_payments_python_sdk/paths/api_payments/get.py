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

from peach_payments_python_sdk.model.payment_get_all_payment_links200_response import PaymentGetAllPaymentLinks200Response as PaymentGetAllPaymentLinks200ResponseSchema
from peach_payments_python_sdk.model.message_response import MessageResponse as MessageResponseSchema
from peach_payments_python_sdk.model.payment_get_all_payment_links_response import PaymentGetAllPaymentLinksResponse as PaymentGetAllPaymentLinksResponseSchema

from peach_payments_python_sdk.type.payment_get_all_payment_links200_response import PaymentGetAllPaymentLinks200Response
from peach_payments_python_sdk.type.message_response import MessageResponse
from peach_payments_python_sdk.type.payment_get_all_payment_links_response import PaymentGetAllPaymentLinksResponse

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.payment_get_all_payment_links_response import PaymentGetAllPaymentLinksResponse as PaymentGetAllPaymentLinksResponsePydantic
from peach_payments_python_sdk.pydantic.message_response import MessageResponse as MessageResponsePydantic
from peach_payments_python_sdk.pydantic.payment_get_all_payment_links200_response import PaymentGetAllPaymentLinks200Response as PaymentGetAllPaymentLinks200ResponsePydantic

from . import path

# Query params
MerchantSchema = schemas.StrSchema
OffsetSchema = schemas.IntSchema
PerPageSchema = schemas.IntSchema
FiltersStartDateSchema = schemas.DateTimeSchema
FiltersEndDateSchema = schemas.DateTimeSchema


class FiltersStatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "initiated": "INITIATED",
            "processing": "PROCESSING",
            "expired": "EXPIRED",
            "cancelled": "CANCELLED",
            "completed": "COMPLETED",
        }
    
    @schemas.classproperty
    def INITIATED(cls):
        return cls("initiated")
    
    @schemas.classproperty
    def PROCESSING(cls):
        return cls("processing")
    
    @schemas.classproperty
    def EXPIRED(cls):
        return cls("expired")
    
    @schemas.classproperty
    def CANCELLED(cls):
        return cls("cancelled")
    
    @schemas.classproperty
    def COMPLETED(cls):
        return cls("completed")
FiltersAmountValueSchema = schemas.NumberSchema


class FiltersAmountOperatorSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "lt": "LT",
            "lte": "LTE",
            "gt": "GT",
            "gte": "GTE",
            "eq": "EQ",
        }
    
    @schemas.classproperty
    def LT(cls):
        return cls("lt")
    
    @schemas.classproperty
    def LTE(cls):
        return cls("lte")
    
    @schemas.classproperty
    def GT(cls):
        return cls("gt")
    
    @schemas.classproperty
    def GTE(cls):
        return cls("gte")
    
    @schemas.classproperty
    def EQ(cls):
        return cls("eq")


class FiltersSendingOptionsSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "sendEmail": "SEND_EMAIL",
            "sendSms": "SEND_SMS",
            "sendWhatsapp": "SEND_WHATSAPP",
            "emailCc": "EMAIL_CC",
            "emailBcc": "EMAIL_BCC",
        }
    
    @schemas.classproperty
    def SEND_EMAIL(cls):
        return cls("sendEmail")
    
    @schemas.classproperty
    def SEND_SMS(cls):
        return cls("sendSms")
    
    @schemas.classproperty
    def SEND_WHATSAPP(cls):
        return cls("sendWhatsapp")
    
    @schemas.classproperty
    def EMAIL_CC(cls):
        return cls("emailCc")
    
    @schemas.classproperty
    def EMAIL_BCC(cls):
        return cls("emailBcc")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'merchant': typing.Union[MerchantSchema, str, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'perPage': typing.Union[PerPageSchema, decimal.Decimal, int, ],
        'filters[startDate]': typing.Union[FiltersStartDateSchema, str, datetime, ],
        'filters[endDate]': typing.Union[FiltersEndDateSchema, str, datetime, ],
        'filters[status]': typing.Union[FiltersStatusSchema, str, ],
        'filters[amountValue]': typing.Union[FiltersAmountValueSchema, decimal.Decimal, int, float, ],
        'filters[amountOperator]': typing.Union[FiltersAmountOperatorSchema, str, ],
        'filters[sendingOptions]': typing.Union[FiltersSendingOptionsSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_merchant = api_client.QueryParameter(
    name="merchant",
    style=api_client.ParameterStyle.FORM,
    schema=MerchantSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_per_page = api_client.QueryParameter(
    name="perPage",
    style=api_client.ParameterStyle.FORM,
    schema=PerPageSchema,
    explode=True,
)
request_query_filters_start_date = api_client.QueryParameter(
    name="filters[startDate]",
    style=api_client.ParameterStyle.FORM,
    schema=FiltersStartDateSchema,
    explode=True,
)
request_query_filters_end_date = api_client.QueryParameter(
    name="filters[endDate]",
    style=api_client.ParameterStyle.FORM,
    schema=FiltersEndDateSchema,
    explode=True,
)
request_query_filters_status = api_client.QueryParameter(
    name="filters[status]",
    style=api_client.ParameterStyle.FORM,
    schema=FiltersStatusSchema,
    explode=True,
)
request_query_filters_amount_value = api_client.QueryParameter(
    name="filters[amountValue]",
    style=api_client.ParameterStyle.FORM,
    schema=FiltersAmountValueSchema,
    explode=True,
)
request_query_filters_amount_operator = api_client.QueryParameter(
    name="filters[amountOperator]",
    style=api_client.ParameterStyle.FORM,
    schema=FiltersAmountOperatorSchema,
    explode=True,
)
request_query_filters_sending_options = api_client.QueryParameter(
    name="filters[sendingOptions]",
    style=api_client.ParameterStyle.FORM,
    schema=FiltersSendingOptionsSchema,
    explode=True,
)
_auth = [
    'BearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = PaymentGetAllPaymentLinksResponseSchema
SchemaFor200ResponseBodyTextCsv = PaymentGetAllPaymentLinks200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentGetAllPaymentLinksResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentGetAllPaymentLinksResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/csv': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextCsv),
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
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
    'text/csv',
)


class BaseApi(api_client.Api):

    def _get_all_payment_links_mapped_args(
        self,
        merchant: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        filters_start_date: typing.Optional[datetime] = None,
        filters_end_date: typing.Optional[datetime] = None,
        filters_status: typing.Optional[str] = None,
        filters_amount_value: typing.Optional[typing.Union[int, float]] = None,
        filters_amount_operator: typing.Optional[str] = None,
        filters_sending_options: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if merchant is not None:
            _query_params["merchant"] = merchant
        if offset is not None:
            _query_params["offset"] = offset
        if per_page is not None:
            _query_params["perPage"] = per_page
        if filters_start_date is not None:
            _query_params["filters[startDate]"] = filters_start_date
        if filters_end_date is not None:
            _query_params["filters[endDate]"] = filters_end_date
        if filters_status is not None:
            _query_params["filters[status]"] = filters_status
        if filters_amount_value is not None:
            _query_params["filters[amountValue]"] = filters_amount_value
        if filters_amount_operator is not None:
            _query_params["filters[amountOperator]"] = filters_amount_operator
        if filters_sending_options is not None:
            _query_params["filters[sendingOptions]"] = filters_sending_options
        args.query = _query_params
        return args

    async def _aget_all_payment_links_oapg(
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
        Retrieve or export all payment links
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_merchant,
            request_query_offset,
            request_query_per_page,
            request_query_filters_start_date,
            request_query_filters_end_date,
            request_query_filters_status,
            request_query_filters_amount_value,
            request_query_filters_amount_operator,
            request_query_filters_sending_options,
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
            path_template='/api/payments',
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


    def _get_all_payment_links_oapg(
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
        Retrieve or export all payment links
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_merchant,
            request_query_offset,
            request_query_per_page,
            request_query_filters_start_date,
            request_query_filters_end_date,
            request_query_filters_status,
            request_query_filters_amount_value,
            request_query_filters_amount_operator,
            request_query_filters_sending_options,
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
            path_template='/api/payments',
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


class GetAllPaymentLinksRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all_payment_links(
        self,
        merchant: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        filters_start_date: typing.Optional[datetime] = None,
        filters_end_date: typing.Optional[datetime] = None,
        filters_status: typing.Optional[str] = None,
        filters_amount_value: typing.Optional[typing.Union[int, float]] = None,
        filters_amount_operator: typing.Optional[str] = None,
        filters_sending_options: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_payment_links_mapped_args(
            merchant=merchant,
            offset=offset,
            per_page=per_page,
            filters_start_date=filters_start_date,
            filters_end_date=filters_end_date,
            filters_status=filters_status,
            filters_amount_value=filters_amount_value,
            filters_amount_operator=filters_amount_operator,
            filters_sending_options=filters_sending_options,
        )
        return await self._aget_all_payment_links_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_all_payment_links(
        self,
        merchant: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        filters_start_date: typing.Optional[datetime] = None,
        filters_end_date: typing.Optional[datetime] = None,
        filters_status: typing.Optional[str] = None,
        filters_amount_value: typing.Optional[typing.Union[int, float]] = None,
        filters_amount_operator: typing.Optional[str] = None,
        filters_sending_options: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_payment_links_mapped_args(
            merchant=merchant,
            offset=offset,
            per_page=per_page,
            filters_start_date=filters_start_date,
            filters_end_date=filters_end_date,
            filters_status=filters_status,
            filters_amount_value=filters_amount_value,
            filters_amount_operator=filters_amount_operator,
            filters_sending_options=filters_sending_options,
        )
        return self._get_all_payment_links_oapg(
            query_params=args.query,
        )

class GetAllPaymentLinks(BaseApi):

    async def aget_all_payment_links(
        self,
        merchant: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        filters_start_date: typing.Optional[datetime] = None,
        filters_end_date: typing.Optional[datetime] = None,
        filters_status: typing.Optional[str] = None,
        filters_amount_value: typing.Optional[typing.Union[int, float]] = None,
        filters_amount_operator: typing.Optional[str] = None,
        filters_sending_options: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaymentGetAllPaymentLinksResponsePydantic:
        raw_response = await self.raw.aget_all_payment_links(
            merchant=merchant,
            offset=offset,
            per_page=per_page,
            filters_start_date=filters_start_date,
            filters_end_date=filters_end_date,
            filters_status=filters_status,
            filters_amount_value=filters_amount_value,
            filters_amount_operator=filters_amount_operator,
            filters_sending_options=filters_sending_options,
            **kwargs,
        )
        if validate:
            return PaymentGetAllPaymentLinksResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentGetAllPaymentLinksResponsePydantic, raw_response.body)
    
    
    def get_all_payment_links(
        self,
        merchant: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        filters_start_date: typing.Optional[datetime] = None,
        filters_end_date: typing.Optional[datetime] = None,
        filters_status: typing.Optional[str] = None,
        filters_amount_value: typing.Optional[typing.Union[int, float]] = None,
        filters_amount_operator: typing.Optional[str] = None,
        filters_sending_options: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PaymentGetAllPaymentLinksResponsePydantic:
        raw_response = self.raw.get_all_payment_links(
            merchant=merchant,
            offset=offset,
            per_page=per_page,
            filters_start_date=filters_start_date,
            filters_end_date=filters_end_date,
            filters_status=filters_status,
            filters_amount_value=filters_amount_value,
            filters_amount_operator=filters_amount_operator,
            filters_sending_options=filters_sending_options,
        )
        if validate:
            return PaymentGetAllPaymentLinksResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentGetAllPaymentLinksResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        merchant: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        filters_start_date: typing.Optional[datetime] = None,
        filters_end_date: typing.Optional[datetime] = None,
        filters_status: typing.Optional[str] = None,
        filters_amount_value: typing.Optional[typing.Union[int, float]] = None,
        filters_amount_operator: typing.Optional[str] = None,
        filters_sending_options: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_payment_links_mapped_args(
            merchant=merchant,
            offset=offset,
            per_page=per_page,
            filters_start_date=filters_start_date,
            filters_end_date=filters_end_date,
            filters_status=filters_status,
            filters_amount_value=filters_amount_value,
            filters_amount_operator=filters_amount_operator,
            filters_sending_options=filters_sending_options,
        )
        return await self._aget_all_payment_links_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        merchant: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        filters_start_date: typing.Optional[datetime] = None,
        filters_end_date: typing.Optional[datetime] = None,
        filters_status: typing.Optional[str] = None,
        filters_amount_value: typing.Optional[typing.Union[int, float]] = None,
        filters_amount_operator: typing.Optional[str] = None,
        filters_sending_options: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_payment_links_mapped_args(
            merchant=merchant,
            offset=offset,
            per_page=per_page,
            filters_start_date=filters_start_date,
            filters_end_date=filters_end_date,
            filters_status=filters_status,
            filters_amount_value=filters_amount_value,
            filters_amount_operator=filters_amount_operator,
            filters_sending_options=filters_sending_options,
        )
        return self._get_all_payment_links_oapg(
            query_params=args.query,
        )

