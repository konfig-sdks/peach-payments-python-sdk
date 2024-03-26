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

from peach_payments_python_sdk.model.checkout_v2_customer import CheckoutV2Customer as CheckoutV2CustomerSchema
from peach_payments_python_sdk.model.checkout_v2_custom_parameters import CheckoutV2CustomParameters as CheckoutV2CustomParametersSchema
from peach_payments_python_sdk.model.message_response import MessageResponse as MessageResponseSchema
from peach_payments_python_sdk.model.checkout_v2 import CheckoutV2 as CheckoutV2Schema
from peach_payments_python_sdk.model.checkout_v2_shipping import CheckoutV2Shipping as CheckoutV2ShippingSchema
from peach_payments_python_sdk.model.checkout_v2_generation_initiate_checkout_instance_response import CheckoutV2GenerationInitiateCheckoutInstanceResponse as CheckoutV2GenerationInitiateCheckoutInstanceResponseSchema
from peach_payments_python_sdk.model.checkout_v2_billing import CheckoutV2Billing as CheckoutV2BillingSchema

from peach_payments_python_sdk.type.checkout_v2_customer import CheckoutV2Customer
from peach_payments_python_sdk.type.message_response import MessageResponse
from peach_payments_python_sdk.type.checkout_v2_generation_initiate_checkout_instance_response import CheckoutV2GenerationInitiateCheckoutInstanceResponse
from peach_payments_python_sdk.type.checkout_v2_billing import CheckoutV2Billing
from peach_payments_python_sdk.type.checkout_v2_custom_parameters import CheckoutV2CustomParameters
from peach_payments_python_sdk.type.checkout_v2 import CheckoutV2
from peach_payments_python_sdk.type.checkout_v2_shipping import CheckoutV2Shipping

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.checkout_v2_custom_parameters import CheckoutV2CustomParameters as CheckoutV2CustomParametersPydantic
from peach_payments_python_sdk.pydantic.checkout_v2_shipping import CheckoutV2Shipping as CheckoutV2ShippingPydantic
from peach_payments_python_sdk.pydantic.message_response import MessageResponse as MessageResponsePydantic
from peach_payments_python_sdk.pydantic.checkout_v2_billing import CheckoutV2Billing as CheckoutV2BillingPydantic
from peach_payments_python_sdk.pydantic.checkout_v2_customer import CheckoutV2Customer as CheckoutV2CustomerPydantic
from peach_payments_python_sdk.pydantic.checkout_v2_generation_initiate_checkout_instance_response import CheckoutV2GenerationInitiateCheckoutInstanceResponse as CheckoutV2GenerationInitiateCheckoutInstanceResponsePydantic
from peach_payments_python_sdk.pydantic.checkout_v2 import CheckoutV2 as CheckoutV2Pydantic

from . import path

