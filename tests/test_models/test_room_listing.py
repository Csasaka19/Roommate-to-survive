import unittest
from models.room_listing import room_listing

class RoomListingTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a room_listing instance for testing
        self.room_listing = room_listing(
            room_id="123",
            room_description="Example room",
            room_price=100,
            room_availability=True,
            room_address="123 Main St",
            room_status="Available",
            user_id="789"
        )

    def test_get_user_id(self):
        # Verify that the correct user ID is returned
        self.assertEqual(self.room_listing.get_user_id(), "789")

    def test_get_room_id(self):
        # Verify that the correct room ID is returned
        self.assertEqual(self.room_listing.get_room_id(), "123")

    def test_get_room_description(self):
        # Verify that the correct room description is returned
        self.assertEqual(self.room_listing.get_room_description(), "Example room")

    def test_get_room_price(self):
        # Verify that the correct room price is returned
        self.assertEqual(self.room_listing.get_room_price(), 100)

    def test_get_room_availability(self):
        # Verify that the correct room availability is returned
        self.assertEqual(self.room_listing.get_room_availability(), True)

    def test_get_room_address(self):
        # Verify that the correct room address is returned
        self.assertEqual(self.room_listing.get_room_address(), "123 Main St")

    def test_get_room_status(self):
        # Verify that the correct room status is returned
        self.assertEqual(self.room_listing.get_room_status(), "Available")

    def test_set_room_listing(self):
        # Verify that the room_listing attributes are set correctly
        user_id = "987"
        room_id = "456"
        room_description = "New room"
        room_price = 200
        room_availability = False
        room_address = "456 Main St"
        room_status = "Not Available"
        self.room_listing.set_room_listing(user_id, room_id, room_description, room_price, room_availability, room_address, room_status)
        self.assertEqual(self.room_listing.user_id, user_id)
        self.assertEqual(self.room_listing.room_id, room_id)
        self.assertEqual(self.room_listing.room_description, room_description)
        self.assertEqual(self.room_listing.room_price, room_price)
        self.assertEqual(self.room_listing.room_availability, room_availability)
        self.assertEqual(self.room_listing.room_address, room_address)
        self.assertEqual(self.room_listing.room_status, room_status)

if __name__ == '__main__':
    unittest.main()
