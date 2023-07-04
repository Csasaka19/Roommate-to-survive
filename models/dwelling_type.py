#!/usr/bin/python3
"""This is the dwelling type module"""
from models.user_profile import user_profile as user


class dwelling_type(user):
    """This is the dwelling type class"""
    def __init__(self, location_id, location_name, location_address, city, country,
                 location_description, user_id, user_type, name, email, phone, budget,
                 gender, age, dwelling_type_id, dwelling_type_name, location):
        """This is the constructor method that initializes the dwelling type class"""
        self.dwelling_type_id = dwelling_type_id
        self.dwelling_type_name = dwelling_type_name
        self.location = location
        super().__init__(location_id, location_name, location_address, city, country,
                 location_description, user_id, user_type, name, email, phone, budget,
                 gender, age)

    def set_dwelling_type(self, user_id, dwelling_type_id, dwelling_type_name, location):
        """This is the setter method that sets the dwelling type attributes"""
        self.user_id = user_id
        self.dwelling_type_id = dwelling_type_id
        self.dwelling_type_name = dwelling_type_name
        self.location = location

    def get_dwelling_type_id(self):
        '''This is the getter method that gets the dwelling type id and returns it'''
        return self.dwelling_type_id

    def get_dwelling_type_name(self):
        """This is the getter method that gets the dwelling type name and returns it"""
        return self.dwelling_type_name

    def get_location(self):
        """This is the getter method that gets the location and returns it"""
        return self.location
    