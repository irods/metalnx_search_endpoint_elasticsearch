# coding: utf-8
from __future__ import absolute_import
import logging

from swagger_server.test import BaseTestCase
from swagger_server.services.grid_search.epigenomics_search_adapter import EpigenomicsSearchAdapter
from swagger_server.services.auth.grid_auth_util import GridAuthUtil

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_get_indexes(self):
        """Test case for get_indexes

        Find index types supported by this api
        """
        logger.debug('TestInfoController: test_get_indexes()')
        grid_auth = GridAuthUtil()
        token = grid_auth.generate_token('testUser')
        response = self.client.open(
            '/v1/indexes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_describe_index(self):
        adapter = EpigenomicsSearchAdapter()
        index = adapter.describe_index()
        self.assertEqual("niehs-epigenomics", index.id)


if __name__ == '__main__':
    import unittest
    unittest.main()
