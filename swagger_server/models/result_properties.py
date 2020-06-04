# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.result_properties_property_set import ResultPropertiesPropertySet  # noqa: F401,E501
from swagger_server import util


class ResultProperties(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, propertyset_title: str=None, propertyset_description: str=None, property_set: List[ResultPropertiesPropertySet]=None):  # noqa: E501
        """ResultProperties - a model defined in Swagger

        :param propertyset_title: The propertyset_title of this ResultProperties.  # noqa: E501
        :type propertyset_title: str
        :param propertyset_description: The propertyset_description of this ResultProperties.  # noqa: E501
        :type propertyset_description: str
        :param property_set: The property_set of this ResultProperties.  # noqa: E501
        :type property_set: List[ResultPropertiesPropertySet]
        """
        self.swagger_types = {
            'propertyset_title': str,
            'propertyset_description': str,
            'property_set': List[ResultPropertiesPropertySet]
        }

        self.attribute_map = {
            'propertyset_title': 'propertyset_title',
            'propertyset_description': 'propertyset_description',
            'property_set': 'propertySet'
        }
        self._propertyset_title = propertyset_title
        self._propertyset_description = propertyset_description
        self._property_set = property_set

    @classmethod
    def from_dict(cls, dikt) -> 'ResultProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The result_properties of this ResultProperties.  # noqa: E501
        :rtype: ResultProperties
        """
        return util.deserialize_model(dikt, cls)

    @property
    def propertyset_title(self) -> str:
        """Gets the propertyset_title of this ResultProperties.

        User friendly title for property set  # noqa: E501

        :return: The propertyset_title of this ResultProperties.
        :rtype: str
        """
        return self._propertyset_title

    @propertyset_title.setter
    def propertyset_title(self, propertyset_title: str):
        """Sets the propertyset_title of this ResultProperties.

        User friendly title for property set  # noqa: E501

        :param propertyset_title: The propertyset_title of this ResultProperties.
        :type propertyset_title: str
        """

        self._propertyset_title = propertyset_title

    @property
    def propertyset_description(self) -> str:
        """Gets the propertyset_description of this ResultProperties.

        Text description of a property set  # noqa: E501

        :return: The propertyset_description of this ResultProperties.
        :rtype: str
        """
        return self._propertyset_description

    @propertyset_description.setter
    def propertyset_description(self, propertyset_description: str):
        """Sets the propertyset_description of this ResultProperties.

        Text description of a property set  # noqa: E501

        :param propertyset_description: The propertyset_description of this ResultProperties.
        :type propertyset_description: str
        """

        self._propertyset_description = propertyset_description

    @property
    def property_set(self) -> List[ResultPropertiesPropertySet]:
        """Gets the property_set of this ResultProperties.


        :return: The property_set of this ResultProperties.
        :rtype: List[ResultPropertiesPropertySet]
        """
        return self._property_set

    @property_set.setter
    def property_set(self, property_set: List[ResultPropertiesPropertySet]):
        """Sets the property_set of this ResultProperties.


        :param property_set: The property_set of this ResultProperties.
        :type property_set: List[ResultPropertiesPropertySet]
        """

        self._property_set = property_set
