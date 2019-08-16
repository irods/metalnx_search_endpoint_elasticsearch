# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.indexes import Indexes  # noqa: E501
from swagger_server.models.search_attributes import SearchAttributes  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_get_index_search_attributes(self):
        """Test case for get_index_search_attributes

        Find search attribute terms for a specific index
        """
        response = self.client.open(
            '/v1/attributes/{index_name}'.format(index_name='index_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_indexes(self):
        """Test case for get_indexes

        Find index types supported by this api
        """
        response = self.client.open(
            '/v1/indexes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
