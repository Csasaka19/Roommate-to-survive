#!/bin/usr/python3
from models.location import location
from models.booking import booking
from models.dwelling_type import dwelling_type
from models.review import review
from models.user_profile import user_profile
from models.room_listing import room_listing
from models.roommate_listing import roommate_listing


def main():
    """Booking class test"""
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
    print("\n")

    """Dwelling type class test"""
    # Create a dwelling type instance
    my_dwelling_type = dwelling_type("73456-4", "Somewhere there", "location_address", "Machakos", "Kenya",
                                     "Best Apartment", 123, "Guest", "Somebarry", "something@gmail.com",
                                     "123-789-90-45", 2000,
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
    my_dwelling_type.set_location(new_location)
    my_dwelling_type.set_dwelling_type(new_user_id, new_dwelling_type_id, new_dwelling_type_name)

    # Get and print updated dwelling type attributes
    print("Updated User ID:", my_dwelling_type.get_user_id())
    print("Updated Dwelling Type ID:", my_dwelling_type.get_dwelling_type_id())
    print("Updated Dwelling Type Name:", my_dwelling_type.get_dwelling_type_name())
    print("Updated Location:", my_dwelling_type.get_location())
    print("\n")

    """Review class test"""
    # Create a review instance
    user_id = 123
    room_id = 1
    rating = 4.5
    review_id = 1
    review_text = "Great experience! Highly recommended."
    review_date = "2023-07-03"
    my_review = review(room_id, rating, review_id, review_text, review_date)
    my_review.set_user_id(user_id)

    # Get and print review attributes
    print("User ID:", my_review.get_user_id())
    print("Room ID:", my_review.get_room_id())
    print("Rating:", my_review.get_rating())
    print("Review ID:", my_review.get_review_id())
    print("Review Text:", my_review.get_review_text())
    print("Review Date:", my_review.get_review_date())

    # Set new review attributes
    new_user_id = 456
    new_room_id = 2
    new_rating = 3.8
    new_review_id = 2
    new_review_text = "Average stay. Room could be cleaner."
    new_review_date = "2023-07-04"
    my_review.set_user_id(new_user_id)
    my_review.set_review(new_room_id, new_rating, new_review_id, new_review_text, new_review_date)

    # Get and print updated review attributes
    print("Updated User ID:", my_review.get_user_id())
    print("Updated Room ID:", my_review.get_room_id())
    print("Updated Rating:", my_review.get_rating())
    print("Updated Review ID:", my_review.get_review_id())
    print("Updated Review Text:", my_review.get_review_text())
    print("Updated Review Date:", my_review.get_review_date())
    print("\n")

    """Location class test"""
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
    my_location.set_location(new_location_id, new_location_name, new_location_address, new_city, new_country,
                             new_location_description)

    # Get and print updated location attributes
    print("Updated Location ID:", my_location.get_location_id())
    print("Updated Location Name:", my_location.get_location_name())
    print("Updated Location Address:", my_location.get_location_address())
    print("Updated City:", my_location.get_city())
    print("Updated Country:", my_location.get_country())
    print("Updated Location Description:", my_location.get_location_description())
    print("\n")

    """Room listing class"""
    # Create a room listing instance
    listing = room_listing(
        room_id="123",
        room_description="Sample Room",
        room_price="1000",
        room_availability=True,
        room_address="Sample Address",
        room_status="Available",
    )

    listing.set_user_id("56-756")

    # Test the getter methods
    user_id = listing.get_user_id()
    room_id = listing.get_room_id()
    room_description = listing.get_room_description()
    room_price = listing.get_room_price()
    room_availability = listing.get_room_availability()
    room_address = listing.get_room_address()
    room_status = listing.get_room_status()

    # Print the results
    print("User ID:", user_id)
    print("Room ID:", room_id)
    print("Room Description:", room_description)
    print("Room Price:", room_price)
    print("Room Availability:", room_availability)
    print("Room Address:", room_address)
    print("Room Status:", room_status)
    print("\n")

    """Roommate listing class"""
    # Create a roommate listing instance
    # listing = roommate_listing(
    #     user="Me",
    #     roommate_id="456",
    #     roommate_description="Sample Roommate",
    #     roommate_price="500",
    #     roommate_availability=True,
    #     roommate_address="Sample Address",
    #     roommate_status="Available",
    #     roommate_preference="Female"
    # )

    # Set the user ID for the roommate listing
    # listing.set_user_id("445-6789")

    # # Test the getter methods
    # user_id = listing.get_user_id()
    # roommate_id = listing.get_roommate_id()
    # roommate_description = listing.get_roommate_description()
    # roommate_price = listing.get_roommate_price()
    # roommate_availability = listing.get_roommate_availability()
    # roommate_address = listing.get_roommate_address()
    # roommate_status = listing.get_roommate_status()
    # roommate_preference = listing.get_roommate_preference()

    # # Print the results
    # print("User ID:", user_id)
    # print("Roommate ID:", roommate_id)
    # print("Roommate Description:", roommate_description)
    # print("Roommate Price:", roommate_price)
    # print("Roommate Availability:", roommate_availability)
    # print("Roommate Address:", roommate_address)
    # print("Roommate Status:", roommate_status)
    # print("Roommate Preference:", roommate_preference)

    """User profile cass test"""
    profile = user_profile(
        location_id="123-90-76",
        location_name="Konza",
        location_address="nbo-066",
        city="Future City",
        country="Kenya",
        location_description="Best City in Machakos",
        user_id="user123",
        user_type="Regular",
        name="Incognitto cc",
        email="incognitto_cc@example.com",
        phone="0712345678",
        budget="10000",
        gender="Male",
        age=30
    )

    # Test the get_user_id() method
    user_id = profile.get_user_id()
    print("User ID:", user_id)

    # Test the create_password() method
    hashed_password = profile.create_password()
    print("Hashed Password:", hashed_password)

    # Test the create_account() method
    profile.create_account()


if __name__ == '__main__':
    main()
