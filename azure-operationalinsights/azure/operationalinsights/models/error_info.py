# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ErrorInfo(Model):
    """The code and message for an error.

    :param code: A machine readable error code.
    :type code: str
    :param message: A human readable error message.
    :type message: str
    :param details: error details.
    :type details: list[~azure.operationalinsights.models.ErrorDetail]
    :param innererror: Inner error details if they exist.
    :type innererror: ~azure.operationalinsights.models.ErrorInfo
    :param additional_properties:
    :type additional_properties: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'ErrorInfo'},
        'additional_properties': {'key': 'additionalProperties', 'type': 'object'},
    }

    def __init__(self, code, message, details=None, innererror=None, additional_properties=None):
        super(ErrorInfo, self).__init__()
        self.code = code
        self.message = message
        self.details = details
        self.innererror = innererror
        self.additional_properties = additional_properties
