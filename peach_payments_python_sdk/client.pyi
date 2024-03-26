# coding: utf-8
"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

import typing
import inspect
from datetime import date, datetime
from peach_payments_python_sdk.client_custom import ClientCustom
from peach_payments_python_sdk.configuration import Configuration
from peach_payments_python_sdk.api_client import ApiClient
from peach_payments_python_sdk.type_util import copy_signature
from peach_payments_python_sdk.apis.tags.batch_api import BatchApi
from peach_payments_python_sdk.apis.tags.checkout_v2_generation_api import CheckoutV2GenerationApi
from peach_payments_python_sdk.apis.tags.checkout_generation_api import CheckoutGenerationApi
from peach_payments_python_sdk.apis.tags.files_api import FilesApi
from peach_payments_python_sdk.apis.tags.helpers_api import HelpersApi
from peach_payments_python_sdk.apis.tags.payment_api import PaymentApi
from peach_payments_python_sdk.apis.tags.payments_api_inbound_api import PaymentsAPIInboundApi
from peach_payments_python_sdk.apis.tags.payments_api_outbound_api import PaymentsAPIOutboundApi
from peach_payments_python_sdk.apis.tags.status_api import StatusApi



class PeachPayments(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.batch: BatchApi = BatchApi(api_client)
        self.checkout_v2_generation: CheckoutV2GenerationApi = CheckoutV2GenerationApi(api_client)
        self.checkout_generation: CheckoutGenerationApi = CheckoutGenerationApi(api_client)
        self.files: FilesApi = FilesApi(api_client)
        self.helpers: HelpersApi = HelpersApi(api_client)
        self.payment: PaymentApi = PaymentApi(api_client)
        self.payments_api_inbound: PaymentsAPIInboundApi = PaymentsAPIInboundApi(api_client)
        self.payments_api_outbound: PaymentsAPIOutboundApi = PaymentsAPIOutboundApi(api_client)
        self.status: StatusApi = StatusApi(api_client)
