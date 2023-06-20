#!/usr/bin/python3
"""Unittest for class user_profile"""
from models.user_profile import user_profile
import unittest

class Test_user_profile(unittest.TestCase):
    """Unittest class for user_profile"""
    def test_isinstance(self):
        """Test if user_profile is an instance of class user_profile"""
        my_user_profile = user_profile()
        self.assertIsInstance(my_user_profile, user_profile)
        
if __name__ == "__main__":
    unittest.main()