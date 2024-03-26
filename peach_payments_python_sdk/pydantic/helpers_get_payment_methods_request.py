# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class HelpersGetPaymentMethodsRequest(BaseModel):
    authentication.entity_id_: str = Field(alias='authentication.entityId')

    # Token to verify the integrity of the request, ensuring that only the merchant sending the request is accepted.
    signature: str = Field(alias='signature')

    # Three-letter ISO 4217 currency code.
    currency: str = Field(alias='currency')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
