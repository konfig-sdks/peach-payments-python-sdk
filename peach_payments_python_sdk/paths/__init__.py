# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from peach_payments_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CHECKOUT_INITIATE = "/checkout/initiate"
    CHECKOUT = "/checkout"
    CHECKOUT_VALIDATE = "/checkout/validate"
    STATUS = "/status"
    MERCHANT_SPECS = "/merchant_specs"
    V2_CHECKOUT = "/v2/checkout"
    API_CHANNELS_ENTITY_ID_PAYMENTS = "/api/channels/{entityId}/payments"
    API_PAYMENTS = "/api/payments"
    API_PAYMENTS_PAYMENT_ID = "/api/payments/{paymentId}"
    API_PAYMENTS_PAYMENT_ID_FILES_FILE_ID = "/api/payments/{paymentId}/files/{fileId}"
    API_ATTACHMENTS = "/api/attachments"
    API_CHANNELS_ENTITY_ID_PAYMENTS_BATCHES = "/api/channels/{entityId}/payments/batches"
    API_BATCHES_BATCH_ID = "/api/batches/{batchId}"
    API_BATCHES_BATCH_ID_FILES = "/api/batches/{batchId}/files"
    _ = "/"
    PAYMENTS = "/payments"
    PAYMENTS_UNIQUE_ID = "/payments/{uniqueId}"
