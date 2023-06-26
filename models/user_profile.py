#!/usr/bin/python3
"""This is the user profile module"""
import hashlib
import getpass


class user_profile():
    """This is the user profile class"""

    def __init__(self, user_id, user_type, name, email, phone, budget, location, country, gender, age):
        """This is the constructor method that initiates the user profile object"""
        self.user_id = user_id
        self.user_type = user_type
        self.name = name
        self.email = email
        self.phone = phone
        self.budget = budget
        self.location = location
        self.country = country
        self.gender = gender
        self.age = age

    def create_password(self):
        """This method creates a password for the user and returns the hashed password"""
        password = getpass.getpass("Enter password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password == confirm_password:
            # Use hashlib to encrypt the password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            return hashed_password
        else:
            print("Passwords do not match. Please try again.")
            return None

    def create_account(self):
        """This method creates a new user account that allows the user to create an account on the system"""
        print("Create a new account")
        self.user_id = input("Enter user ID: ")
        self.user_type = input("Enter user type: ")
        self.name = input("Enter name: ")
        self.email = input("Enter email: ")
        self.phone = input("Enter phone number: ")
        self.budget = input("Enter budget: ")
        self.location = input("Enter location: ")
        self.country = input("Enter country: ")
        self.gender = input("Enter gender: ")
        self.age = int(input("Enter age: "))

        # Set password
        hashed_password = self.create_password()
        if hashed_password:
            self.password = hashed_password
            print("Account created successfully!")
        else:
            print("Failed to create an account.")

# Usage example
# user = UserProfile("", "", "", "", "", "", "", "", "", 0)
# user.create_account()
