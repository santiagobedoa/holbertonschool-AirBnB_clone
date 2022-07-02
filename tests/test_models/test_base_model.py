#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for base_model.py
"""

import models
import unittest
from unittest import mock
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

    @mock.patch('models.storage')
    def test_save(self, mock_engine):
        """ Test base save method without models.storage method"""
        init_updated_at = self.base.updated_at
        self.base.save()
        last_updated_at = self.base.updated_at
        self.assertNotEqual(init_updated_at, last_updated_at)
        self.assertTrue(mock_engine.save.called)


if __name__ == '__main__':
    unittest.main()
