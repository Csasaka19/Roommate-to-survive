#!/usr/bin/python3
"""This is the roommate listing module"""
from models.user_profile import user_profile as user


def roommate_listing(user):
    """This is the roommate listing class"""

    def __init__(self,  roommate_id, roommate_description, roommate_price, roommate_availability,
                 roommate_address, roommate_status, roommate_preference):
        """This is the constructor method that initializes the roommate listing class"""
        self.roommate_id = roommate_id
        self.roommate_description = roommate_description
        self.roommate_price = roommate_price
        self.roommate_availability = roommate_availability
        self.roommate_address = roommate_address
        self.roommate_status = roommate_status
        self.roommate_preference = roommate_preference

    def set_roommate_listing(self, roommate_id, roommate_description, roommate_price, roommate_availability,
                             roommate_address, roommate_status, roommate_preference):
        """This is the setter method that sets the roommate listing attributes"""
        self.roommate_id = roommate_id
        self.roommate_description = roommate_description
        self.roommate_price = roommate_price
        self.roommate_availability = roommate_availability
        self.roommate_address = roommate_address
        self.roommate_status = roommate_status
        self.roommate_preference = roommate_preference

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        """This is the getter method that gets the user id and returns it"""
        return self.user_id

    def get_roommate_id(self):
        """This is the getter method that gets the roommate id and returns it"""
        return self.roommate_id

    def get_roommate_description(self):
        """This is the getter method that gets the roommate description and returns it"""
        return self.roommate_description

    def get_roommate_price(self):
        """This is the getter method that gets the roommate price and returns it"""
        return self.roommate_price

    def get_roommate_availability(self):
        """This is the getter method that gets the roommate availability and returns it"""
        return self.roommate_availability

    def get_roommate_address(self):
        """This is the getter method that gets the roommate address and returns it"""
        return self.roommate_address

    def get_roommate_status(self):
        """This is the getter method that gets the roommate status and returns it"""
        return self.roommate_status

    def get_roommate_preference(self):
        """This is the getter method that gets the roommate preference and returns it"""
        return self.roommate_preference

