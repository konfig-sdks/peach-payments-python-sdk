# coding: utf-8

"""
    Payments API inbound

    The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.

    The version of the OpenAPI document: 2.0.0
    Contact: support@peachpayments.com
    Created by: https://support.peachpayments.com/support/home
"""

from peach_payments_python_sdk.paths.api_payments_payment_id_files_file_id.get import DownloadFileRaw
from peach_payments_python_sdk.paths.api_attachments.post import UploadFileRaw


class FilesApiRaw(
    DownloadFileRaw,
    UploadFileRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
