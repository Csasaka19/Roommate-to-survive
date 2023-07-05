import unittest
import getpass
from requests import patch
from models.user_profile import user_profile


class UserProfileTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a user_profile instance for testing
        self.user_profile = user_profile(
            location_id="1",
            location_name="Test Location",
            location_address="123 Main St",
            city="Test City",
            country="Test Country",
            location_description="Test Description",
            user_id="123",
            user_type="Test Type",
            name="Test User",
            email="test@example.com",
            phone="123456789",
            budget="1000",
            gender="Male",
            age=25
        )

    def test_get_user_id(self):
        # Verify that the correct user ID is returned
        self.assertEqual(self.user_profile.get_user_id(), "123")

    def test_create_password_matching(self):
        # Verify that a password is created when matching passwords are provided
        self.assertEqual(self.user_profile.create_password(), "c4f1af9b5fbc5ae5a73d18898e4a3b89a1d4f8dbbf52f41e656e59ea18af2520")

    def test_create_password_not_matching(self):
        # Verify that None is returned when non-matching passwords are provided
        original_getpass = getpass.getpass
        getpass.getpass = lambda prompt: "password"
        self.assertIsNone(self.user_profile.create_password())
        getpass.getpass = original_getpass

    def test_create_account(self):
        # Verify that the account is created successfully
        original_input = input
        input_values = [
            "123",
            "Test Type",
            "Test User",
            "test@example.com",
            "123456789",
            "1000",
            "Test Location",
            "Test Country",
            "Male",
            "25",
            "password",
            "password",
        ]
        input_index = 0
        def mock_input(prompt):
            nonlocal input_index
            value = input_values[input_index]
            input_index += 1
            return value
        input = mock_input

        expected_output = [
            "Enter user ID: ",
            "Enter user type: ",
            "Enter name: ",
            "Enter email: ",
            "Enter phone number: ",
            "Enter budget: ",
            "Enter location: ",
            "Enter country: ",
            "Enter gender: ",
            "Enter age: ",
            "Enter password: ",
            "Confirm password: ",
            "Account created successfully!"
        ]

        with patch("builtins.input", side_effect=input):
            with patch("builtins.print") as mock_print:
                self.user_profile.create_account()

        printed_output = [call.args[0] for call in mock_print.call_args_list]
        self.assertEqual(printed_output, expected_output)

        input = original_input

if __name__ == '__main__':
    unittest.main()
