#!/usr/bin/python3
"""This is the review and rating module"""
from models.user_profile import user_profile as user


class review(user):
    """This is the review and rating class"""

    def __init__(self, room_id, rating, review_id, review_text, review_date):
        """This is init method that initializes the review and rating class"""
        self.user_id = super().get_user_id()
        self.room_id = room_id
        self.rating = rating
        self.review_id = review_id
        self.review_text = review_text
        self.review_date = review_date

    def set_review(self, room_id, rating, review_id, review_text, review_date):
        """This is the setter method that sets the review and rating attributes"""
        self.user_id = super().get_user_id()
        self.room_id = room_id
        self.rating = rating
        self.review_id = review_id
        self.review_text = review_text
        self.review_date = review_date

    def get_user_id(self):
        """This is the getter method that gets the user id and returns it"""
        return self.user_id

    def get_room_id(self):
        """This is the getter method that gets the room id and returns it"""
        return self.room_id

    def get_rating(self):
        """This is the getter method that gets the rating and returns it"""
        return self.rating

    def get_review_id(self):
        """This is the getter method that gets the review id and returns it"""""
        return self.review_id

    def get_review_text(self):
        """This is the getter method that gets the review text and returns it"""
        return self.review_text

    def get_review_date(self):
        """This is the getter method that gets the review date and returns it"""
        return self.review_date
