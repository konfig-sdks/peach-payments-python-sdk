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

from peach_payments_python_sdk.model.checkout import Checkout as CheckoutSchema
from peach_payments_python_sdk.model.checkout_generation_initiate_redirect_checkout_response import CheckoutGenerationInitiateRedirectCheckoutResponse as CheckoutGenerationInitiateRedirectCheckoutResponseSchema

from peach_payments_python_sdk.type.checkout_generation_initiate_redirect_checkout_response import CheckoutGenerationInitiateRedirectCheckoutResponse
from peach_payments_python_sdk.type.checkout import Checkout

from ...api_client import Dictionary
from peach_payments_python_sdk.pydantic.checkout_generation_initiate_redirect_checkout_response import CheckoutGenerationInitiateRedirectCheckoutResponse as CheckoutGenerationInitiateRedirectCheckoutResponsePydantic
from peach_payments_python_sdk.pydantic.checkout import Checkout as CheckoutPydantic

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
SchemaForRequestBodyApplicationJson = CheckoutSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = CheckoutSchema


request_body_checkout = api_client.RequestBody(
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
SchemaFor201ResponseBodyApplicationJson = CheckoutGenerationInitiateRedirectCheckoutResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: CheckoutGenerationInitiateRedirectCheckoutResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: CheckoutGenerationInitiateRedirectCheckoutResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
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
    '201': _response_for_201,
    '400': _response_for_400,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _initiate_redirect_checkout_mapped_args(
        self,
        authentication_entity_id: str,
        signature: str,
        merchant_transaction_id: str,
        amount: str,
        payment_type: str,
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[str] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters_name: typing.Optional[str] = None,
        customer_merchant_customer_id: typing.Optional[str] = None,
        customer_given_name: typing.Optional[str] = None,
        customer_surname: typing.Optional[str] = None,
        customer_mobile: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        customer_status: typing.Optional[str] = None,
        customer_birth_date: typing.Optional[str] = None,
        customer_ip: typing.Optional[str] = None,
        customer_phone: typing.Optional[str] = None,
        customer_id_number: typing.Optional[str] = None,
        billing_street1: typing.Optional[str] = None,
        billing_street2: typing.Optional[str] = None,
        billing_city: typing.Optional[str] = None,
        billing_company: typing.Optional[str] = None,
        billing_country: typing.Optional[str] = None,
        billing_state: typing.Optional[str] = None,
        billing_postcode: typing.Optional[str] = None,
        shipping_street1: typing.Optional[str] = None,
        shipping_street2: typing.Optional[str] = None,
        shipping_city: typing.Optional[str] = None,
        shipping_company: typing.Optional[str] = None,
        shipping_postcode: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        shipping_state: typing.Optional[str] = None,
        cart_tax: typing.Optional[str] = None,
        cart_shipping_amount: typing.Optional[str] = None,
        cart_discount: typing.Optional[str] = None,
        create_registration: typing.Optional[str] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if authentication_entity_id is not None:
            _body["authentication.entityId"] = authentication_entity_id
        if signature is not None:
            _body["signature"] = signature
        if merchant_transaction_id is not None:
            _body["merchantTransactionId"] = merchant_transaction_id
        if amount is not None:
            _body["amount"] = amount
        if payment_type is not None:
            _body["paymentType"] = payment_type
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
        if custom_parameters_name is not None:
            _body["customParameters[name]"] = custom_parameters_name
        if customer_merchant_customer_id is not None:
            _body["customer.merchantCustomerId"] = customer_merchant_customer_id
        if customer_given_name is not None:
            _body["customer.givenName"] = customer_given_name
        if customer_surname is not None:
            _body["customer.surname"] = customer_surname
        if customer_mobile is not None:
            _body["customer.mobile"] = customer_mobile
        if customer_email is not None:
            _body["customer.email"] = customer_email
        if customer_status is not None:
            _body["customer.status"] = customer_status
        if customer_birth_date is not None:
            _body["customer.birthDate"] = customer_birth_date
        if customer_ip is not None:
            _body["customer.ip"] = customer_ip
        if customer_phone is not None:
            _body["customer.phone"] = customer_phone
        if customer_id_number is not None:
            _body["customer.idNumber"] = customer_id_number
        if billing_street1 is not None:
            _body["billing.street1"] = billing_street1
        if billing_street2 is not None:
            _body["billing.street2"] = billing_street2
        if billing_city is not None:
            _body["billing.city"] = billing_city
        if billing_company is not None:
            _body["billing.company"] = billing_company
        if billing_country is not None:
            _body["billing.country"] = billing_country
        if billing_state is not None:
            _body["billing.state"] = billing_state
        if billing_postcode is not None:
            _body["billing.postcode"] = billing_postcode
        if shipping_street1 is not None:
            _body["shipping.street1"] = shipping_street1
        if shipping_street2 is not None:
            _body["shipping.street2"] = shipping_street2
        if shipping_city is not None:
            _body["shipping.city"] = shipping_city
        if shipping_company is not None:
            _body["shipping.company"] = shipping_company
        if shipping_postcode is not None:
            _body["shipping.postcode"] = shipping_postcode
        if shipping_country is not None:
            _body["shipping.country"] = shipping_country
        if shipping_state is not None:
            _body["shipping.state"] = shipping_state
        if cart_tax is not None:
            _body["cart.tax"] = cart_tax
        if cart_shipping_amount is not None:
            _body["cart.shippingAmount"] = cart_shipping_amount
        if cart_discount is not None:
            _body["cart.discount"] = cart_discount
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

    async def _ainitiate_redirect_checkout_oapg(
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
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Initiate redirect-based Checkout
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
            path_template='/checkout/initiate',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_checkout.serialize(body, content_type)
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


    def _initiate_redirect_checkout_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Initiate redirect-based Checkout
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
            path_template='/checkout/initiate',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_checkout.serialize(body, content_type)
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


class InitiateRedirectCheckoutRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ainitiate_redirect_checkout(
        self,
        authentication_entity_id: str,
        signature: str,
        merchant_transaction_id: str,
        amount: str,
        payment_type: str,
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[str] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters_name: typing.Optional[str] = None,
        customer_merchant_customer_id: typing.Optional[str] = None,
        customer_given_name: typing.Optional[str] = None,
        customer_surname: typing.Optional[str] = None,
        customer_mobile: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        customer_status: typing.Optional[str] = None,
        customer_birth_date: typing.Optional[str] = None,
        customer_ip: typing.Optional[str] = None,
        customer_phone: typing.Optional[str] = None,
        customer_id_number: typing.Optional[str] = None,
        billing_street1: typing.Optional[str] = None,
        billing_street2: typing.Optional[str] = None,
        billing_city: typing.Optional[str] = None,
        billing_company: typing.Optional[str] = None,
        billing_country: typing.Optional[str] = None,
        billing_state: typing.Optional[str] = None,
        billing_postcode: typing.Optional[str] = None,
        shipping_street1: typing.Optional[str] = None,
        shipping_street2: typing.Optional[str] = None,
        shipping_city: typing.Optional[str] = None,
        shipping_company: typing.Optional[str] = None,
        shipping_postcode: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        shipping_state: typing.Optional[str] = None,
        cart_tax: typing.Optional[str] = None,
        cart_shipping_amount: typing.Optional[str] = None,
        cart_discount: typing.Optional[str] = None,
        create_registration: typing.Optional[str] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initiate_redirect_checkout_mapped_args(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            payment_type=payment_type,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters_name=custom_parameters_name,
            customer_merchant_customer_id=customer_merchant_customer_id,
            customer_given_name=customer_given_name,
            customer_surname=customer_surname,
            customer_mobile=customer_mobile,
            customer_email=customer_email,
            customer_status=customer_status,
            customer_birth_date=customer_birth_date,
            customer_ip=customer_ip,
            customer_phone=customer_phone,
            customer_id_number=customer_id_number,
            billing_street1=billing_street1,
            billing_street2=billing_street2,
            billing_city=billing_city,
            billing_company=billing_company,
            billing_country=billing_country,
            billing_state=billing_state,
            billing_postcode=billing_postcode,
            shipping_street1=shipping_street1,
            shipping_street2=shipping_street2,
            shipping_city=shipping_city,
            shipping_company=shipping_company,
            shipping_postcode=shipping_postcode,
            shipping_country=shipping_country,
            shipping_state=shipping_state,
            cart_tax=cart_tax,
            cart_shipping_amount=cart_shipping_amount,
            cart_discount=cart_discount,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        return await self._ainitiate_redirect_checkout_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def initiate_redirect_checkout(
        self,
        authentication_entity_id: str,
        signature: str,
        merchant_transaction_id: str,
        amount: str,
        payment_type: str,
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[str] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters_name: typing.Optional[str] = None,
        customer_merchant_customer_id: typing.Optional[str] = None,
        customer_given_name: typing.Optional[str] = None,
        customer_surname: typing.Optional[str] = None,
        customer_mobile: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        customer_status: typing.Optional[str] = None,
        customer_birth_date: typing.Optional[str] = None,
        customer_ip: typing.Optional[str] = None,
        customer_phone: typing.Optional[str] = None,
        customer_id_number: typing.Optional[str] = None,
        billing_street1: typing.Optional[str] = None,
        billing_street2: typing.Optional[str] = None,
        billing_city: typing.Optional[str] = None,
        billing_company: typing.Optional[str] = None,
        billing_country: typing.Optional[str] = None,
        billing_state: typing.Optional[str] = None,
        billing_postcode: typing.Optional[str] = None,
        shipping_street1: typing.Optional[str] = None,
        shipping_street2: typing.Optional[str] = None,
        shipping_city: typing.Optional[str] = None,
        shipping_company: typing.Optional[str] = None,
        shipping_postcode: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        shipping_state: typing.Optional[str] = None,
        cart_tax: typing.Optional[str] = None,
        cart_shipping_amount: typing.Optional[str] = None,
        cart_discount: typing.Optional[str] = None,
        create_registration: typing.Optional[str] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initiate_redirect_checkout_mapped_args(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            payment_type=payment_type,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters_name=custom_parameters_name,
            customer_merchant_customer_id=customer_merchant_customer_id,
            customer_given_name=customer_given_name,
            customer_surname=customer_surname,
            customer_mobile=customer_mobile,
            customer_email=customer_email,
            customer_status=customer_status,
            customer_birth_date=customer_birth_date,
            customer_ip=customer_ip,
            customer_phone=customer_phone,
            customer_id_number=customer_id_number,
            billing_street1=billing_street1,
            billing_street2=billing_street2,
            billing_city=billing_city,
            billing_company=billing_company,
            billing_country=billing_country,
            billing_state=billing_state,
            billing_postcode=billing_postcode,
            shipping_street1=shipping_street1,
            shipping_street2=shipping_street2,
            shipping_city=shipping_city,
            shipping_company=shipping_company,
            shipping_postcode=shipping_postcode,
            shipping_country=shipping_country,
            shipping_state=shipping_state,
            cart_tax=cart_tax,
            cart_shipping_amount=cart_shipping_amount,
            cart_discount=cart_discount,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        return self._initiate_redirect_checkout_oapg(
            body=args.body,
            header_params=args.header,
        )

class InitiateRedirectCheckout(BaseApi):

    async def ainitiate_redirect_checkout(
        self,
        authentication_entity_id: str,
        signature: str,
        merchant_transaction_id: str,
        amount: str,
        payment_type: str,
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[str] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters_name: typing.Optional[str] = None,
        customer_merchant_customer_id: typing.Optional[str] = None,
        customer_given_name: typing.Optional[str] = None,
        customer_surname: typing.Optional[str] = None,
        customer_mobile: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        customer_status: typing.Optional[str] = None,
        customer_birth_date: typing.Optional[str] = None,
        customer_ip: typing.Optional[str] = None,
        customer_phone: typing.Optional[str] = None,
        customer_id_number: typing.Optional[str] = None,
        billing_street1: typing.Optional[str] = None,
        billing_street2: typing.Optional[str] = None,
        billing_city: typing.Optional[str] = None,
        billing_company: typing.Optional[str] = None,
        billing_country: typing.Optional[str] = None,
        billing_state: typing.Optional[str] = None,
        billing_postcode: typing.Optional[str] = None,
        shipping_street1: typing.Optional[str] = None,
        shipping_street2: typing.Optional[str] = None,
        shipping_city: typing.Optional[str] = None,
        shipping_company: typing.Optional[str] = None,
        shipping_postcode: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        shipping_state: typing.Optional[str] = None,
        cart_tax: typing.Optional[str] = None,
        cart_shipping_amount: typing.Optional[str] = None,
        cart_discount: typing.Optional[str] = None,
        create_registration: typing.Optional[str] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CheckoutGenerationInitiateRedirectCheckoutResponsePydantic:
        raw_response = await self.raw.ainitiate_redirect_checkout(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            payment_type=payment_type,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters_name=custom_parameters_name,
            customer_merchant_customer_id=customer_merchant_customer_id,
            customer_given_name=customer_given_name,
            customer_surname=customer_surname,
            customer_mobile=customer_mobile,
            customer_email=customer_email,
            customer_status=customer_status,
            customer_birth_date=customer_birth_date,
            customer_ip=customer_ip,
            customer_phone=customer_phone,
            customer_id_number=customer_id_number,
            billing_street1=billing_street1,
            billing_street2=billing_street2,
            billing_city=billing_city,
            billing_company=billing_company,
            billing_country=billing_country,
            billing_state=billing_state,
            billing_postcode=billing_postcode,
            shipping_street1=shipping_street1,
            shipping_street2=shipping_street2,
            shipping_city=shipping_city,
            shipping_company=shipping_company,
            shipping_postcode=shipping_postcode,
            shipping_country=shipping_country,
            shipping_state=shipping_state,
            cart_tax=cart_tax,
            cart_shipping_amount=cart_shipping_amount,
            cart_discount=cart_discount,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
            **kwargs,
        )
        if validate:
            return CheckoutGenerationInitiateRedirectCheckoutResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CheckoutGenerationInitiateRedirectCheckoutResponsePydantic, raw_response.body)
    
    
    def initiate_redirect_checkout(
        self,
        authentication_entity_id: str,
        signature: str,
        merchant_transaction_id: str,
        amount: str,
        payment_type: str,
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[str] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters_name: typing.Optional[str] = None,
        customer_merchant_customer_id: typing.Optional[str] = None,
        customer_given_name: typing.Optional[str] = None,
        customer_surname: typing.Optional[str] = None,
        customer_mobile: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        customer_status: typing.Optional[str] = None,
        customer_birth_date: typing.Optional[str] = None,
        customer_ip: typing.Optional[str] = None,
        customer_phone: typing.Optional[str] = None,
        customer_id_number: typing.Optional[str] = None,
        billing_street1: typing.Optional[str] = None,
        billing_street2: typing.Optional[str] = None,
        billing_city: typing.Optional[str] = None,
        billing_company: typing.Optional[str] = None,
        billing_country: typing.Optional[str] = None,
        billing_state: typing.Optional[str] = None,
        billing_postcode: typing.Optional[str] = None,
        shipping_street1: typing.Optional[str] = None,
        shipping_street2: typing.Optional[str] = None,
        shipping_city: typing.Optional[str] = None,
        shipping_company: typing.Optional[str] = None,
        shipping_postcode: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        shipping_state: typing.Optional[str] = None,
        cart_tax: typing.Optional[str] = None,
        cart_shipping_amount: typing.Optional[str] = None,
        cart_discount: typing.Optional[str] = None,
        create_registration: typing.Optional[str] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CheckoutGenerationInitiateRedirectCheckoutResponsePydantic:
        raw_response = self.raw.initiate_redirect_checkout(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            payment_type=payment_type,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters_name=custom_parameters_name,
            customer_merchant_customer_id=customer_merchant_customer_id,
            customer_given_name=customer_given_name,
            customer_surname=customer_surname,
            customer_mobile=customer_mobile,
            customer_email=customer_email,
            customer_status=customer_status,
            customer_birth_date=customer_birth_date,
            customer_ip=customer_ip,
            customer_phone=customer_phone,
            customer_id_number=customer_id_number,
            billing_street1=billing_street1,
            billing_street2=billing_street2,
            billing_city=billing_city,
            billing_company=billing_company,
            billing_country=billing_country,
            billing_state=billing_state,
            billing_postcode=billing_postcode,
            shipping_street1=shipping_street1,
            shipping_street2=shipping_street2,
            shipping_city=shipping_city,
            shipping_company=shipping_company,
            shipping_postcode=shipping_postcode,
            shipping_country=shipping_country,
            shipping_state=shipping_state,
            cart_tax=cart_tax,
            cart_shipping_amount=cart_shipping_amount,
            cart_discount=cart_discount,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        if validate:
            return CheckoutGenerationInitiateRedirectCheckoutResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CheckoutGenerationInitiateRedirectCheckoutResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        authentication_entity_id: str,
        signature: str,
        merchant_transaction_id: str,
        amount: str,
        payment_type: str,
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[str] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters_name: typing.Optional[str] = None,
        customer_merchant_customer_id: typing.Optional[str] = None,
        customer_given_name: typing.Optional[str] = None,
        customer_surname: typing.Optional[str] = None,
        customer_mobile: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        customer_status: typing.Optional[str] = None,
        customer_birth_date: typing.Optional[str] = None,
        customer_ip: typing.Optional[str] = None,
        customer_phone: typing.Optional[str] = None,
        customer_id_number: typing.Optional[str] = None,
        billing_street1: typing.Optional[str] = None,
        billing_street2: typing.Optional[str] = None,
        billing_city: typing.Optional[str] = None,
        billing_company: typing.Optional[str] = None,
        billing_country: typing.Optional[str] = None,
        billing_state: typing.Optional[str] = None,
        billing_postcode: typing.Optional[str] = None,
        shipping_street1: typing.Optional[str] = None,
        shipping_street2: typing.Optional[str] = None,
        shipping_city: typing.Optional[str] = None,
        shipping_company: typing.Optional[str] = None,
        shipping_postcode: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        shipping_state: typing.Optional[str] = None,
        cart_tax: typing.Optional[str] = None,
        cart_shipping_amount: typing.Optional[str] = None,
        cart_discount: typing.Optional[str] = None,
        create_registration: typing.Optional[str] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initiate_redirect_checkout_mapped_args(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            payment_type=payment_type,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters_name=custom_parameters_name,
            customer_merchant_customer_id=customer_merchant_customer_id,
            customer_given_name=customer_given_name,
            customer_surname=customer_surname,
            customer_mobile=customer_mobile,
            customer_email=customer_email,
            customer_status=customer_status,
            customer_birth_date=customer_birth_date,
            customer_ip=customer_ip,
            customer_phone=customer_phone,
            customer_id_number=customer_id_number,
            billing_street1=billing_street1,
            billing_street2=billing_street2,
            billing_city=billing_city,
            billing_company=billing_company,
            billing_country=billing_country,
            billing_state=billing_state,
            billing_postcode=billing_postcode,
            shipping_street1=shipping_street1,
            shipping_street2=shipping_street2,
            shipping_city=shipping_city,
            shipping_company=shipping_company,
            shipping_postcode=shipping_postcode,
            shipping_country=shipping_country,
            shipping_state=shipping_state,
            cart_tax=cart_tax,
            cart_shipping_amount=cart_shipping_amount,
            cart_discount=cart_discount,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        return await self._ainitiate_redirect_checkout_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        authentication_entity_id: str,
        signature: str,
        merchant_transaction_id: str,
        amount: str,
        payment_type: str,
        currency: str,
        nonce: str,
        shopper_result_url: str,
        referer: str,
        default_payment_method: typing.Optional[str] = None,
        force_default_method: typing.Optional[str] = None,
        merchant_invoice_id: typing.Optional[str] = None,
        cancel_url: typing.Optional[str] = None,
        notification_url: typing.Optional[str] = None,
        custom_parameters_name: typing.Optional[str] = None,
        customer_merchant_customer_id: typing.Optional[str] = None,
        customer_given_name: typing.Optional[str] = None,
        customer_surname: typing.Optional[str] = None,
        customer_mobile: typing.Optional[str] = None,
        customer_email: typing.Optional[str] = None,
        customer_status: typing.Optional[str] = None,
        customer_birth_date: typing.Optional[str] = None,
        customer_ip: typing.Optional[str] = None,
        customer_phone: typing.Optional[str] = None,
        customer_id_number: typing.Optional[str] = None,
        billing_street1: typing.Optional[str] = None,
        billing_street2: typing.Optional[str] = None,
        billing_city: typing.Optional[str] = None,
        billing_company: typing.Optional[str] = None,
        billing_country: typing.Optional[str] = None,
        billing_state: typing.Optional[str] = None,
        billing_postcode: typing.Optional[str] = None,
        shipping_street1: typing.Optional[str] = None,
        shipping_street2: typing.Optional[str] = None,
        shipping_city: typing.Optional[str] = None,
        shipping_company: typing.Optional[str] = None,
        shipping_postcode: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        shipping_state: typing.Optional[str] = None,
        cart_tax: typing.Optional[str] = None,
        cart_shipping_amount: typing.Optional[str] = None,
        cart_discount: typing.Optional[str] = None,
        create_registration: typing.Optional[str] = None,
        originator: typing.Optional[str] = None,
        return_to: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initiate_redirect_checkout_mapped_args(
            authentication_entity_id=authentication_entity_id,
            signature=signature,
            merchant_transaction_id=merchant_transaction_id,
            amount=amount,
            payment_type=payment_type,
            currency=currency,
            nonce=nonce,
            shopper_result_url=shopper_result_url,
            referer=referer,
            default_payment_method=default_payment_method,
            force_default_method=force_default_method,
            merchant_invoice_id=merchant_invoice_id,
            cancel_url=cancel_url,
            notification_url=notification_url,
            custom_parameters_name=custom_parameters_name,
            customer_merchant_customer_id=customer_merchant_customer_id,
            customer_given_name=customer_given_name,
            customer_surname=customer_surname,
            customer_mobile=customer_mobile,
            customer_email=customer_email,
            customer_status=customer_status,
            customer_birth_date=customer_birth_date,
            customer_ip=customer_ip,
            customer_phone=customer_phone,
            customer_id_number=customer_id_number,
            billing_street1=billing_street1,
            billing_street2=billing_street2,
            billing_city=billing_city,
            billing_company=billing_company,
            billing_country=billing_country,
            billing_state=billing_state,
            billing_postcode=billing_postcode,
            shipping_street1=shipping_street1,
            shipping_street2=shipping_street2,
            shipping_city=shipping_city,
            shipping_company=shipping_company,
            shipping_postcode=shipping_postcode,
            shipping_country=shipping_country,
            shipping_state=shipping_state,
            cart_tax=cart_tax,
            cart_shipping_amount=cart_shipping_amount,
            cart_discount=cart_discount,
            create_registration=create_registration,
            originator=originator,
            return_to=return_to,
        )
        return self._initiate_redirect_checkout_oapg(
            body=args.body,
            header_params=args.header,
        )

