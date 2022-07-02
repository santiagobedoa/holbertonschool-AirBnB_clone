#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for base_model.py
"""


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

    def test_kwargs(self):
        """ Test attributes pass by kwargs """
        k_base = BaseModel(name="Test_Model", number=42)
        dict_kbase = k_base.to_dict()
        test_attr = ['name',
                     'number',
                     '__class__'
                     ]
        real_attr = list(dict_kbase.keys())
        self.assertCountEqual(real_attr, test_attr)

    @mock.patch('models.storage')
    def test_save(self, mock_engine):
        """ Test base save method without models.storage method"""
        init_updated_at = self.base.updated_at
        self.base.save()
        last_updated_at = self.base.updated_at
        self.assertNotEqual(init_updated_at, last_updated_at)
        self.assertTrue(mock_engine.save.called)

    def test_to_dict(self):
        """ Test dictionary conversion creating new key/value pairs """
        self.base.name = "Test_Model"
        self.base.number = 42
        dict_test = self.base.to_dict()
        test_attr = ['id',
                     'name',
                     'number',
                     'created_at',
                     'updated_at',
                     '__class__'
                     ]
        real_attr = list(dict_test.keys())
        self.assertCountEqual(real_attr, test_attr)

    def test_to_dict_values(self):
        """ Test dict values """
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.base.name = "Test_Model"
        self.base.number = 42
        dict_test = self.base.to_dict()
        self.assertEqual(dict_test['name'], "Test_Model")
        self.assertEqual(dict_test['number'], 42)
        self.assertEqual(dict_test['__class__'], "BaseModel")
        self.assertEqual(dict_test['created_at'],
                         self.base.created_at.strftime(time_fmt))
        self.assertEqual(dict_test['updated_at'],
                         self.base.updated_at.strftime(time_fmt))

    def test_str(self):
        """ Test string method """
        test_str = f"[BaseModel] ({self.base.id}) {self.base.__dict__}"
        self.assertEqual(test_str, str(self.base))


if __name__ == '__main__':
    unittest.main()
