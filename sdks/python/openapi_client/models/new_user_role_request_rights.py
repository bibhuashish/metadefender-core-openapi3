# coding: utf-8

"""
    MetaDefender Core

    ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works.   # noqa: E501

    The version of the OpenAPI document: v4.18.0
    Contact: feedback@opswat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class NewUserRoleRequestRights(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'agents': 'RolePermissionObject',
        'cert': 'RolePermissionObject',
        'configlog': 'RolePermissionObject',
        'engines': 'RolePermissionObject',
        'external': 'RolePermissionObject',
        'license': 'RolePermissionObject',
        'quarantine': 'RolePermissionObject',
        'retention': 'RolePermissionObject',
        'rule': 'RolePermissionObject',
        'scan': 'RolePermissionObject',
        'scanlog': 'RolePermissionObject',
        'skip': 'RolePermissionObject',
        'update': 'RolePermissionObject',
        'updatelog': 'RolePermissionObject',
        'users': 'RolePermissionObject',
        'workflow': 'RolePermissionObject',
        'zone': 'RolePermissionObject'
    }

    attribute_map = {
        'agents': 'agents',
        'cert': 'cert',
        'configlog': 'configlog',
        'engines': 'engines',
        'external': 'external',
        'license': 'license',
        'quarantine': 'quarantine',
        'retention': 'retention',
        'rule': 'rule',
        'scan': 'scan',
        'scanlog': 'scanlog',
        'skip': 'skip',
        'update': 'update',
        'updatelog': 'updatelog',
        'users': 'users',
        'workflow': 'workflow',
        'zone': 'zone'
    }

    def __init__(self, agents=None, cert=None, configlog=None, engines=None, external=None, license=None, quarantine=None, retention=None, rule=None, scan=None, scanlog=None, skip=None, update=None, updatelog=None, users=None, workflow=None, zone=None, local_vars_configuration=None):  # noqa: E501
        """NewUserRoleRequestRights - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._agents = None
        self._cert = None
        self._configlog = None
        self._engines = None
        self._external = None
        self._license = None
        self._quarantine = None
        self._retention = None
        self._rule = None
        self._scan = None
        self._scanlog = None
        self._skip = None
        self._update = None
        self._updatelog = None
        self._users = None
        self._workflow = None
        self._zone = None
        self.discriminator = None

        if agents is not None:
            self.agents = agents
        if cert is not None:
            self.cert = cert
        if configlog is not None:
            self.configlog = configlog
        if engines is not None:
            self.engines = engines
        if external is not None:
            self.external = external
        if license is not None:
            self.license = license
        if quarantine is not None:
            self.quarantine = quarantine
        if retention is not None:
            self.retention = retention
        if rule is not None:
            self.rule = rule
        if scan is not None:
            self.scan = scan
        if scanlog is not None:
            self.scanlog = scanlog
        if skip is not None:
            self.skip = skip
        if update is not None:
            self.update = update
        if updatelog is not None:
            self.updatelog = updatelog
        if users is not None:
            self.users = users
        if workflow is not None:
            self.workflow = workflow
        if zone is not None:
            self.zone = zone

    @property
    def agents(self):
        """Gets the agents of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for Node.  # noqa: E501

        :return: The agents of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this NewUserRoleRequestRights.

        What permissions are allowed for Node.  # noqa: E501

        :param agents: The agents of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._agents = agents

    @property
    def cert(self):
        """Gets the cert of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for Certificates.  # noqa: E501

        :return: The cert of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this NewUserRoleRequestRights.

        What permissions are allowed for Certificates.  # noqa: E501

        :param cert: The cert of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._cert = cert

    @property
    def configlog(self):
        """Gets the configlog of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for Configuration logs.  # noqa: E501

        :return: The configlog of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._configlog

    @configlog.setter
    def configlog(self, configlog):
        """Sets the configlog of this NewUserRoleRequestRights.

        What permissions are allowed for Configuration logs.  # noqa: E501

        :param configlog: The configlog of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._configlog = configlog

    @property
    def engines(self):
        """Gets the engines of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for Engines and Modules.  # noqa: E501

        :return: The engines of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._engines

    @engines.setter
    def engines(self, engines):
        """Sets the engines of this NewUserRoleRequestRights.

        What permissions are allowed for Engines and Modules.  # noqa: E501

        :param engines: The engines of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._engines = engines

    @property
    def external(self):
        """Gets the external of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for External actions (External Scanner/Post Actions).  # noqa: E501

        :return: The external of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this NewUserRoleRequestRights.

        What permissions are allowed for External actions (External Scanner/Post Actions).  # noqa: E501

        :param external: The external of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._external = external

    @property
    def license(self):
        """Gets the license of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the License.  # noqa: E501

        :return: The license of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this NewUserRoleRequestRights.

        What permissions are allowed for managing the License.  # noqa: E501

        :param license: The license of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._license = license

    @property
    def quarantine(self):
        """Gets the quarantine of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the Quarantine.  # noqa: E501

        :return: The quarantine of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._quarantine

    @quarantine.setter
    def quarantine(self, quarantine):
        """Sets the quarantine of this NewUserRoleRequestRights.

        What permissions are allowed for managing the Quarantine.  # noqa: E501

        :param quarantine: The quarantine of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._quarantine = quarantine

    @property
    def retention(self):
        """Gets the retention of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the retention policies.  # noqa: E501

        :return: The retention of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this NewUserRoleRequestRights.

        What permissions are allowed for managing the retention policies.  # noqa: E501

        :param retention: The retention of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._retention = retention

    @property
    def rule(self):
        """Gets the rule of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the workflow rules.  # noqa: E501

        :return: The rule of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this NewUserRoleRequestRights.

        What permissions are allowed for managing the workflow rules.  # noqa: E501

        :param rule: The rule of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._rule = rule

    @property
    def scan(self):
        """Gets the scan of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing analysis actions.  # noqa: E501

        :return: The scan of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._scan

    @scan.setter
    def scan(self, scan):
        """Sets the scan of this NewUserRoleRequestRights.

        What permissions are allowed for managing analysis actions.  # noqa: E501

        :param scan: The scan of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._scan = scan

    @property
    def scanlog(self):
        """Gets the scanlog of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the analysis logs.  # noqa: E501

        :return: The scanlog of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._scanlog

    @scanlog.setter
    def scanlog(self, scanlog):
        """Sets the scanlog of this NewUserRoleRequestRights.

        What permissions are allowed for managing the analysis logs.  # noqa: E501

        :param scanlog: The scanlog of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._scanlog = scanlog

    @property
    def skip(self):
        """Gets the skip of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the Whitelist/blacklist defined in the Inventory.  # noqa: E501

        :return: The skip of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this NewUserRoleRequestRights.

        What permissions are allowed for managing the Whitelist/blacklist defined in the Inventory.  # noqa: E501

        :param skip: The skip of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._skip = skip

    @property
    def update(self):
        """Gets the update of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the update configuration.  # noqa: E501

        :return: The update of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this NewUserRoleRequestRights.

        What permissions are allowed for managing the update configuration.  # noqa: E501

        :param update: The update of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._update = update

    @property
    def updatelog(self):
        """Gets the updatelog of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the update logs.  # noqa: E501

        :return: The updatelog of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._updatelog

    @updatelog.setter
    def updatelog(self, updatelog):
        """Sets the updatelog of this NewUserRoleRequestRights.

        What permissions are allowed for managing the update logs.  # noqa: E501

        :param updatelog: The updatelog of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._updatelog = updatelog

    @property
    def users(self):
        """Gets the users of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the users.  # noqa: E501

        :return: The users of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this NewUserRoleRequestRights.

        What permissions are allowed for managing the users.  # noqa: E501

        :param users: The users of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._users = users

    @property
    def workflow(self):
        """Gets the workflow of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the workflow templates.  # noqa: E501

        :return: The workflow of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this NewUserRoleRequestRights.

        What permissions are allowed for managing the workflow templates.  # noqa: E501

        :param workflow: The workflow of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._workflow = workflow

    @property
    def zone(self):
        """Gets the zone of this NewUserRoleRequestRights.  # noqa: E501

        What permissions are allowed for managing the network zones.  # noqa: E501

        :return: The zone of this NewUserRoleRequestRights.  # noqa: E501
        :rtype: RolePermissionObject
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this NewUserRoleRequestRights.

        What permissions are allowed for managing the network zones.  # noqa: E501

        :param zone: The zone of this NewUserRoleRequestRights.  # noqa: E501
        :type: RolePermissionObject
        """

        self._zone = zone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewUserRoleRequestRights):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewUserRoleRequestRights):
            return True

        return self.to_dict() != other.to_dict()