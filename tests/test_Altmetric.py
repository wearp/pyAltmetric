#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_Altmetric
----------------------------------

Tests for `Altmetric` module.
"""

import unittest
import requests
from Altmetric.Altmetric import Altmetric, AltmetricException, HTTPException, Citation, CitationCollection


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

    def test_fetch_with_40X_HTTP_status_code(self):
        self.assertRaises(HTTPException,
                lambda: self.b.fetch("citations", "1w", nlmid="xxx"))

    def tearDown(self):
        pass


class TestCitation(unittest.TestCase):
    def setUp(self):
        self.a = Altmetric()

    def test_Article__init__(self):
        response = self.a.id("108989")
        self.assertTrue(isinstance(response, dict))
        article = Citation(response)
        self.assertEqual(article.title, "Rebuilding Global Fisheries")


class TestCitationCollection(unittest.TestCase):
    def setUp(self):
        self.a = Altmetric()
        citation = self.a.id("108989")
        self.single_citation = Citation(citation)
        self.collection_a = CitationCollection()

        self.citations = self.a.citations("1d", page=1, nlmid="0410462")
        self.collection_b = CitationCollection()

    def test_add_citation(self):
        self.collection_a.add_citation(self.single_citation)
        self.assertTrue(isinstance(self.collection_a.citations[0], Citation))
        self.assertEqual(self.collection_a.citations[0].title, 
                "Rebuilding Global Fisheries")


class TestHttpException(unittest.TestCase):
    def setUp(self):
        self.a = HTTPException(403, "Unauthorized access")

    def test_HTTPException(self):
        self.assertEqual(self.a.status_code, 403)
        self.assertEqual(self.a.message, "Unauthorized access")

if __name__ == '__main__':
    unittest.main()
