#!/usr/bin/python3
"""Unittest for location.py module"""
from models.location import location
import unittest

class Test_location(unittest.TestCase):
    """Unittest class for class location"""
    def test_isinstance(self):
        """Test if location is an instance of class location"""
        my_location = location()
        self.assertIsInstance(my_location, location)
        
if __name__ == "__main__":
    unittest.main()