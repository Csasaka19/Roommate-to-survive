#!/usr/bin/python3
"""This is the main location module.It creates a location instance and prints its attributes"""
from models.location import location

def main():
    # Create a location instance
    location_id = 1
    location_name = "Hotel XYZ"
    location_address = "123 Main Street"
    city = "Cityville"
    country = "Countryland"
    location_description = "A beautiful hotel in the heart of the city"
    my_location = location(location_id, location_name, location_address, city, country, location_description)

    # Get and print location attributes
    print("Location ID:", my_location.get_location_id())
    print("Location Name:", my_location.get_location_name())
    print("Location Address:", my_location.get_location_address())
    print("City:", my_location.get_city())
    print("Country:", my_location.get_country())
    print("Location Description:", my_location.get_location_description())

    # Set new location attributes
    new_location_id = 2
    new_location_name = "Resort ABC"
    new_location_address = "456 Beach Road"
    new_city = "Seaside"
    new_country = "Beachland"
    new_location_description = "A luxurious beachfront resort"
    my_location.set_location(new_location_id, new_location_name, new_location_address, new_city, new_country, new_location_description)

    # Get and print updated location attributes
    print("Updated Location ID:", my_location.get_location_id())
    print("Updated Location Name:", my_location.get_location_name())
    print("Updated Location Address:", my_location.get_location_address())
    print("Updated City:", my_location.get_city())
    print("Updated Country:", my_location.get_country())
    print("Updated Location Description:", my_location.get_location_description())

if __name__ == "__main__":
    main()
