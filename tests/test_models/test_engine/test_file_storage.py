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
        # self.base = BaseModel()
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

    def test_save_file(self):
        """ Test storage save the file """
        # self.base = BaseModel()
        self.base.save()
        self.assertTrue(os.path.exists('./file.json') is True)
        os.remove('./file.json')

    def test_save_content(self):
        """ Test storage save the correct content """
        # self.base = BaseModel()
        self.base.name = "Santi"
        base_id = self.base.id
        self.base.save()
        flags = 0
        with open('./file.json', 'r') as file:
            read_file = file.read()
            if "Santi" in read_file:
                flags += 1
            if base_id in read_file:
                flags += 1
        self.assertTrue(flags == 2)
        os.remove('./file.json')

    def test_all(self):
        """ Test storage all function """
        # self.base = BaseModel()
        dict_objs = dict()
        obj = f"{type(self.base).__name__}.{self.base.id}"
        dict_objs[obj] = self.base
        self.assertEqual(dict_objs, self.storage.all())
