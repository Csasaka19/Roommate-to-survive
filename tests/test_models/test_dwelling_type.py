#!/usr/bin/python3
"""Unittest for class dwelling_type"""
from models.dwelling_type import dwelling_type 
import unittest

class Test_dwelling_type(unittest.TestCase):
    """Unittest class for dwelling_type"""
    def test_isinstance(self):
        """Test if dwelling_type is an instance of class dwelling_type"""
        my_dwelling_type = dwelling_type()
        self.assertIsInstance(my_dwelling_type, dwelling_type)


if __name__ == "__main__":
    unittest.main()