# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.deep_cdr_details_details import DeepCDRDetailsDetails
from openapi_server import util

from openapi_server.models.deep_cdr_details_details import DeepCDRDetailsDetails  # noqa: E501

class DeepCDRDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, details=None):  # noqa: E501
        """DeepCDRDetails - a model defined in OpenAPI

        :param description: The description of this DeepCDRDetails.  # noqa: E501
        :type description: str
        :param details: The details of this DeepCDRDetails.  # noqa: E501
        :type details: List[DeepCDRDetailsDetails]
        """
        self.openapi_types = {
            'description': str,
            'details': List[DeepCDRDetailsDetails]
        }

        self.attribute_map = {
            'description': 'description',
            'details': 'details'
        }

        self._description = description
        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'DeepCDRDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeepCDRDetails of this DeepCDRDetails.  # noqa: E501
        :rtype: DeepCDRDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this DeepCDRDetails.

        Action was successful or not.  # noqa: E501

        :return: The description of this DeepCDRDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeepCDRDetails.

        Action was successful or not.  # noqa: E501

        :param description: The description of this DeepCDRDetails.
        :type description: str
        """

        self._description = description

    @property
    def details(self):
        """Gets the details of this DeepCDRDetails.

        List of all sanitized objects  # noqa: E501

        :return: The details of this DeepCDRDetails.
        :rtype: List[DeepCDRDetailsDetails]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DeepCDRDetails.

        List of all sanitized objects  # noqa: E501

        :param details: The details of this DeepCDRDetails.
        :type details: List[DeepCDRDetailsDetails]
        """

        self._details = details