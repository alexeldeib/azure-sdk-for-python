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

from .create_job_properties import CreateJobProperties


class CreateUSqlJobProperties(CreateJobProperties):
    """U-SQL job properties used when submitting U-SQL jobs.

    All required parameters must be populated in order to send to Azure.

    :param runtime_version: The runtime version of the Data Lake Analytics
     engine to use for the specific type of job being run.
    :type runtime_version: str
    :param script: Required. The script to run. Please note that the maximum
     script size is 3 MB.
    :type script: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param compile_mode: The specific compilation mode for the job used during
     execution. If this is not specified during submission, the server will
     determine the optimal compilation mode. Possible values include:
     'Semantic', 'Full', 'SingleBox'
    :type compile_mode: str or
     ~azure.mgmt.datalake.analytics.job.models.CompileMode
    """

    _validation = {
        'script': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'runtime_version': {'key': 'runtimeVersion', 'type': 'str'},
        'script': {'key': 'script', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'compile_mode': {'key': 'compileMode', 'type': 'CompileMode'},
    }

    def __init__(self, **kwargs):
        super(CreateUSqlJobProperties, self).__init__(**kwargs)
        self.compile_mode = kwargs.get('compile_mode', None)
        self.type = 'USql'
