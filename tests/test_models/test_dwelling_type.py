import unittest
from models.dwelling_type import dwelling_type

class DwellingTypeTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a dwelling_type instance for testing"""
        self.dwelling_type = dwelling_type(
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
            dwelling_type_id="789",
            dwelling_type_name="Apartment"
        )

    def test_get_dwelling_type_id(self):
        """Verify that the correct dwelling type ID is returned"""
        self.assertEqual(self.dwelling_type.get_dwelling_type_id(), "789")

    def test_get_dwelling_type_name(self):
        """Verify that the correct dwelling type name is returned"""
        self.assertEqual(self.dwelling_type.get_dwelling_type_name(), "Apartment")

    def test_get_location(self):
        """Verify that the correct location is returned"""
        location = {
            "location_id": "123",
            "location_name": "Example Location",
            "location_address": "123 Main St",
            "city": "City",
            "country": "Country",
            "location_description": "Example Description"
        }
        self.assertEqual(self.dwelling_type.get_location(), location)

    def test_set_dwelling_type(self):
        """Verify that the dwelling type attributes are set correctly"""
        user_id = "987"
        dwelling_type_id = "654"
        dwelling_type_name = "House"
        self.dwelling_type.set_dwelling_type(user_id, dwelling_type_id, dwelling_type_name)
        self.assertEqual(self.dwelling_type.user_id, user_id)
        self.assertEqual(self.dwelling_type.dwelling_type_id, dwelling_type_id)
        self.assertEqual(self.dwelling_type.dwelling_type_name, dwelling_type_name)

if __name__ == '__main__':
    unittest.main()
