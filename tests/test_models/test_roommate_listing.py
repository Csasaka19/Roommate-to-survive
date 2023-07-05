import unittest
from models.roommate_listing import roommate_listing

class RoommateListingTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a roommate_listing instance for testing
        self.roommate_listing = roommate_listing(
            user_id="123",
            roommate_id="456",
            roommate_description="Example roommate",
            roommate_price=200,
            roommate_availability=True,
            roommate_address="456 Main St",
            roommate_status="Available",
            roommate_preference="Non-smoker"
        )

    def test_get_user_id(self):
        # Verify that the correct user ID is returned
        self.assertEqual(self.roommate_listing.get_user_id(), "123")

    def test_get_roommate_id(self):
        # Verify that the correct roommate ID is returned
        self.assertEqual(self.roommate_listing.get_roommate_id(), "456")

    def test_get_roommate_description(self):
        # Verify that the correct roommate description is returned
        self.assertEqual(self.roommate_listing.get_roommate_description(), "Example roommate")

    def test_get_roommate_price(self):
        # Verify that the correct roommate price is returned
        self.assertEqual(self.roommate_listing.get_roommate_price(), 200)

    def test_get_roommate_availability(self):
        # Verify that the correct roommate availability is returned
        self.assertEqual(self.roommate_listing.get_roommate_availability(), True)

    def test_get_roommate_address(self):
        # Verify that the correct roommate address is returned
        self.assertEqual(self.roommate_listing.get_roommate_address(), "456 Main St")

    def test_get_roommate_status(self):
        # Verify that the correct roommate status is returned
        self.assertEqual(self.roommate_listing.get_roommate_status(), "Available")

    def test_get_roommate_preference(self):
        # Verify that the correct roommate preference is returned
        self.assertEqual(self.roommate_listing.get_roommate_preference(), "Non-smoker")

    def test_set_roommate_listing(self):
        # Verify that the roommate_listing attributes are set correctly
        user_id = "789"
        roommate_id = "987"
        roommate_description = "New roommate"
        roommate_price = 300
        roommate_availability = False
        roommate_address = "789 Main St"
        roommate_status = "Not Available"
        roommate_preference = "Quiet"
        self.roommate_listing.set_roommate_listing(user_id, roommate_id, roommate_description, roommate_price, roommate_availability, roommate_address, roommate_status, roommate_preference)
        self.assertEqual(self.roommate_listing.user_id, user_id)
        self.assertEqual(self.roommate_listing.roommate_id, roommate_id)
        self.assertEqual(self.roommate_listing.roommate_description, roommate_description)
        self.assertEqual(self.roommate_listing.roommate_price, roommate_price)
        self.assertEqual(self.roommate_listing.roommate_availability, roommate_availability)
        self.assertEqual(self.roommate_listing.roommate_address, roommate_address)
        self.assertEqual(self.roommate_listing.roommate_status, roommate_status)
        self.assertEqual(self.roommate_listing.roommate_preference, roommate_preference)

if __name__ == '__main__':
    unittest.main()
