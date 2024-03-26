# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

import unittest

import os
from pprint import pprint
from peach_payments_python_sdk import PeachPayments

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        peachpayments = PeachPayments(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(peachpayments)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
