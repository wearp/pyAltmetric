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
        self.b = Altmetric(api_key="KEY_HERE")

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
