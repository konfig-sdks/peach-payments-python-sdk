# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

import unittest
from unittest.mock import patch

import urllib3

import peach_payments_python_sdk
from peach_payments_python_sdk.paths.payments_unique_id import get
from peach_payments_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPaymentsUniqueId(ApiTestMixin, unittest.TestCase):
    """
    PaymentsUniqueId unit test stubs
        Query a transaction by transaction ID
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
