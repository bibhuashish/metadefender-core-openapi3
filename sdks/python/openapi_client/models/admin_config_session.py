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


class AdminConfigSession(object):
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
        'absolute_session_timeout': 'int',
        'allow_cross_ip_sessions': 'bool',
        'allow_duplicate_session': 'bool',
        'session_timeout': 'int'
    }

    attribute_map = {
        'absolute_session_timeout': 'absoluteSessionTimeout',
        'allow_cross_ip_sessions': 'allowCrossIpSessions',
        'allow_duplicate_session': 'allowDuplicateSession',
        'session_timeout': 'sessionTimeout'
    }

    def __init__(self, absolute_session_timeout=None, allow_cross_ip_sessions=None, allow_duplicate_session=None, session_timeout=None, local_vars_configuration=None):  # noqa: E501
        """AdminConfigSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._absolute_session_timeout = None
        self._allow_cross_ip_sessions = None
        self._allow_duplicate_session = None
        self._session_timeout = None
        self.discriminator = None

        if absolute_session_timeout is not None:
            self.absolute_session_timeout = absolute_session_timeout
        if allow_cross_ip_sessions is not None:
            self.allow_cross_ip_sessions = allow_cross_ip_sessions
        if allow_duplicate_session is not None:
            self.allow_duplicate_session = allow_duplicate_session
        if session_timeout is not None:
            self.session_timeout = session_timeout

    @property
    def absolute_session_timeout(self):
        """Gets the absolute_session_timeout of this AdminConfigSession.  # noqa: E501

        The interval (in milliseconds) for overall session length timeout (regardless of activity).  # noqa: E501

        :return: The absolute_session_timeout of this AdminConfigSession.  # noqa: E501
        :rtype: int
        """
        return self._absolute_session_timeout

    @absolute_session_timeout.setter
    def absolute_session_timeout(self, absolute_session_timeout):
        """Sets the absolute_session_timeout of this AdminConfigSession.

        The interval (in milliseconds) for overall session length timeout (regardless of activity).  # noqa: E501

        :param absolute_session_timeout: The absolute_session_timeout of this AdminConfigSession.  # noqa: E501
        :type: int
        """

        self._absolute_session_timeout = absolute_session_timeout

    @property
    def allow_cross_ip_sessions(self):
        """Gets the allow_cross_ip_sessions of this AdminConfigSession.  # noqa: E501

        Allow requests from the same user to come from different IPs.  # noqa: E501

        :return: The allow_cross_ip_sessions of this AdminConfigSession.  # noqa: E501
        :rtype: bool
        """
        return self._allow_cross_ip_sessions

    @allow_cross_ip_sessions.setter
    def allow_cross_ip_sessions(self, allow_cross_ip_sessions):
        """Sets the allow_cross_ip_sessions of this AdminConfigSession.

        Allow requests from the same user to come from different IPs.  # noqa: E501

        :param allow_cross_ip_sessions: The allow_cross_ip_sessions of this AdminConfigSession.  # noqa: E501
        :type: bool
        """

        self._allow_cross_ip_sessions = allow_cross_ip_sessions

    @property
    def allow_duplicate_session(self):
        """Gets the allow_duplicate_session of this AdminConfigSession.  # noqa: E501

        Allow same user to have multiple active sessions.  # noqa: E501

        :return: The allow_duplicate_session of this AdminConfigSession.  # noqa: E501
        :rtype: bool
        """
        return self._allow_duplicate_session

    @allow_duplicate_session.setter
    def allow_duplicate_session(self, allow_duplicate_session):
        """Sets the allow_duplicate_session of this AdminConfigSession.

        Allow same user to have multiple active sessions.  # noqa: E501

        :param allow_duplicate_session: The allow_duplicate_session of this AdminConfigSession.  # noqa: E501
        :type: bool
        """

        self._allow_duplicate_session = allow_duplicate_session

    @property
    def session_timeout(self):
        """Gets the session_timeout of this AdminConfigSession.  # noqa: E501

        The interval (in milliseconds) for the user's session timeout, based on last activity. Timer starts after the last activity for the apikey.  # noqa: E501

        :return: The session_timeout of this AdminConfigSession.  # noqa: E501
        :rtype: int
        """
        return self._session_timeout

    @session_timeout.setter
    def session_timeout(self, session_timeout):
        """Sets the session_timeout of this AdminConfigSession.

        The interval (in milliseconds) for the user's session timeout, based on last activity. Timer starts after the last activity for the apikey.  # noqa: E501

        :param session_timeout: The session_timeout of this AdminConfigSession.  # noqa: E501
        :type: int
        """

        self._session_timeout = session_timeout

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
        if not isinstance(other, AdminConfigSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdminConfigSession):
            return True

        return self.to_dict() != other.to_dict()