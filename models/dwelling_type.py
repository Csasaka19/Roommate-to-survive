#!/usr/bin/python3
"""This is the dwelling type module"""


class dwelling_type():
    """This is the dwelling type class"""
    def __init__(self, dwelling_type_id, dwelling_type_name, location):
        """This is the constructor method that initializes the dwelling type class"""
        self.dwelling_type_id = dwelling_type_id
        self.dwelling_type_name = dwelling_type_name
        self.location = location

    def set_dwelling_type(self, dwelling_type_id, dwelling_type_name, location):
        """This is the setter method that sets the dwelling type attributes"""
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
    