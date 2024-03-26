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

from peach_payments_python_sdk.model.files_upload_file_request import FilesUploadFileRequest as FilesUploadFileRequestSchema
from peach_payments_python_sdk.model.message_response import MessageResponse as MessageResponseSchema
from peach_payments_python_sdk.model.files_upload_file_response import FilesUploadFileResponse as FilesUploadFileResponseSchema

from peach_payments_python_sdk.type.message_response import MessageResponse
from peach_payments_python_sdk.type.files_upload_file_response import FilesUploadFileResponse
from peach_payments_python_sdk.type.files_upload_file_request import FilesUploadFileRequest

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.message_response import MessageResponse as MessageResponsePydantic
from peach_payments_python_sdk.pydantic.files_upload_file_request import FilesUploadFileRequest as FilesUploadFileRequestPydantic
from peach_payments_python_sdk.pydantic.files_upload_file_response import FilesUploadFileResponse as FilesUploadFileResponsePydantic

# body param
SchemaForRequestBodyMultipartFormData = FilesUploadFileRequestSchema


request_body_files_upload_file_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
SchemaFor200ResponseBodyApplicationJson = FilesUploadFileResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FilesUploadFileResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FilesUploadFileResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = MessageResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: MessageResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: MessageResponse


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
SchemaFor404ResponseBodyApplicationJson = MessageResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: MessageResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: MessageResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _upload_file_mapped_args(
        self,
        file: typing.Optional[typing.IO] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if file is not None:
            _body["file"] = file
        args.body = _body
        return args

    async def _aupload_file_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Upload a file
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/api/attachments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_files_upload_file_request.serialize(body, content_type)
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


    def _upload_file_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Upload a file
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/api/attachments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_files_upload_file_request.serialize(body, content_type)
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


class UploadFileRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupload_file(
        self,
        file: typing.Optional[typing.IO] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_file_mapped_args(
            file=file,
        )
        return await self._aupload_file_oapg(
            body=args.body,
            **kwargs,
        )
    
    def upload_file(
        self,
        file: typing.Optional[typing.IO] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_file_mapped_args(
            file=file,
        )
        return self._upload_file_oapg(
            body=args.body,
        )

class UploadFile(BaseApi):

    async def aupload_file(
        self,
        file: typing.Optional[typing.IO] = None,
        validate: bool = False,
        **kwargs,
    ) -> FilesUploadFileResponsePydantic:
        raw_response = await self.raw.aupload_file(
            file=file,
            **kwargs,
        )
        if validate:
            return FilesUploadFileResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesUploadFileResponsePydantic, raw_response.body)
    
    
    def upload_file(
        self,
        file: typing.Optional[typing.IO] = None,
        validate: bool = False,
    ) -> FilesUploadFileResponsePydantic:
        raw_response = self.raw.upload_file(
            file=file,
        )
        if validate:
            return FilesUploadFileResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesUploadFileResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        file: typing.Optional[typing.IO] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_file_mapped_args(
            file=file,
        )
        return await self._aupload_file_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        file: typing.Optional[typing.IO] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_file_mapped_args(
            file=file,
        )
        return self._upload_file_oapg(
            body=args.body,
        )

