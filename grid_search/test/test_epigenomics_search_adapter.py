# coding: utf-8

from __future__ import absolute_import
import unittest
from grid_search.epigenomics_search_adapter import EpigenomicsSearchAdapter


class TestEpigenomicsSearchAdapter(unittest.TestCase):

    def test_describe_index(self):
        adapter = EpigenomicsSearchAdapter()
        index = adapter.describe_index()
        self.assertEqual("niehs-epigenomics", index.id)


