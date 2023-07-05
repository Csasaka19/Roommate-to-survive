import unittest
from models.location import location

class LocationTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a location instance for testing
        self.location = location(
            location_id="123",
            location_name="Example Location",
            location_address="123 Main St",
            city="City",
            country="Country",
            location_description="Example Description"
        )

    def test_get_location_id(self):
        # Verify that the correct location ID is returned
        self.assertEqual(self.location.get_location_id(), "123")

    def test_get_location_name(self):
        # Verify that the correct location name is returned
        self.assertEqual(self.location.get_location_name(), "Example Location")

    def test_get_location_address(self):
        # Verify that the correct location address is returned
        self.assertEqual(self.location.get_location_address(), "123 Main St")

    def test_get_city(self):
        # Verify that the correct city is returned
        self.assertEqual(self.location.get_city(), "City")

    def test_get_country(self):
        # Verify that the correct country is returned
        self.assertEqual(self.location.get_country(), "Country")

    def test_get_location_description(self):
        # Verify that the correct location description is returned
        self.assertEqual(self.location.get_location_description(), "Example Description")

    def test_set_location(self):
        # Verify that the location attributes are set correctly
        location_id = "456"
        location_name = "New Location"
        location_address = "456 Main St"
        city = "New City"
        country = "New Country"
        location_description = "New Description"
        self.location.set_location(location_id, location_name, location_address, city, country, location_description)
        self.assertEqual(self.location.location_id, location_id)
        self.assertEqual(self.location.location_name, location_name)
        self.assertEqual(self.location.location_address, location_address)
        self.assertEqual(self.location.city, city)
        self.assertEqual(self.location.country, country)
        self.assertEqual(self.location.location_description, location_description)

if __name__ == '__main__':
    unittest.main()
