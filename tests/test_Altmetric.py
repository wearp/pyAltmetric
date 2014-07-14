#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_Altmetric
----------------------------------

Tests for `Altmetric` module.
"""

import unittest

from Altmetric.Altmetric import Altmetric


class TestAltmetric(unittest.TestCase):

    def setUp(self):
        self.a = Altmetric()
        self.b = Altmetric()

    def test_fetch_with_200_HTTP_status_code(self):
        response = self.a.fetch("citations", "1w", page=1, nlmid="0410462",)
        self.assertEqual(self.a.params, {'nlmid': '0410462', 'page': 1})
        self.assertTrue(isinstance(response, dict))
        response_2 = self.a.citations("1w", page=1, nlmid="0410462",)
        self.assertTrue(isinstance(response_2, dict))

    def test_fetch_with_404_HTTP_status_code(self):
        response = self.b.citations("1d", page=1, nlmid="XXXX",)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
