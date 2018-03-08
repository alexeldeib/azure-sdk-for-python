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

from .resource import Resource


class GroupContract(Resource):
    """Contract details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param display_name: Required. Group name.
    :type display_name: str
    :param description: Group description. Can contain HTML formatting tags.
    :type description: str
    :ivar built_in: true if the group is one of the three system groups
     (Administrators, Developers, or Guests); otherwise false.
    :vartype built_in: bool
    :param group_contract_type: Group type. Possible values include: 'custom',
     'system', 'external'
    :type group_contract_type: str or
     ~azure.mgmt.apimanagement.models.GroupType
    :param external_id: For external groups, this property contains the id of
     the group from the external identity provider, e.g. for Azure Active
     Directory aad://<tenant>.onmicrosoft.com/groups/<group object id>;
     otherwise the value is null.
    :type external_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'required': True, 'max_length': 300, 'min_length': 1},
        'description': {'max_length': 1000},
        'built_in': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'built_in': {'key': 'properties.builtIn', 'type': 'bool'},
        'group_contract_type': {'key': 'properties.type', 'type': 'GroupType'},
        'external_id': {'key': 'properties.externalId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GroupContract, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.built_in = None
        self.group_contract_type = kwargs.get('group_contract_type', None)
        self.external_id = kwargs.get('external_id', None)
