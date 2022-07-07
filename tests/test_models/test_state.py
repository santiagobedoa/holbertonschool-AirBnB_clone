#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for state.py
"""

import unittest
from unittest import mock
from models import state

State = state.State


class TestState(unittest.TestCase):
    """ Test State class """
    def setUp(self):
        """ Set instance for class tests """
        self.state = State()

    def test_init(self):
        """ Test base class instantiation """
        self.assertIsInstance(self.state, State)

    def test_init_att(self):
        """ test if initial attributes are set up """
        state_str = str(self.state)
        state_lst = ['id', 'created_at', 'updated_at']
        count = 0
        for word in state_lst:
            if word in state_str:
                count += 1
        self.assertEqual(3, count)

    def test_class_attr(self):
        """ Test class attribute pass as kwarg """
        state_class = State(__class__='Test', id='1234567890987654321')
        self.assertEqual(type(state_class), State)

    def test_kwargs(self):
        """ Test for attributes pass by kwargs """
        k_state = State(name="Test_Model", number=42)
        dict_kstate = k_state.to_dict()
        test_attr = ['name',
                     'number',
                     '__class__'
                     ]
        real_attr = list(dict_kstate.keys())
        self.assertCountEqual(real_attr, test_attr)

    @mock.patch('models.storage')
    def test_save(self, mock_engine):
        """ Test base save method without models.storage method"""
        init_updated_at = self.state.updated_at
        self.state.save()
        last_updated_at = self.state.updated_at
        self.assertNotEqual(init_updated_at, last_updated_at)
        self.assertTrue(mock_engine.save.called)

    def test_to_dict(self):
        """ Test dictionary conversion creating new key/value pairs """
        self.state.name = "Test_Model"
        self.state.number = 42
        dict_test = self.state.to_dict()
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
        self.state.name = "Test_Model"
        self.state.number = 42
        dict_test = self.state.to_dict()
        self.assertEqual(dict_test['name'], "Test_Model")
        self.assertEqual(dict_test['number'], 42)
        self.assertEqual(dict_test['__class__'], "State")
        self.assertEqual(dict_test['created_at'],
                         self.state.created_at.strftime(time_fmt))
        self.assertEqual(dict_test['updated_at'],
                         self.state.updated_at.strftime(time_fmt))

    def test_str(self):
        """ Test string method """
        test_str = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(test_str, str(self.state))

    def test_name_attr(self):
        """ Test if name is an attribute of State """
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")
        self.state.name = "Holbertonlandia"
        self.assertEqual(self.state.name, "Holbertonlandia")


if __name__ == '__main__':
    unittest.main()
