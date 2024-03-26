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
from peach_payments_python_sdk.paths.api_payments_payment_id_files_file_id import get
from peach_payments_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiPaymentsPaymentIdFilesFileId(ApiTestMixin, unittest.TestCase):
    """
    ApiPaymentsPaymentIdFilesFileId unit test stubs
        Download a file
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
