#!/usr/bin/python3
"""This is the main dwelling type module.It creates a dwelling type instance and prints its attributes"""
from models.dwelling_type import dwelling_type

def main():
    # Create a dwelling type instance
    my_dwelling_type = dwelling_type("location_id", "location_name", "location_address", "Machakos", "Kenya",
                 "Best Apartment", 123, "Guest", "Somebarry", "something@gmail.com","123-789-90-45", 2000,
                 "Male", 25, 3456, "Apartment")

    # Get and print dwelling type attributes
    print("User ID:", my_dwelling_type.get_user_id())
    print("Dwelling Type ID:", my_dwelling_type.get_dwelling_type_id())
    print("Dwelling Type Name:", my_dwelling_type.get_dwelling_type_name())
    print("Location:", my_dwelling_type.get_location())

    # Set new dwelling type attributes
    new_user_id = 456
    new_dwelling_type_id = 2
    new_dwelling_type_name = "House"
    new_location = "Suburb"
    my_dwelling_type.set_dwelling_type(new_user_id, new_dwelling_type_id, new_dwelling_type_name)

    # Get and print updated dwelling type attributes
    print("Updated User ID:", my_dwelling_type.get_user_id())
    print("Updated Dwelling Type ID:", my_dwelling_type.get_dwelling_type_id())
    print("Updated Dwelling Type Name:", my_dwelling_type.get_dwelling_type_name())
    print("Updated Location:", my_dwelling_type.get_location())

if __name__ == "__main__":
    main()
