#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for user.py
"""

import unittest
from models import user
from models import base_model

User = user.User
BaseModel = base_model.BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        """ Set user instance for all the tests """
        self.user = User()

    def test_init(self):
        """ Test user initialization """
        self.assertIsInstance(self.user, User)

    def test_init_att(self):
        """ test if initial attributes are set up """
        user_str = str(self.user)
        user_lst = ['id', 'created_at', 'updated_at']
        count = 0
        for word in user_lst:
            if word in user_str:
                count += 1
        self.assertEqual(3, count)

    def test_inheritance(self):
        """ Test if user inherits from BaseModel """
        self.assertIsInstance(self.user, BaseModel)

    def test_email_attr(self):
        """ Test if email is an attribute of user """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")
        self.user.email = "holbie@holbertonschool.com"
        self.assertEqual(self.user.email, "holbie@holbertonschool.com")

    def test_password_attr(self):
        """ Test if password is an attribute of user """
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")
        self.user.password = "*#$@&"
        self.assertEqual(self.user.password, "*#$@&")

    def test_first_attr(self):
        """ Test if first_name is an attribute of user """
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")
        self.user.first_name = "holbie"
        self.assertEqual(self.user.first_name, "holbie")

    def test_last_attr(self):
        """ Test if last_name is an attribute of user """
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")
        self.user.last_name = "school"
        self.assertEqual(self.user.last_name, "school")


if __name__ == "__main__":
    unittest.main()
