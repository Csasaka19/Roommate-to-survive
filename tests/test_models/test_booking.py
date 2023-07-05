import unittest
from datetime import date
from models.booking import booking

class BookingTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a booking instance for testing"""
        self.booking = booking(
            location_id="123",
            location_name="Example Location",
            location_address="123 Main St",
            city="City",
            country="Country",
            location_description="Example Description",
            user_id="456",
            user_type="Regular",
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            budget=100,
            gender="Male",
            age=30,
            booking_id="789",
            booking_date=date(2023, 7, 1)
        )

    def test_confirm_booking(self):
        """Verify that booking status is changed to "Confirmed" after confirming the booking"""
        self.booking.confirm_booking()
        self.assertEqual(self.booking.booking_status, "Confirmed")

    def test_cancel_booking(self):
        """Verify that booking status is changed to "Cancelled" after canceling the booking"""
        self.booking.cancel_booking()
        self.assertEqual(self.booking.booking_status, "Cancelled")

    def test_update_booking_date(self):
        """Verify that booking date is updated correctly"""
        new_date = date(2023, 8, 1)
        self.booking.update_booking_date(new_date)
        self.assertEqual(self.booking.booking_date, new_date)

if __name__ == '__main__':
    unittest.main()
