import typing_extensions

from peach_payments_python_sdk.paths import PathValues
from peach_payments_python_sdk.apis.paths.checkout_initiate import CheckoutInitiate
from peach_payments_python_sdk.apis.paths.checkout import Checkout
from peach_payments_python_sdk.apis.paths.checkout_validate import CheckoutValidate
from peach_payments_python_sdk.apis.paths.status import Status
from peach_payments_python_sdk.apis.paths.merchant_specs import MerchantSpecs
from peach_payments_python_sdk.apis.paths.v2_checkout import V2Checkout
from peach_payments_python_sdk.apis.paths.api_channels_entity_id_payments import ApiChannelsEntityIdPayments
from peach_payments_python_sdk.apis.paths.api_payments import ApiPayments
from peach_payments_python_sdk.apis.paths.api_payments_payment_id import ApiPaymentsPaymentId
from peach_payments_python_sdk.apis.paths.api_payments_payment_id_files_file_id import ApiPaymentsPaymentIdFilesFileId
from peach_payments_python_sdk.apis.paths.api_attachments import ApiAttachments
from peach_payments_python_sdk.apis.paths.api_channels_entity_id_payments_batches import ApiChannelsEntityIdPaymentsBatches
from peach_payments_python_sdk.apis.paths.api_batches_batch_id import ApiBatchesBatchId
from peach_payments_python_sdk.apis.paths.api_batches_batch_id_files import ApiBatchesBatchIdFiles
from peach_payments_python_sdk.apis.paths.root import Root
from peach_payments_python_sdk.apis.paths.payments import Payments
from peach_payments_python_sdk.apis.paths.payments_unique_id import PaymentsUniqueId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CHECKOUT_INITIATE: CheckoutInitiate,
        PathValues.CHECKOUT: Checkout,
        PathValues.CHECKOUT_VALIDATE: CheckoutValidate,
        PathValues.STATUS: Status,
        PathValues.MERCHANT_SPECS: MerchantSpecs,
        PathValues.V2_CHECKOUT: V2Checkout,
        PathValues.API_CHANNELS_ENTITY_ID_PAYMENTS: ApiChannelsEntityIdPayments,
        PathValues.API_PAYMENTS: ApiPayments,
        PathValues.API_PAYMENTS_PAYMENT_ID: ApiPaymentsPaymentId,
        PathValues.API_PAYMENTS_PAYMENT_ID_FILES_FILE_ID: ApiPaymentsPaymentIdFilesFileId,
        PathValues.API_ATTACHMENTS: ApiAttachments,
        PathValues.API_CHANNELS_ENTITY_ID_PAYMENTS_BATCHES: ApiChannelsEntityIdPaymentsBatches,
        PathValues.API_BATCHES_BATCH_ID: ApiBatchesBatchId,
        PathValues.API_BATCHES_BATCH_ID_FILES: ApiBatchesBatchIdFiles,
        PathValues._: Root,
        PathValues.PAYMENTS: Payments,
        PathValues.PAYMENTS_UNIQUE_ID: PaymentsUniqueId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CHECKOUT_INITIATE: CheckoutInitiate,
        PathValues.CHECKOUT: Checkout,
        PathValues.CHECKOUT_VALIDATE: CheckoutValidate,
        PathValues.STATUS: Status,
        PathValues.MERCHANT_SPECS: MerchantSpecs,
        PathValues.V2_CHECKOUT: V2Checkout,
        PathValues.API_CHANNELS_ENTITY_ID_PAYMENTS: ApiChannelsEntityIdPayments,
        PathValues.API_PAYMENTS: ApiPayments,
        PathValues.API_PAYMENTS_PAYMENT_ID: ApiPaymentsPaymentId,
        PathValues.API_PAYMENTS_PAYMENT_ID_FILES_FILE_ID: ApiPaymentsPaymentIdFilesFileId,
        PathValues.API_ATTACHMENTS: ApiAttachments,
        PathValues.API_CHANNELS_ENTITY_ID_PAYMENTS_BATCHES: ApiChannelsEntityIdPaymentsBatches,
        PathValues.API_BATCHES_BATCH_ID: ApiBatchesBatchId,
        PathValues.API_BATCHES_BATCH_ID_FILES: ApiBatchesBatchIdFiles,
        PathValues._: Root,
        PathValues.PAYMENTS: Payments,
        PathValues.PAYMENTS_UNIQUE_ID: PaymentsUniqueId,
    }
)
