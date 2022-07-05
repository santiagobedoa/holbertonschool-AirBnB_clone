#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest session for review.py
"""

import unittest
from unittest import mock
from models import review

Review = review.Review


class TestReview(unittest.TestCase):
    """ Test Review class """
    def setUp(self):
        """ Set instance for class tests """
        self.review = Review()

    def test_init(self):
        """ Test base class instantiation """
        self.assertIsInstance(self.review, Review)

    def test_init_att(self):
        """ test if initial attributes are set up """
        review_str = str(self.review)
        review_lst = ['id', 'created_at', 'updated_at']
        count = 0
        for word in review_lst:
            if word in review_str:
                count += 1
        self.assertEqual(3, count)

    def test_class_attr(self):
        """ Test class attribute pass as kwarg """
        review_class = Review(__class__='Test', id='1234567890987654321')
        self.assertEqual(type(review_class), Review)

    def test_kwargs(self):
        """ Test for attributes pass by kwargs """
        k_review = Review(text="Test_Model", number=42)
        dict_kreview = k_review.to_dict()
        test_attr = ['text',
                     'number',
                     '__class__'
                     ]
        real_attr = list(dict_kreview.keys())
        self.assertCountEqual(real_attr, test_attr)

    @mock.patch('models.storage')
    def test_save(self, mock_engine):
        """ Test base save method without models.storage method"""
        init_updated_at = self.review.updated_at
        self.review.save()
        last_updated_at = self.review.updated_at
        self.assertNotEqual(init_updated_at, last_updated_at)
        self.assertTrue(mock_engine.save.called)

    def test_to_dict(self):
        """ Test dictionary conversion creating new key/value pairs """
        self.review.text = "Test_Model"
        self.review.number = 42
        dict_test = self.review.to_dict()
        test_attr = ['id',
                     'text',
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
        self.review.text = "Test_Model"
        self.review.number = 42
        dict_test = self.review.to_dict()
        self.assertEqual(dict_test['text'], "Test_Model")
        self.assertEqual(dict_test['number'], 42)
        self.assertEqual(dict_test['__class__'], "Review")
        self.assertEqual(dict_test['created_at'],
                         self.review.created_at.strftime(time_fmt))
        self.assertEqual(dict_test['updated_at'],
                         self.review.updated_at.strftime(time_fmt))

    def test_str(self):
        """ Test string method """
        test_str = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(test_str, str(self.review))


if __name__ == '__main__':
    unittest.main()
