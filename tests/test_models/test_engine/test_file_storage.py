#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for file_storage.py
"""

import unittest
from models.engine import file_storage

FileStorage = file_storage.FileStorage


class TestStorage(unittest.TestCase):
    """ Class for testing the storage of base_model instances """
    def setUp(self):
        """ Sets up FileStorage object for each test """
        self.storage = FileStorage()

    def test_instance(self):
