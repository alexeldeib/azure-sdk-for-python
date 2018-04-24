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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION


class ContainerRegistryManagementClientConfiguration(AzureConfiguration):
    """Configuration for ContainerRegistryManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ContainerRegistryManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('containerregistrymanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ContainerRegistryManagementClient(object):
    """ContainerRegistryManagementClient

    :ivar config: Configuration for client.
    :vartype config: ContainerRegistryManagementClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A dict using operation group name to API version.
    :type profile: dict[str, str]    """

    DEFAULT_API_VERSION = '2017-10-01'
    DEFAULT_PROFILE = None

    def __init__(
            self, credentials, subscription_id, api_version=DEFAULT_API_VERSION, base_url=None, profile=DEFAULT_PROFILE):

        self.config = ContainerRegistryManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        self.api_version = api_version
        self.profile = dict(profile) if profile is not None else {}

############ Generated from here ############

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2017-03-01: :mod:`v2017_03_01.models<azure.mgmt.containerregistry.v2017_03_01.models>`
           * 2017-10-01: :mod:`v2017_10_01.models<azure.mgmt.containerregistry.v2017_10_01.models>`
           * 2017-10-01: :mod:`v2018_02_01_preview.models<azure.mgmt.containerregistry.v2018_02_01_preview.models>`
        """
        if api_version == '2017-03-01':
            from .v2017_03_01 import models
            return models
        elif api_version == '2017-10-01':
            from .v2017_10_01 import models
            return models
        elif api_version == '2017-10-01':
            from .v2018_02_01_preview import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))
    
    @property
    def build_steps(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`BuildStepsOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.BuildStepsOperations>`
        """
        api_version = self.profile.get('build_steps', self.api_version)
        if api_version == '2017-10-01':
            from .v2018_02_01_preview.operations import BuildStepsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def build_tasks(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`BuildTasksOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.BuildTasksOperations>`
        """
        api_version = self.profile.get('build_tasks', self.api_version)
        if api_version == '2017-10-01':
            from .v2018_02_01_preview.operations import BuildTasksOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def builds(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`BuildsOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.BuildsOperations>`
        """
        api_version = self.profile.get('builds', self.api_version)
        if api_version == '2017-10-01':
            from .v2018_02_01_preview.operations import BuildsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2017-03-01: :class:`Operations<azure.mgmt.containerregistry.v2017_03_01.operations.Operations>`
           * 2017-10-01: :class:`Operations<azure.mgmt.containerregistry.v2017_10_01.operations.Operations>`
           * 2017-10-01: :class:`Operations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.Operations>`
        """
        api_version = self.profile.get('operations', self.api_version)
        if api_version == '2017-03-01':
            from .v2017_03_01.operations import Operations as OperationClass
        elif api_version == '2017-10-01':
            from .v2017_10_01.operations import Operations as OperationClass
        elif api_version == '2017-10-01':
            from .v2018_02_01_preview.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def registries(self):
        """Instance depends on the API version:

           * 2017-03-01: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2017_03_01.operations.RegistriesOperations>`
           * 2017-10-01: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2017_10_01.operations.RegistriesOperations>`
           * 2017-10-01: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.RegistriesOperations>`
        """
        api_version = self.profile.get('registries', self.api_version)
        if api_version == '2017-03-01':
            from .v2017_03_01.operations import RegistriesOperations as OperationClass
        elif api_version == '2017-10-01':
            from .v2017_10_01.operations import RegistriesOperations as OperationClass
        elif api_version == '2017-10-01':
            from .v2018_02_01_preview.operations import RegistriesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def replications(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2017_10_01.operations.ReplicationsOperations>`
           * 2017-10-01: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.ReplicationsOperations>`
        """
        api_version = self.profile.get('replications', self.api_version)
        if api_version == '2017-10-01':
            from .v2017_10_01.operations import ReplicationsOperations as OperationClass
        elif api_version == '2017-10-01':
            from .v2018_02_01_preview.operations import ReplicationsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def webhooks(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2017_10_01.operations.WebhooksOperations>`
           * 2017-10-01: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.WebhooksOperations>`
        """
        api_version = self.profile.get('webhooks', self.api_version)
        if api_version == '2017-10-01':
            from .v2017_10_01.operations import WebhooksOperations as OperationClass
        elif api_version == '2017-10-01':
            from .v2018_02_01_preview.operations import WebhooksOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