# Header params
RefererSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'Referer': typing.Union[RefererSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_referer = api_client.HeaderParameter(
    name="Referer",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RefererSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CheckoutV2Schema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = CheckoutV2Schema


request_body_checkout_v2 = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
_auth = [
    'BearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = CheckoutV2GenerationInitiateCheckoutInstanceResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CheckoutV2GenerationInitiateCheckoutInstanceResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CheckoutV2GenerationInitiateCheckoutInstanceResponse


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
SchemaFor500ResponseBodyApplicationJson = MessageResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: MessageResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: MessageResponse


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

    def _initiate_checkout_instance_mapped_args(
        self,
        authentication_entity_id: str,
        merchant_transaction_id: str,
        amount: typing.Union[int, float],
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[bool] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters: typing.Optional[CheckoutV2CustomParameters] = None,
        customer: typing.Optional[CheckoutV2Customer] = None,
        billing: typing.Optional[CheckoutV2Billing] = None,
        shipping: typing.Optional[CheckoutV2Shipping] = None,
        create_registration: typing.Optional[bool] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if authentication_entity_id is not None:
            _body["authentication.entityId"] = authentication_entity_id
        if merchant_transaction_id is not None:
            _body["merchantTransactionId"] = merchant_transaction_id
        if amount is not None:
            _body["amount"] = amount
        if currency is not None:
            _body["currency"] = currency
        if nonce is not None:
            _body["nonce"] = nonce
        if shopper_result_url is not None:
            _body["shopperResultUrl"] = shopper_result_url
        if default_payment_method is not None:
            _body["defaultPaymentMethod"] = default_payment_method
        if force_default_method is not None:
            _body["forceDefaultMethod"] = force_default_method
        if merchant_invoice_id is not None:
            _body["merchantInvoiceId"] = merchant_invoice_id
        if cancel_url is not None:
            _body["cancelUrl"] = cancel_url
        if notification_url is not None:
            _body["notificationUrl"] = notification_url
        if custom_parameters is not None:
            _body["customParameters"] = custom_parameters
        if customer is not None:
            _body["customer"] = customer
        if billing is not None:
            _body["billing"] = billing
        if shipping is not None:
            _body["shipping"] = shipping
        if create_registration is not None:
            _body["createRegistration"] = create_registration
        if originator is not None:
            _body["originator"] = originator
        if return_to is not None:
            _body["returnTo"] = return_to
        args.body = _body
        if referer is not None:
            _header_params["Referer"] = referer
        args.header = _header_params
        return args

    async def _ainitiate_checkout_instance_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
        Initiate Checkout
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_referer,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
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
            path_template='/v2/checkout',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_checkout_v2.serialize(body, content_type)
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


    def _initiate_checkout_instance_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
        Initiate Checkout
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_referer,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
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
            path_template='/v2/checkout',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_checkout_v2.serialize(body, content_type)
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


class InitiateCheckoutInstanceRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ainitiate_checkout_instance(
        self,
        authentication_entity_id: str,
        merchant_transaction_id: str,
        amount: typing.Union[int, float],
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[bool] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters: typing.Optional[CheckoutV2CustomParameters] = None,
        customer: typing.Optional[CheckoutV2Customer] = None,
        billing: typing.Optional[CheckoutV2Billing] = None,
        shipping: typing.Optional[CheckoutV2Shipping] = None,
        create_registration: typing.Optional[bool] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initiate_checkout_instance_mapped_args(
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters=custom_parameters,
            customer=customer,
            billing=billing,
            shipping=shipping,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        return await self._ainitiate_checkout_instance_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def initiate_checkout_instance(
        self,
        authentication_entity_id: str,
        merchant_transaction_id: str,
        amount: typing.Union[int, float],
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[bool] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters: typing.Optional[CheckoutV2CustomParameters] = None,
        customer: typing.Optional[CheckoutV2Customer] = None,
        billing: typing.Optional[CheckoutV2Billing] = None,
        shipping: typing.Optional[CheckoutV2Shipping] = None,
        create_registration: typing.Optional[bool] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initiate_checkout_instance_mapped_args(
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters=custom_parameters,
            customer=customer,
            billing=billing,
            shipping=shipping,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        return self._initiate_checkout_instance_oapg(
            body=args.body,
            header_params=args.header,
        )

class InitiateCheckoutInstance(BaseApi):

    async def ainitiate_checkout_instance(
        self,
        authentication_entity_id: str,
        merchant_transaction_id: str,
        amount: typing.Union[int, float],
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[bool] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters: typing.Optional[CheckoutV2CustomParameters] = None,
        customer: typing.Optional[CheckoutV2Customer] = None,
        billing: typing.Optional[CheckoutV2Billing] = None,
        shipping: typing.Optional[CheckoutV2Shipping] = None,
        create_registration: typing.Optional[bool] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CheckoutV2GenerationInitiateCheckoutInstanceResponsePydantic:
        raw_response = await self.raw.ainitiate_checkout_instance(
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters=custom_parameters,
            customer=customer,
            billing=billing,
            shipping=shipping,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
            **kwargs,
        )
        if validate:
            return CheckoutV2GenerationInitiateCheckoutInstanceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CheckoutV2GenerationInitiateCheckoutInstanceResponsePydantic, raw_response.body)
    
    
    def initiate_checkout_instance(
        self,
        authentication_entity_id: str,
        merchant_transaction_id: str,
        amount: typing.Union[int, float],
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[bool] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters: typing.Optional[CheckoutV2CustomParameters] = None,
        customer: typing.Optional[CheckoutV2Customer] = None,
        billing: typing.Optional[CheckoutV2Billing] = None,
        shipping: typing.Optional[CheckoutV2Shipping] = None,
        create_registration: typing.Optional[bool] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CheckoutV2GenerationInitiateCheckoutInstanceResponsePydantic:
        raw_response = self.raw.initiate_checkout_instance(
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters=custom_parameters,
            customer=customer,
            billing=billing,
            shipping=shipping,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        if validate:
            return CheckoutV2GenerationInitiateCheckoutInstanceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CheckoutV2GenerationInitiateCheckoutInstanceResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        authentication_entity_id: str,
        merchant_transaction_id: str,
        amount: typing.Union[int, float],
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[bool] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters: typing.Optional[CheckoutV2CustomParameters] = None,
        customer: typing.Optional[CheckoutV2Customer] = None,
        billing: typing.Optional[CheckoutV2Billing] = None,
        shipping: typing.Optional[CheckoutV2Shipping] = None,
        create_registration: typing.Optional[bool] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initiate_checkout_instance_mapped_args(
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters=custom_parameters,
            customer=customer,
            billing=billing,
            shipping=shipping,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        return await self._ainitiate_checkout_instance_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        authentication_entity_id: str,
        merchant_transaction_id: str,
        amount: typing.Union[int, float],
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[bool] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters: typing.Optional[CheckoutV2CustomParameters] = None,
        customer: typing.Optional[CheckoutV2Customer] = None,
        billing: typing.Optional[CheckoutV2Billing] = None,
        shipping: typing.Optional[CheckoutV2Shipping] = None,
        create_registration: typing.Optional[bool] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initiate_checkout_instance_mapped_args(
            authentication_entity_id=authentication_entity_id,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters=custom_parameters,
            customer=customer,
            billing=billing,
            shipping=shipping,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        return self._initiate_checkout_instance_oapg(
            body=args.body,
            header_params=args.header,
        )

