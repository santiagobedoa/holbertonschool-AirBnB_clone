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
        """ Test if user inherits from user """
        self.assertIsInstance(self.user, User)

    def test_to_dict(self):
        """ Test dictionary conversion creating new key/value pairs """
        self.user.email = "holbie@holbertonschool.com"
        self.user.password = "*#$@&"
        dict_test = self.user.to_dict()
        test_attr = ['id',
                     'email',
                     'password',
                     'created_at',
                     'updated_at',
                     '__class__'
                     ]
        real_attr = list(dict_test.keys())
        self.assertCountEqual(real_attr, test_attr)

    def test_to_dict_values(self):
        """ Test dict values """
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.user.email = "holbie@holbertonschool.com"
        self.user.password = "*#$@&"
        dict_test = self.user.to_dict()
        self.assertEqual(dict_test['email'], "holbie@holbertonschool.com")
        self.assertEqual(dict_test['password'], "*#$@&")
        self.assertEqual(dict_test['__class__'], "User")
        self.assertEqual(dict_test['created_at'],
                         self.user.created_at.strftime(time_fmt))
        self.assertEqual(dict_test['updated_at'],
                         self.user.updated_at.strftime(time_fmt))

    def test_str(self):
        """ Test string method """
        test_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(test_str, str(self.user))

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
