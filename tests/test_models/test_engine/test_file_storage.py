#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for file_storage.py
"""

import unittest
import os
from models import base_model
from models.engine import file_storage

FileStorage = file_storage.FileStorage
BaseModel = base_model.BaseModel


class TestStorage(unittest.TestCase):
    """ Class for testing the storage of base_model instances """
    def setUp(self):
        """ Sets up FileStorage object for each test """
        self.storage = FileStorage()
        self.base = BaseModel()

    def test_instance(self):
        """ Test instance creation """
        self.assertEqual(type(self.storage), FileStorage)

    def test_reload(self):
        """ Test storage reload function """
        self.base.name = "Manu"
        self.base.save()
        base_id = self.base.id
        flag = 0
        self.storage.reload()
        objects = self.storage.all()
        for key in objects.keys():
            if base_id in key:
                flag += 1
        self.assertTrue(1 == flag)
        os.remove('./file.json')
