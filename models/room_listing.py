#!/usr/bin/python3
"""This is the available room_listing module"""
from models.user_profile import user_profile as user

class room_listing(user):
    """This is the available room_listing class"""
    

    def __init__(self, room_id, room_description, room_price, room_availability, room_address, room_status):
        """This is init method that initializes the available room_listing class"""
        self.user_id = super().get_user_id()
        self.room_id = room_id
        self.room_description = room_description
        self.room_price = room_price
        self.room_availability = room_availability
        self.room_address = room_address
        self.room_status = room_status

    def set_room_listing(self,room_id, room_description, room_price, room_availability, room_address, room_status):
        """This is the setter method that sets the available room_listing attributes"""
        self.user_id = super().get_user_id()
        self.room_id = room_id
        self.room_description = room_description
        self.room_price = room_price
        self.room_availability = room_availability
        self.room_address = room_address
        self.room_status = room_status

    def get_user_id(self):
        """This is the getter method that gets the user id and returns it"""
        return self.user_id

    def get_room_id(self):
        """This is the getter method that gets the room id and returns it"""
        return self.room_id

    def get_room_description(self):
        """This is the getter method that gets the room description and returns it"""
        return self.room_description

    def get_room_price(self):
        """This is the getter method that gets the room price and returns it"""
        return self.room_price

    def get_room_availability(self):
        """This is the getter method that gets the room availability and returns it"""""
        return self.room_availability

    def get_room_address(self):
        """This is the getter method that gets the room address and returns it"""
        return self.room_address

    def get_room_status(self):
        """This is the getter method that gets the room status and returns it"""
        return self.room_status
