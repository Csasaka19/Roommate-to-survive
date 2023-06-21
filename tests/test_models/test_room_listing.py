#!/usr/bin/python3
"""Unittest for class room_listing"""
from models.room_listing import room_listing
import unittest

class Test_room_listing(unittest.TestCase):
    """Unittest class for room_listing"""
    def test_isinstance(self):
        """Test if room_listing is an instance of class room_listing"""
        my_room_listing = room_listing()
        self.assertIsInstance(my_room_listing, room_listing)
        
if __name__ == "__main__":
    unittest.main()