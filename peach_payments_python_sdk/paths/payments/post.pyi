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
from peach_payments_python_sdk.model.virtual_account import VirtualAccount as VirtualAccountSchema
from peach_payments_python_sdk.model.currency import Currency as CurrencySchema
from peach_payments_python_sdk.model.error400_response import Error400Response as Error400ResponseSchema
from peach_payments_python_sdk.model.address import Address as AddressSchema
from peach_payments_python_sdk.model.payment_brand import PaymentBrand as PaymentBrandSchema
from peach_payments_python_sdk.model.merchant_transaction_id import MerchantTransactionId as MerchantTransactionIdSchema
from peach_payments_python_sdk.model.customer import Customer as CustomerSchema
from peach_payments_python_sdk.model.cart import Cart as CartSchema
from peach_payments_python_sdk.model.authentication import Authentication as AuthenticationSchema
from peach_payments_python_sdk.model.merchant_invoice_id import MerchantInvoiceId as MerchantInvoiceIdSchema
from peach_payments_python_sdk.model.amount import Amount as AmountSchema
from peach_payments_python_sdk.model.payments_api_inbound_initiate_debit_transaction_response import PaymentsApiInboundInitiateDebitTransactionResponse as PaymentsApiInboundInitiateDebitTransactionResponseSchema
from peach_payments_python_sdk.model.shopify import Shopify as ShopifySchema
from peach_payments_python_sdk.model.payment_type import PaymentType as PaymentTypeSchema
from peach_payments_python_sdk.model.payment_request import PaymentRequest as PaymentRequestSchema

from peach_payments_python_sdk.type.payment_type import PaymentType
from peach_payments_python_sdk.type.payment_request import PaymentRequest
from peach_payments_python_sdk.type.merchant_invoice_id import MerchantInvoiceId
from peach_payments_python_sdk.type.merchant_transaction_id import MerchantTransactionId
from peach_payments_python_sdk.type.payment_brand import PaymentBrand
from peach_payments_python_sdk.type.customer import Customer
from peach_payments_python_sdk.type.payments_api_inbound_initiate_debit_transaction_response import PaymentsApiInboundInitiateDebitTransactionResponse
from peach_payments_python_sdk.type.error_response import ErrorResponse
from peach_payments_python_sdk.type.authentication import Authentication
from peach_payments_python_sdk.type.currency import Currency
from peach_payments_python_sdk.type.amount import Amount
from peach_payments_python_sdk.type.shopify import Shopify
from peach_payments_python_sdk.type.error400_response import Error400Response
from peach_payments_python_sdk.type.cart import Cart
from peach_payments_python_sdk.type.address import Address
from peach_payments_python_sdk.type.virtual_account import VirtualAccount

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.authentication import Authentication as AuthenticationPydantic
from peach_payments_python_sdk.pydantic.amount import Amount as AmountPydantic
from peach_payments_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from peach_payments_python_sdk.pydantic.merchant_invoice_id import MerchantInvoiceId as MerchantInvoiceIdPydantic
from peach_payments_python_sdk.pydantic.shopify import Shopify as ShopifyPydantic
from peach_payments_python_sdk.pydantic.payment_request import PaymentRequest as PaymentRequestPydantic
from peach_payments_python_sdk.pydantic.payment_type import PaymentType as PaymentTypePydantic
from peach_payments_python_sdk.pydantic.virtual_account import VirtualAccount as VirtualAccountPydantic
from peach_payments_python_sdk.pydantic.error400_response import Error400Response as Error400ResponsePydantic
from peach_payments_python_sdk.pydantic.customer import Customer as CustomerPydantic
from peach_payments_python_sdk.pydantic.merchant_transaction_id import MerchantTransactionId as MerchantTransactionIdPydantic
from peach_payments_python_sdk.pydantic.cart import Cart as CartPydantic
from peach_payments_python_sdk.pydantic.currency import Currency as CurrencyPydantic
from peach_payments_python_sdk.pydantic.payments_api_inbound_initiate_debit_transaction_response import PaymentsApiInboundInitiateDebitTransactionResponse as PaymentsApiInboundInitiateDebitTransactionResponsePydantic
from peach_payments_python_sdk.pydantic.payment_brand import PaymentBrand as PaymentBrandPydantic
from peach_payments_python_sdk.pydantic.address import Address as AddressPydantic

# body param
SchemaForRequestBodyApplicationJson = PaymentRequestSchema


