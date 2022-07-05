#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for Place.py
"""

import unittest
from models import place
from models import base_model

Place = place.Place
BaseModel = base_model.BaseModel


class TestPlace(unittest.TestCase):

    def setUp(self):
        """ Set Place instance for all the tests """
        self.place = Place()

    def test_init(self):
        """ Test Place initialization """
        self.assertIsInstance(self.place, Place)

    def test_init_att(self):
        """ test if initial attributes are set up """
        place_str = str(self.place)
        place_lst = ['id', 'created_at', 'updated_at']
        count = 0
        for word in place_lst:
            if word in place_str:
                count += 1
        self.assertEqual(3, count)

    def test_inheritance(self):
        """ Test if Place inherits from BaseModel """
        self.assertIsInstance(self.place, BaseModel)

    def test_city_id_attr(self):
        """ Test if city_id is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, "")
        self.place.city_id = "holbiecity"
        self.assertEqual(self.place.city_id, "holbiecity")

    def test_user_id_attr(self):
        """ Test if user_id is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, "")
        self.place.user_id = "holbie42"
        self.assertEqual(self.place.user_id, "holbie42")

    def test_name_attr(self):
        """ Test if name is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, "")
        self.place.name = "holbie"
        self.assertEqual(self.place.name, "holbie")

    def test_description_attr(self):
        """ Test if description is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, "")
        self.place.description = "virtual"
        self.assertEqual(self.place.description, "virtual")

    def test_number_rooms_attr(self):
        """ Test if number_rooms is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(self.place.number_rooms, 0)
        self.place.number_rooms = 3
        self.assertEqual(self.place.number_rooms, 3)

    def test_number_bathrooms_attr(self):
        """ Test if number_bathrooms is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.place.number_bathrooms = 1
        self.assertEqual(self.place.number_bathrooms, 1)

    def test_max_guest_attr(self):
        """ Test if max_guest is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(self.place.max_guest, 0)
        self.place.max_guest = 3
        self.assertEqual(self.place.max_guest, 3)

    def test_price_by_night_attr(self):
        """ Test if price_by_night is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(self.place.price_by_night, 0)
        self.place.price_by_night = 3
        self.assertEqual(self.place.price_by_night, 3)

    def test_latitude_attr(self):
        """ Test if latitude is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(self.place.latitude, 0.0)
        self.place.latitude = 20.42
        self.assertEqual(self.place.latitude, 20.42)

    def test_longitude_attr(self):
        """ Test if longitude is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(self.place.longitude, 0.0)
        self.place.longitude = 14.26
        self.assertEqual(self.place.longitude, 14.26)

    def test_amenity_ids_attr(self):
        """ Test if amenity_ids is an attribute of Place """
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(type(self.place.amenity_ids), list)
        self.assertEqual(self.place.amenity_ids, [])
        self.place.amenity_ids = [1, 2, 3, 4]
        self.assertEqual(self.place.amenity_ids, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
