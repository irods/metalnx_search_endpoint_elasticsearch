# coding: utf-8

from __future__ import absolute_import
import unittest
from swagger_server.services.grid_search.search_adapter import SearchAdapter


class TestEpigenomicsSearchAdapter(unittest.TestCase):

    def test_describe_index(self):
        adapter = SearchAdapter()
        index = adapter.describe_index()
        self.assertEqual("epigenomics", index.id)


