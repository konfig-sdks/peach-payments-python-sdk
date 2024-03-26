import typing_extensions

from peach_payments_python_sdk.apis.tags import TagValues
from peach_payments_python_sdk.apis.tags.batch_api import BatchApi
from peach_payments_python_sdk.apis.tags.payments_api_inbound_api import PaymentsAPIInboundApi
from peach_payments_python_sdk.apis.tags.checkout_generation_api import CheckoutGenerationApi
from peach_payments_python_sdk.apis.tags.payment_api import PaymentApi
from peach_payments_python_sdk.apis.tags.status_api import StatusApi
from peach_payments_python_sdk.apis.tags.files_api import FilesApi
from peach_payments_python_sdk.apis.tags.helpers_api import HelpersApi
from peach_payments_python_sdk.apis.tags.checkout_v2_generation_api import CheckoutV2GenerationApi
from peach_payments_python_sdk.apis.tags.payments_api_outbound_api import PaymentsAPIOutboundApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BATCH: BatchApi,
        TagValues.PAYMENTS_API_INBOUND: PaymentsAPIInboundApi,
        TagValues.CHECKOUT_GENERATION: CheckoutGenerationApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.STATUS: StatusApi,
        TagValues.FILES: FilesApi,
        TagValues.HELPERS: HelpersApi,
        TagValues.CHECKOUT_V2_GENERATION: CheckoutV2GenerationApi,
        TagValues.PAYMENTS_API_OUTBOUND: PaymentsAPIOutboundApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BATCH: BatchApi,
        TagValues.PAYMENTS_API_INBOUND: PaymentsAPIInboundApi,
        TagValues.CHECKOUT_GENERATION: CheckoutGenerationApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.STATUS: StatusApi,
        TagValues.FILES: FilesApi,
        TagValues.HELPERS: HelpersApi,
        TagValues.CHECKOUT_V2_GENERATION: CheckoutV2GenerationApi,
        TagValues.PAYMENTS_API_OUTBOUND: PaymentsAPIOutboundApi,
    }
)
