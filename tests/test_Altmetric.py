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

    def test_fetch_that_is_successful(self):
        response = self.a.fetch("citations", "1w", page=1, nlmid="0410462",)
        self.assertEqual(self.a.params, {'nlmid': '0410462', 'page': 1})
        self.assertTrue(isinstance(response, dict))
        response_2 = self.a.citations("1w", page=1, nlmid="0410462",)
        self.assertTrue(isinstance(response_2, dict))

    def test_fetch_that_raises_HTTP_exception(self):
        self.assertRaises(HTTPException,
                lambda: self.b.fetch("citations", "1w", nlmid="xxx"))

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

    def test__iter__(self):
        article = Citation(self.response)
        for i in article:
            self.assertTrue(isinstance(i, tuple)) 

class TestCitationCollection(unittest.TestCase):
    def setUp(self):
        self.a = Altmetric()
        self.collection_a = CitationCollection()
        self.collection_b = CitationCollection()
        
        citation = self.a.id("108989")
        self.single_citation = Citation(citation)
        self.citations = self.a.citations("1d", page=1, nlmid="0410462")

    def test_add_citation_with_one_citation_object(self):
        self.collection_a.add_citation(self.single_citation)
        self.assertTrue(isinstance(self.collection_a.citations[0], Citation))
        self.assertEqual(self.collection_a.citations[0].title, 
                "Rebuilding Global Fisheries")

    def test_add_citation_with_multiple_citation_objects(self):
        i = self.citations['results'][0]
        p = self.citations['results'][1]
        
        self.collection_b.add_citation(Citation(i), Citation(p))
        self.assertTrue(isinstance(self.collection_b.citations[0], Citation)) 
        self.assertTrue(isinstance(self.collection_b.citations[1], Citation))
 
    def test__iter__(self):
        i = self.citations['results'][0]
        p = self.citations['results'][1]
        x = self.citations['results'][2]
    
        self.collection_b.add_citation(Citation(i), Citation(p), Citation(x))
        for x in self.collection_b:
            print x

class TestHttpException(unittest.TestCase):
    def setUp(self):
        self.a = HTTPException(403, "Unauthorized access")

    def test_HTTPException(self):
        self.assertEqual(self.a.status_code, 403)
        self.assertEqual(self.a.message, "Unauthorized access")


if __name__ == '__main__':
    unittest.main()
