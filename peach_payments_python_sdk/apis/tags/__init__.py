# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from peach_payments_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BATCH = "Batch"
    PAYMENTS_API_INBOUND = "Payments API inbound"
    CHECKOUT_GENERATION = "Checkout generation"
    PAYMENT = "Payment"
    STATUS = "Status"
    FILES = "Files"
    HELPERS = "Helpers"
    CHECKOUT_V2_GENERATION = "Checkout V2 generation"
    PAYMENTS_API_OUTBOUND = "Payments API outbound"
