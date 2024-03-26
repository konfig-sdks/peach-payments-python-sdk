# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

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


class StatusQueryPaymentStatusResponseAudit(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['StatusQueryPaymentStatusResponseAuditItem']:
            return StatusQueryPaymentStatusResponseAuditItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['StatusQueryPaymentStatusResponseAuditItem'], typing.List['StatusQueryPaymentStatusResponseAuditItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'StatusQueryPaymentStatusResponseAudit':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'StatusQueryPaymentStatusResponseAuditItem':
        return super().__getitem__(i)

from peach_payments_python_sdk.model.status_query_payment_status_response_audit_item import StatusQueryPaymentStatusResponseAuditItem
