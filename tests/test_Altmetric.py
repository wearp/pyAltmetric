#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_Altmetric
----------------------------------

Tests for `Altmetric` module.
"""

import unittest
import requests
from Altmetric.Altmetric import Altmetric, AltmetricException, HTTPException


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
        self.assertRaises(HTTPException,
                lambda: self.b.fetch("citations", "1w", nlmid="xxx"))

    def test_HTTPException(self):
        self.exception = HTTPException(403, "Unauthorized access")
        self.assertEqual(self.exception.status_code, 403)
        self.assertEqual(self.exception.message, "Unauthorized access")

    def tearDown(self):
        pass




if __name__ == '__main__':
    unittest.main()
