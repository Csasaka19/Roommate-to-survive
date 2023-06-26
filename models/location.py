#!/usr/bin/python3
"""This is the location related module"""


class location():
    """This is the location related class"""

    def __init__(self, location_id, location_name, location_address, city,
                 country, location_description):
        """This is the location related constructor method
        and it initializes the location related class"""
        self.location_id = location_id
        self.location_name = location_name
        self.location_address = location_address
        self.city = city
        self.country = country
        self.location_description = location_description

    def set_location(self, location_id, location_name,
                     location_address, city, country, location_description):
        """This is the setter method that sets the location
        related attributes of the location related class"""
        self.location_id = location_id
        self.location_name = location_name
        self.location_address = location_address
        self.city = city
        self.country = country
        self.location_description = location_description

    def get_location_id(self):
        """This is the getter method that gets the
        location id and returns it"""
        return self.location_id

    def get_location_name(self):
        """This is the getter method that gets the
        location name and returns it"""
        return self.location_name

    def get_location_address(self):
        """This is the getter method that gets the
        location address and returns it"""
        return self.location_address

    def get_city(self):
        """This is the getter method that gets the city and returns it"""
        return self.city

    def get_country(self):
        """This is the getter method that gets the country and returns it"""
        return self.country

    def get_location_description(self):
        """This is the getter method that gets the
        location description and returns it"""
        return self.location_description
