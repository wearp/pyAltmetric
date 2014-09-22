#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyaltmetric
----------------------------------

Tests for `pyaltmetric` module.
"""

import unittest
import requests
from pyaltmetric.pyaltmetric import Altmetric, AltmetricException, HTTPException, Citation


class TestAltmetric(unittest.TestCase):
    def setUp(self):
        self.a = Altmetric()
        self.b = Altmetric("123")

    def test_fetch_that_is_successful(self):
        response = self.a.fetch("citations", "1w", page=1, nlmid="0410462",)
        self.assertEqual(self.a.params, {'nlmid': '0410462', 'page': 1})
        self.assertTrue(isinstance(response, dict))
        response_2 = self.a.citations("1w", page=1, nlmid="0410462",)
        self.assertTrue(isinstance(response_2, dict))

    def test_fetch_that_raises_a_404_Not_Found(self):
        response = self.a.citations("1w", cited_in="facebook", nlmid="0370352")
        self.assertEqual(response, None)

    def test_fetch_that_raises_HTTP_exception(self):
        self.assertRaises(HTTPException,
                lambda: self.b.fetch("citations", "1w", nlmid="0410462"))

    def tearDown(self):
        pass


class TestCitation(unittest.TestCase):
    def setUp(self):
        a = Altmetric()
        self.response = a.id("108989")

    def test_Article__init__(self):
        self.assertTrue(isinstance(self.response, dict))
        article = Citation(self.response)
        self.assertEqual(article.title, "Rebuilding Global Fisheries")

    def test_get_fields(self):
        article = Citation(self.response)
        fields = article.get_fields('title', 'nlmid')
        self.assertEqual(fields[0], "Rebuilding Global Fisheries")
        self.assertEqual(fields[1], "0404511")

    def test_get_fields_with_nonexitent_attribute(self):
        article = Citation(self.response)
        fields = article.get_fields('title', 'nonexistent', 'nlmid')
        self.assertEqual(fields[0], "Rebuilding Global Fisheries")
        self.assertEqual(fields[1], "")
        self.assertEqual(fields[2], "0404511")

if __name__ == '__main__':
    unittest.main()
