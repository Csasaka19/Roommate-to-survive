#!/usr/bin/python3
"""This is the booking module"""
from models.user_profile import user_profile as user


class booking(user):
    """This is the booking class"""
    def __init__(self, booking_id, user_id, booking_date):
        """This is the constructor method that initializes the booking class"""
        self.booking_id = booking_id
        super().__init__(user_id)
        self.booking_date = booking_date
        self.booking_status = "Pending"

    def confirm_booking(self):
        """Confirm the booking"""
        self.booking_status = "Confirmed"

    def cancel_booking(self):
        """Cancel the booking"""
        self.booking_status = "Cancelled"

    def update_booking_date(self, new_date):
        """Update the booking date"""
        self.booking_date = new_date
