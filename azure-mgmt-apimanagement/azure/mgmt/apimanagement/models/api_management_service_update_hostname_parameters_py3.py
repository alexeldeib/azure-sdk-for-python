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


class ApiManagementServiceUpdateHostnameParameters(Model):
    """Parameters supplied to the UpdateHostname operation.

    :param update: Hostnames to create or update.
    :type update:
     list[~azure.mgmt.apimanagement.models.HostnameConfigurationOld]
    :param delete: Hostnames types to delete.
    :type delete: list[str or ~azure.mgmt.apimanagement.models.HostnameType]
    """

    _attribute_map = {
        'update': {'key': 'update', 'type': '[HostnameConfigurationOld]'},
        'delete': {'key': 'delete', 'type': '[HostnameType]'},
    }

    def __init__(self, *, update=None, delete=None, **kwargs) -> None:
        super(ApiManagementServiceUpdateHostnameParameters, self).__init__(**kwargs)
        self.update = update
        self.delete = delete
