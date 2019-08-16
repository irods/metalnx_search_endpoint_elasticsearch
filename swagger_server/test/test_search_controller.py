# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.search_data import SearchData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

    def test_generic_search(self):
        """Test case for generic_search

        Generic search on one or all available indexes
        """
        query_string = [('index_name', 'index_name_example'),
                        ('search_query', 'search_query_example')]
        response = self.client.open(
            '/v1/search',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
