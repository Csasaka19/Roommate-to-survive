#!/usr/bin/python3
"""Unittest for review.py module"""
from models.review import review
import unittest

class Test_review(unittest.TestCase):
    """Unittest class for class review"""
    def test_isinstance(self):
        """Test if review is an instance of class review"""
        my_review = review()
        self.assertIsInstance(my_review, review)
        
if __name__ == "__main__":
    unittest.main()