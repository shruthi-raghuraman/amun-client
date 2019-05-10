# coding: utf-8

"""
    Amun API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from amun.swagger_client.models.inspection_specification_run_requests_hardware import InspectionSpecificationRunRequestsHardware  # noqa: F401,E501


class InspectionSpecificationRunRequests(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cpu': 'str',
        'hardware': 'InspectionSpecificationRunRequestsHardware',
        'memory': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'hardware': 'hardware',
        'memory': 'memory'
    }

    def __init__(self, cpu=None, hardware=None, memory=None):  # noqa: E501
        """InspectionSpecificationRunRequests - a model defined in Swagger"""  # noqa: E501

        self._cpu = None
        self._hardware = None
        self._memory = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if hardware is not None:
            self.hardware = hardware
        if memory is not None:
            self.memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this InspectionSpecificationRunRequests.  # noqa: E501

        CPU cores requested at run time  # noqa: E501

        :return: The cpu of this InspectionSpecificationRunRequests.  # noqa: E501
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this InspectionSpecificationRunRequests.

        CPU cores requested at run time  # noqa: E501

        :param cpu: The cpu of this InspectionSpecificationRunRequests.  # noqa: E501
        :type: str
        """
        if cpu is not None and len(cpu) < 1:
            raise ValueError("Invalid value for `cpu`, length must be greater than or equal to `1`")  # noqa: E501

        self._cpu = cpu

    @property
    def hardware(self):
        """Gets the hardware of this InspectionSpecificationRunRequests.  # noqa: E501


        :return: The hardware of this InspectionSpecificationRunRequests.  # noqa: E501
        :rtype: InspectionSpecificationRunRequestsHardware
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this InspectionSpecificationRunRequests.


        :param hardware: The hardware of this InspectionSpecificationRunRequests.  # noqa: E501
        :type: InspectionSpecificationRunRequestsHardware
        """

        self._hardware = hardware

    @property
    def memory(self):
        """Gets the memory of this InspectionSpecificationRunRequests.  # noqa: E501

        CPU Memory requested at run time  # noqa: E501

        :return: The memory of this InspectionSpecificationRunRequests.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this InspectionSpecificationRunRequests.

        CPU Memory requested at run time  # noqa: E501

        :param memory: The memory of this InspectionSpecificationRunRequests.  # noqa: E501
        :type: str
        """
        if memory is not None and len(memory) < 1:
            raise ValueError("Invalid value for `memory`, length must be greater than or equal to `1`")  # noqa: E501

        self._memory = memory

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InspectionSpecificationRunRequests, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InspectionSpecificationRunRequests):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
