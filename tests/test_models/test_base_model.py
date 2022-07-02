#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for base_model.py
"""

import unittest
from models import base_model

BaseModel = base_model.BaseModel


class TestBase(unittest.TestCase):
    """ Test Base class """
    def setUp(self):
        """ Set instance for class tests """
        self.base = BaseModel()

    def test_init(self):
        """ Test base class instantiation """
        self.assertIsInstance(self.base, BaseModel)

    def test_init_att(self):
        """ test if initial attributes are set up """
        base_str = str(self.base)
        base_lst = ['id', 'created_at', 'updated_at']
        count = 0
        for word in base_lst:
            if word in base_str:
                count += 1
        self.assertEqual(3, count)


if __name__ == '__main__':
    unittest.main()
