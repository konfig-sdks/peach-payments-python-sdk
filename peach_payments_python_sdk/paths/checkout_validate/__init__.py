# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from peach_payments_python_sdk.paths.checkout_validate import Api

from peach_payments_python_sdk.paths import PathValues

path = PathValues.CHECKOUT_VALIDATE