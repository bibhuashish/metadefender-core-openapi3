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


class InlineResponse2009(object):
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
        'data_id': 'str',
        'request_time': 'str',
        'status_code': 'int',
        'url': 'str'
    }

    attribute_map = {
        'data_id': 'data_id',
        'request_time': 'request_time',
        'status_code': 'status_code',
        'url': 'url'
    }

    def __init__(self, data_id=None, request_time=None, status_code=None, url=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2009 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_id = None
        self._request_time = None
        self._status_code = None
        self._url = None
        self.discriminator = None

        if data_id is not None:
            self.data_id = data_id
        if request_time is not None:
            self.request_time = request_time
        if status_code is not None:
            self.status_code = status_code
        if url is not None:
            self.url = url

    @property
    def data_id(self):
        """Gets the data_id of this InlineResponse2009.  # noqa: E501

        The file submission identifier  # noqa: E501

        :return: The data_id of this InlineResponse2009.  # noqa: E501
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """Sets the data_id of this InlineResponse2009.

        The file submission identifier  # noqa: E501

        :param data_id: The data_id of this InlineResponse2009.  # noqa: E501
        :type: str
        """

        self._data_id = data_id

    @property
    def request_time(self):
        """Gets the request_time of this InlineResponse2009.  # noqa: E501

        A timestamp when the request has been made.  # noqa: E501

        :return: The request_time of this InlineResponse2009.  # noqa: E501
        :rtype: str
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this InlineResponse2009.

        A timestamp when the request has been made.  # noqa: E501

        :param request_time: The request_time of this InlineResponse2009.  # noqa: E501
        :type: str
        """

        self._request_time = request_time

    @property
    def status_code(self):
        """Gets the status_code of this InlineResponse2009.  # noqa: E501

        What was the returned HTTP status code.  # noqa: E501

        :return: The status_code of this InlineResponse2009.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this InlineResponse2009.

        What was the returned HTTP status code.  # noqa: E501

        :param status_code: The status_code of this InlineResponse2009.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def url(self):
        """Gets the url of this InlineResponse2009.  # noqa: E501

        What was the called URL (should match the `callbackurl` header).  # noqa: E501

        :return: The url of this InlineResponse2009.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse2009.

        What was the called URL (should match the `callbackurl` header).  # noqa: E501

        :param url: The url of this InlineResponse2009.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, InlineResponse2009):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2009):
            return True

        return self.to_dict() != other.to_dict()