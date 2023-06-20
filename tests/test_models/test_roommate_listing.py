#!/usr/bin/python3
"""Unittest for class roommate_listing"""
from models.roommate_listing import roommate_listing
import unittest

class Test_roommate_listing(unittest.TestCase):
    """Unittest class for roommate_listing"""
    def test_isinstance(self):
        """Test if roommate_listing is an instance of class roommate_listing"""
        my_roommate_listing = roommate_listing()
        self.assertIsInstance(my_roommate_listing, roommate_listing)
        
if __name__ == "__main__":
    unittest.main()