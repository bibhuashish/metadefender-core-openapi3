# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserRequestAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, password=None):  # noqa: E501
        """UserRequestAllOf - a model defined in OpenAPI

        :param password: The password of this UserRequestAllOf.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'password': str
        }

        self.attribute_map = {
            'password': 'password'
        }

        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'UserRequestAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserRequest_allOf of this UserRequestAllOf.  # noqa: E501
        :rtype: UserRequestAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def password(self):
        """Gets the password of this UserRequestAllOf.

        The user's password  # noqa: E501

        :return: The password of this UserRequestAllOf.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserRequestAllOf.

        The user's password  # noqa: E501

        :param password: The password of this UserRequestAllOf.
        :type password: str
        """

        self._password = password