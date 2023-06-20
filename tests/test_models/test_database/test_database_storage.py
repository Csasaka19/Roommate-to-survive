#!/usr/bin/python3
"""This module contains tests for the database storage class"""
from models.database.database_storage import Database_Storage
from models.user_profile import user_profile
from models.review import review
from models.room_listing import room_listing
from models.roommate_listing import roommate_listing
from models.location import location
from models.dwelling_type import dwelling_type
from models.booking import booking
import unittest

class Test_Database_Storage(unittest.TestCase):
    """This class tests the database storage class"""
    def setUp(self):
        """This method sets up the tests"""
        self.database = Database_Storage()
        self.database.reload()
        self.user = user_profile()
        
if __name__ == "__main__":
    unittest.main()