request_body_payment_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = PaymentsApiInboundInitiateDebitTransactionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentsApiInboundInitiateDebitTransactionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentsApiInboundInitiateDebitTransactionResponse


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _initiate_debit_transaction_mapped_args(
        self,
        authentication: Authentication,
        merchant_transaction_id: MerchantTransactionId,
        amount: Amount,
        currency: Currency,
        payment_brand: PaymentBrand,
        payment_type: PaymentType,
        virtual_account: typing.Optional[VirtualAccount] = None,
        shipping: typing.Optional[Address] = None,
        billing: typing.Optional[Address] = None,
        shopify: typing.Optional[Shopify] = None,
        customer: typing.Optional[Customer] = None,
        cart: typing.Optional[Cart] = None,
        merchant_invoice_id: typing.Optional[MerchantInvoiceId] = None,
        shopper_result_url: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if authentication is not None:
            _body["authentication"] = authentication
        if merchant_transaction_id is not None:
            _body["merchantTransactionId"] = merchant_transaction_id
        if amount is not None:
            _body["amount"] = amount
        if currency is not None:
            _body["currency"] = currency
        if payment_brand is not None:
            _body["paymentBrand"] = payment_brand
        if payment_type is not None:
            _body["paymentType"] = payment_type
        if virtual_account is not None:
            _body["virtualAccount"] = virtual_account
        if shipping is not None:
            _body["shipping"] = shipping
        if billing is not None:
            _body["billing"] = billing
        if shopify is not None:
            _body["shopify"] = shopify
        if customer is not None:
            _body["customer"] = customer
        if cart is not None:
            _body["cart"] = cart
        if merchant_invoice_id is not None:
            _body["merchantInvoiceId"] = merchant_invoice_id
        if shopper_result_url is not None:
            _body["shopperResultUrl"] = shopper_result_url
        args.body = _body
        return args

    async def _ainitiate_debit_transaction_oapg(
        self,
        body: typing.Any = None,
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
        Payment
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
            path_template='/payments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_payment_request.serialize(body, content_type)
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


    def _initiate_debit_transaction_oapg(
        self,
        body: typing.Any = None,
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
        Payment
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
            path_template='/payments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_payment_request.serialize(body, content_type)
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


class InitiateDebitTransactionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ainitiate_debit_transaction(
        self,
        authentication: Authentication,
        merchant_transaction_id: MerchantTransactionId,
        amount: Amount,
        currency: Currency,
        payment_brand: PaymentBrand,
        payment_type: PaymentType,
        virtual_account: typing.Optional[VirtualAccount] = None,
        shipping: typing.Optional[Address] = None,
        billing: typing.Optional[Address] = None,
        shopify: typing.Optional[Shopify] = None,
        customer: typing.Optional[Customer] = None,
        cart: typing.Optional[Cart] = None,
        merchant_invoice_id: typing.Optional[MerchantInvoiceId] = None,
        shopper_result_url: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initiate_debit_transaction_mapped_args(
            authentication=authentication,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            payment_brand=payment_brand,
            payment_type=payment_type,
            virtual_account=virtual_account,
            shipping=shipping,
            billing=billing,
            shopify=shopify,
            customer=customer,
            cart=cart,
            merchant_invoice_id=merchant_invoice_id,
            shopper_result_url=shopper_result_url,
        )
        return await self._ainitiate_debit_transaction_oapg(
            body=args.body,
            **kwargs,
        )
    
    def initiate_debit_transaction(
        self,
        authentication: Authentication,
        merchant_transaction_id: MerchantTransactionId,
        amount: Amount,
        currency: Currency,
        payment_brand: PaymentBrand,
        payment_type: PaymentType,
        virtual_account: typing.Optional[VirtualAccount] = None,
        shipping: typing.Optional[Address] = None,
        billing: typing.Optional[Address] = None,
        shopify: typing.Optional[Shopify] = None,
        customer: typing.Optional[Customer] = None,
        cart: typing.Optional[Cart] = None,
        merchant_invoice_id: typing.Optional[MerchantInvoiceId] = None,
        shopper_result_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initiate_debit_transaction_mapped_args(
            authentication=authentication,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            payment_brand=payment_brand,
            payment_type=payment_type,
            virtual_account=virtual_account,
            shipping=shipping,
            billing=billing,
            shopify=shopify,
            customer=customer,
            cart=cart,
            merchant_invoice_id=merchant_invoice_id,
            shopper_result_url=shopper_result_url,
        )
        return self._initiate_debit_transaction_oapg(
            body=args.body,
        )

class InitiateDebitTransaction(BaseApi):

    async def ainitiate_debit_transaction(
        self,
        authentication: Authentication,
        merchant_transaction_id: MerchantTransactionId,
        amount: Amount,
        currency: Currency,
        payment_brand: PaymentBrand,
        payment_type: PaymentType,
        virtual_account: typing.Optional[VirtualAccount] = None,
        shipping: typing.Optional[Address] = None,
        billing: typing.Optional[Address] = None,
        shopify: typing.Optional[Shopify] = None,
        customer: typing.Optional[Customer] = None,
        cart: typing.Optional[Cart] = None,
        merchant_invoice_id: typing.Optional[MerchantInvoiceId] = None,
        shopper_result_url: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaymentsApiInboundInitiateDebitTransactionResponsePydantic:
        raw_response = await self.raw.ainitiate_debit_transaction(
            authentication=authentication,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            payment_brand=payment_brand,
            payment_type=payment_type,
            virtual_account=virtual_account,
            shipping=shipping,
            billing=billing,
            shopify=shopify,
            customer=customer,
            cart=cart,
            merchant_invoice_id=merchant_invoice_id,
            shopper_result_url=shopper_result_url,
            **kwargs,
        )
        if validate:
            return RootModel[PaymentsApiInboundInitiateDebitTransactionResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PaymentsApiInboundInitiateDebitTransactionResponsePydantic, raw_response.body)
    
    
    def initiate_debit_transaction(
        self,
        authentication: Authentication,
        merchant_transaction_id: MerchantTransactionId,
        amount: Amount,
        currency: Currency,
        payment_brand: PaymentBrand,
        payment_type: PaymentType,
        virtual_account: typing.Optional[VirtualAccount] = None,
        shipping: typing.Optional[Address] = None,
        billing: typing.Optional[Address] = None,
        shopify: typing.Optional[Shopify] = None,
        customer: typing.Optional[Customer] = None,
        cart: typing.Optional[Cart] = None,
        merchant_invoice_id: typing.Optional[MerchantInvoiceId] = None,
        shopper_result_url: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PaymentsApiInboundInitiateDebitTransactionResponsePydantic:
        raw_response = self.raw.initiate_debit_transaction(
            authentication=authentication,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            payment_brand=payment_brand,
            payment_type=payment_type,
            virtual_account=virtual_account,
            shipping=shipping,
            billing=billing,
            shopify=shopify,
            customer=customer,
            cart=cart,
            merchant_invoice_id=merchant_invoice_id,
            shopper_result_url=shopper_result_url,
        )
        if validate:
            return RootModel[PaymentsApiInboundInitiateDebitTransactionResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PaymentsApiInboundInitiateDebitTransactionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        authentication: Authentication,
        merchant_transaction_id: MerchantTransactionId,
        amount: Amount,
        currency: Currency,
        payment_brand: PaymentBrand,
        payment_type: PaymentType,
        virtual_account: typing.Optional[VirtualAccount] = None,
        shipping: typing.Optional[Address] = None,
        billing: typing.Optional[Address] = None,
        shopify: typing.Optional[Shopify] = None,
        customer: typing.Optional[Customer] = None,
        cart: typing.Optional[Cart] = None,
        merchant_invoice_id: typing.Optional[MerchantInvoiceId] = None,
        shopper_result_url: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initiate_debit_transaction_mapped_args(
            authentication=authentication,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            payment_brand=payment_brand,
            payment_type=payment_type,
            virtual_account=virtual_account,
            shipping=shipping,
            billing=billing,
            shopify=shopify,
            customer=customer,
            cart=cart,
            merchant_invoice_id=merchant_invoice_id,
            shopper_result_url=shopper_result_url,
        )
        return await self._ainitiate_debit_transaction_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        authentication: Authentication,
        merchant_transaction_id: MerchantTransactionId,
        amount: Amount,
        currency: Currency,
        payment_brand: PaymentBrand,
        payment_type: PaymentType,
        virtual_account: typing.Optional[VirtualAccount] = None,
        shipping: typing.Optional[Address] = None,
        billing: typing.Optional[Address] = None,
        shopify: typing.Optional[Shopify] = None,
        customer: typing.Optional[Customer] = None,
        cart: typing.Optional[Cart] = None,
        merchant_invoice_id: typing.Optional[MerchantInvoiceId] = None,
        shopper_result_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initiate_debit_transaction_mapped_args(
            authentication=authentication,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            currency=currency,
            payment_brand=payment_brand,
            payment_type=payment_type,
            virtual_account=virtual_account,
            shipping=shipping,
            billing=billing,
            shopify=shopify,
            customer=customer,
            cart=cart,
            merchant_invoice_id=merchant_invoice_id,
            shopper_result_url=shopper_result_url,
        )
        return self._initiate_debit_transaction_oapg(
            body=args.body,
        )

