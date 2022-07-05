#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for city.py
"""

import unittest
from models import city
from models import base_model

City = city.City
BaseModel = base_model.BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        """ Set city instance for all the tests """
        self.city = City()

    def test_init(self):
        """ Test city initialization """
        self.assertIsInstance(self.citycity, City)

    def test_init_att(self):
        """ test if initial attributes are set up """
        city_str = str(self.city)
        city_lst = ['id', 'created_at', 'updated_at']
        count = 0
        for word in city_lst:
            if word in city_str:
                count += 1
        self.assertEqual(3, count)

    def test_inheritance(self):
        """ Test if city inherits from BaseModel """
        self.assertIsInstance(self.city, BaseModel)

    def test_state_id_attr(self):
        """ Test if state_id is an attribute of city """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, "")
        self.city.state_id = "Holberton_DC"
        self.assertEqual(self.city.state_id, "Holberton_DC")

    def test_name_attr(self):
        """ Test if name is an attribute of city """
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, "")
        self.city.name = "Holbertonlandia"
        self.assertEqual(self.city.name, "Holbertonlandia")


if __name__ == "__main__":
    unittest.main()
