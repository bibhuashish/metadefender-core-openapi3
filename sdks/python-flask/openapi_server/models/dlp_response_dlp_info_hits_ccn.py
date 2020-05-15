# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dlp_rule_match_result import DLPRuleMatchResult
from openapi_server import util

from openapi_server.models.dlp_rule_match_result import DLPRuleMatchResult  # noqa: E501

class DLPResponseDlpInfoHitsCcn(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_name=None, hits=None):  # noqa: E501
        """DLPResponseDlpInfoHitsCcn - a model defined in OpenAPI

        :param display_name: The display_name of this DLPResponseDlpInfoHitsCcn.  # noqa: E501
        :type display_name: str
        :param hits: The hits of this DLPResponseDlpInfoHitsCcn.  # noqa: E501
        :type hits: List[DLPRuleMatchResult]
        """
        self.openapi_types = {
            'display_name': str,
            'hits': List[DLPRuleMatchResult]
        }

        self.attribute_map = {
            'display_name': 'display_name',
            'hits': 'hits'
        }

        self._display_name = display_name
        self._hits = hits

    @classmethod
    def from_dict(cls, dikt) -> 'DLPResponseDlpInfoHitsCcn':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DLPResponse_dlp_info_hits_ccn of this DLPResponseDlpInfoHitsCcn.  # noqa: E501
        :rtype: DLPResponseDlpInfoHitsCcn
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_name(self):
        """Gets the display_name of this DLPResponseDlpInfoHitsCcn.

        Credit Card Number, Social Security Number, or in case of RegEx, the name of the rule that has been given by the user  # noqa: E501

        :return: The display_name of this DLPResponseDlpInfoHitsCcn.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DLPResponseDlpInfoHitsCcn.

        Credit Card Number, Social Security Number, or in case of RegEx, the name of the rule that has been given by the user  # noqa: E501

        :param display_name: The display_name of this DLPResponseDlpInfoHitsCcn.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def hits(self):
        """Gets the hits of this DLPResponseDlpInfoHitsCcn.

        A list of detections that matched this rule/pattern.  # noqa: E501

        :return: The hits of this DLPResponseDlpInfoHitsCcn.
        :rtype: List[DLPRuleMatchResult]
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this DLPResponseDlpInfoHitsCcn.

        A list of detections that matched this rule/pattern.  # noqa: E501

        :param hits: The hits of this DLPResponseDlpInfoHitsCcn.
        :type hits: List[DLPRuleMatchResult]
        """

        self._hits = hits