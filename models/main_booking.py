#!/usr/bin/python3
"""This module is the main booking module which tests the booking class"""
from models.booking import booking
from models.user_profile import user_id as user_id

def main():
    # Create a booking instance
    booking_id = 1
    user_id = 123
    booking_date = "2023-07-03"
    my_booking = booking(booking_id, user_id, booking_date)

    # Print initial booking status
    print("Initial Booking Status:", my_booking.booking_status)

    # Confirm the booking
    my_booking.confirm_booking()
    print("Updated Booking Status:", my_booking.booking_status)

    # Update the booking date
    new_date = "2023-07-04"
    my_booking.update_booking_date(new_date)
    print("Updated Booking Date:", my_booking.booking_date)

    # Cancel the booking
    my_booking.cancel_booking()
    print("Updated Booking Status:", my_booking.booking_status)

if __name__ == "__main__":
    main()
