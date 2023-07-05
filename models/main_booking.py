from booking import booking

def main():
    # Create a booking object
    booking_obj = booking(location_id=123, location_name="Hotel ABC", location_address="123 Main Street",
                          city="City XYZ", country="Country XYZ", location_description="Beautiful hotel",
                          user_id=456, user_type="Guest", name="John Doe", email="john.doe@example.com",
                          phone="123-456-7890", budget=1000, gender="Male", age=30,
                          booking_id=789, booking_date="2023-07-10")

    # Print the initial booking status
    print("Initial Booking Status:", booking_obj.booking_status)

    # Confirm the booking
    booking_obj.confirm_booking()
    print("Booking Status after confirmation:", booking_obj.booking_status)

    # Update the booking date
    booking_obj.update_booking_date("2023-07-15")
    print("Updated Booking Date:", booking_obj.booking_date)

    # Cancel the booking
    booking_obj.cancel_booking()
    print("Booking Status after cancellation:", booking_obj.booking_status)

if __name__ == '__main__':
    main()
