#!/usr/bin/python3
"""Unittest for class booking"""
from models.booking import booking
import unittest

class Test_Booking(unittest.TestCase):
    """Unittest class for class booking"""
    
    def test_isinstance(self):
        """Test if booking is an instance of class booking"""
        my_booking = booking()
        self.assertIsInstance(my_booking, booking)
        

if  __name__ == "__main__":
    unittest.main()