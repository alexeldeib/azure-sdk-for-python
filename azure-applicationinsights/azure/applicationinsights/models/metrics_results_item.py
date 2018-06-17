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


class MetricsResultsItem(Model):
    """MetricsResultsItem.

    :param id: The specified ID for this metric.
    :type id: str
    :param status: The HTTP status code of this metric query.
    :type status: int
    :param body: The results of this metric query.
    :type body: ~azure.applicationinsights.models.MetricsResult
    """

    _validation = {
        'id': {'required': True},
        'status': {'required': True},
        'body': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'int'},
        'body': {'key': 'body', 'type': 'MetricsResult'},
    }

    def __init__(self, id, status, body):
        super(MetricsResultsItem, self).__init__()
        self.id = id
        self.status = status
        self.body = body
