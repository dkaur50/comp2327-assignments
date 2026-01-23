"""Unit testing for the Client class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase): 

    def test_init_valid_inputs(self):
        """This function is to test the validity of the initialised inputs"""
        
        # Arrange
        client_number = 101
        first_name = "Anne"
        last_name = "Clinton"
        email_address = "anne.clinton@gmail.com"

        # Act
        client = Client(client_number, first_name, last_name, email_address)

        # Assert
        self.assertEqual(client._Client__client_number, 1212)
        self.assertEqual(client._Client__first_name, "Anne")
        self.assertEqual(client._Client__last_name, "Clinton")
        self.assertEqual(client._Client__email_address, "anne.clinton@pixellriver.com")

    def test_init_invalid_client_number(self):
        with self.assertRaises(ValueError) as context:
            Client("abc", "Anne", "Clinton", "anne.clinton@pixellriver.com")

        self.assertEqual(
            str(context.exception),
            "The client number should be an integer."
        )

    def test_init_blank_first_name(self):
        with self.assertRaises(ValueError) as context:
            Client(1212, " ", "Clinton", "anne.clinton@pixellriver.com")

        self.assertEqual(
            str(context.exception),
            "The first_name cannot be blank."
        )

    def test_init_blank_last_name(self):
        with self.assertRaises(ValueError) as context:
            Client(1212, "Anne", " ", "anne.clinton@pixellriver.com")

        self.assertEqual(
            str(context.exception),
            "The last_name cannot be blank."
        )

    def test_init_invalid_email_address(self):
        with self.assertRaises(ValueError) as context:
            Client(1212, "Anne", "Clinton", "anne.clinton.gmail.com")

        self.assertEqual(
            str(context.exception),
            "The email_address is not valid."
        )

    # ---------- ACCESSOR TESTS ----------

    def test_get_client_number(self):
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        self.assertEqual(client.client_number, 1212)

    def test_get_first_name(self):
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        self.assertEqual(client.first_name, "Anne")

    def test_get_last_name(self):
        """This function is to check that whether the get_email_address 
        function is working or not.
        """

        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        self.assertEqual(client.last_name, "Clinton")

    def test_get_email_address(self):
        """This function is to check that whether the get_email_address 
        function is working or not.
        """
        
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        self.assertEqual(client.email_address, "anne.clinton@pixellriver.com")

    def test__str__(self):
        """This function is to check if the final test result has 
        the correct format as per the assignment requirements.
        """

        # Arrange
        client = Client(1212, "Anne", "Clinton", "anne@gmail.com")

        # Act
        actual = str(client)

        # Assert
        expected = "Clinton, Anne [1212] - anne@gmail.com"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
