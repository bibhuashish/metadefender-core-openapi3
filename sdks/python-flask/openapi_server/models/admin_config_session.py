# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AdminConfigSession(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, absolute_session_timeout=None, allow_cross_ip_sessions=None, allow_duplicate_session=None, session_timeout=None):  # noqa: E501
        """AdminConfigSession - a model defined in OpenAPI

        :param absolute_session_timeout: The absolute_session_timeout of this AdminConfigSession.  # noqa: E501
        :type absolute_session_timeout: int
        :param allow_cross_ip_sessions: The allow_cross_ip_sessions of this AdminConfigSession.  # noqa: E501
        :type allow_cross_ip_sessions: bool
        :param allow_duplicate_session: The allow_duplicate_session of this AdminConfigSession.  # noqa: E501
        :type allow_duplicate_session: bool
        :param session_timeout: The session_timeout of this AdminConfigSession.  # noqa: E501
        :type session_timeout: int
        """
        self.openapi_types = {
            'absolute_session_timeout': int,
            'allow_cross_ip_sessions': bool,
            'allow_duplicate_session': bool,
            'session_timeout': int
        }

        self.attribute_map = {
            'absolute_session_timeout': 'absoluteSessionTimeout',
            'allow_cross_ip_sessions': 'allowCrossIpSessions',
            'allow_duplicate_session': 'allowDuplicateSession',
            'session_timeout': 'sessionTimeout'
        }

        self._absolute_session_timeout = absolute_session_timeout
        self._allow_cross_ip_sessions = allow_cross_ip_sessions
        self._allow_duplicate_session = allow_duplicate_session
        self._session_timeout = session_timeout

    @classmethod
    def from_dict(cls, dikt) -> 'AdminConfigSession':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AdminConfigSession of this AdminConfigSession.  # noqa: E501
        :rtype: AdminConfigSession
        """
        return util.deserialize_model(dikt, cls)

    @property
    def absolute_session_timeout(self):
        """Gets the absolute_session_timeout of this AdminConfigSession.

        The interval (in milliseconds) for overall session length timeout (regardless of activity).  # noqa: E501

        :return: The absolute_session_timeout of this AdminConfigSession.
        :rtype: int
        """
        return self._absolute_session_timeout

    @absolute_session_timeout.setter
    def absolute_session_timeout(self, absolute_session_timeout):
        """Sets the absolute_session_timeout of this AdminConfigSession.

        The interval (in milliseconds) for overall session length timeout (regardless of activity).  # noqa: E501

        :param absolute_session_timeout: The absolute_session_timeout of this AdminConfigSession.
        :type absolute_session_timeout: int
        """

        self._absolute_session_timeout = absolute_session_timeout

    @property
    def allow_cross_ip_sessions(self):
        """Gets the allow_cross_ip_sessions of this AdminConfigSession.

        Allow requests from the same user to come from different IPs.  # noqa: E501

        :return: The allow_cross_ip_sessions of this AdminConfigSession.
        :rtype: bool
        """
        return self._allow_cross_ip_sessions

    @allow_cross_ip_sessions.setter
    def allow_cross_ip_sessions(self, allow_cross_ip_sessions):
        """Sets the allow_cross_ip_sessions of this AdminConfigSession.

        Allow requests from the same user to come from different IPs.  # noqa: E501

        :param allow_cross_ip_sessions: The allow_cross_ip_sessions of this AdminConfigSession.
        :type allow_cross_ip_sessions: bool
        """

        self._allow_cross_ip_sessions = allow_cross_ip_sessions

    @property
    def allow_duplicate_session(self):
        """Gets the allow_duplicate_session of this AdminConfigSession.

        Allow same user to have multiple active sessions.  # noqa: E501

        :return: The allow_duplicate_session of this AdminConfigSession.
        :rtype: bool
        """
        return self._allow_duplicate_session

    @allow_duplicate_session.setter
    def allow_duplicate_session(self, allow_duplicate_session):
        """Sets the allow_duplicate_session of this AdminConfigSession.

        Allow same user to have multiple active sessions.  # noqa: E501

        :param allow_duplicate_session: The allow_duplicate_session of this AdminConfigSession.
        :type allow_duplicate_session: bool
        """

        self._allow_duplicate_session = allow_duplicate_session

    @property
    def session_timeout(self):
        """Gets the session_timeout of this AdminConfigSession.

        The interval (in milliseconds) for the user's session timeout, based on last activity. Timer starts after the last activity for the apikey.  # noqa: E501

        :return: The session_timeout of this AdminConfigSession.
        :rtype: int
        """
        return self._session_timeout

    @session_timeout.setter
    def session_timeout(self, session_timeout):
        """Sets the session_timeout of this AdminConfigSession.

        The interval (in milliseconds) for the user's session timeout, based on last activity. Timer starts after the last activity for the apikey.  # noqa: E501

        :param session_timeout: The session_timeout of this AdminConfigSession.
        :type session_timeout: int
        """

        self._session_timeout = session_timeout