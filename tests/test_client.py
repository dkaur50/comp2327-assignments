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
        """This function is to test the validity of the valid inputs"""
        
        # Arrange
        client_number = 1212
        first_name = "Anne"
        last_name = "Clinton"
        email_address = "anne.clinton@pixellriver.com"

        # Act
        client = Client(client_number, first_name, last_name, email_address)

        # Assert
        self.assertEqual(client._Client__client_number, 1212)
        self.assertEqual(client._Client__first_name, "Anne")
        self.assertEqual(client._Client__last_name, "Clinton")
        self.assertEqual(client._Client__email_address, "anne.clinton@pixellriver.com")

    def test_init_invalid_client_number(self):
        """This function is to test invalid client number."""

        # Arrange
        client_number = "abc"

        # Act
        with self.assertRaises(ValueError) as context:
            Client(client_number, "Anne", "Clinton", "anne@gmail.com")

        # Assert
        self.assertEqual(str(context.exception),
                        "The client_number should be an integer.")

    def test_blank_first_name(self):
        """This function is to test blank first name."""

        # Arrange
        first_name = " "

        # Act
        with self.assertRaises(ValueError) as context:
            Client(101, first_name, "Clinton", "anne@gmail.com")

        # Assert
        self.assertEqual(str(context.exception),
                         "The first_name cannot be blank.")

    def test_blank_last_name(self):
        """This function is to test blank last name."""

        # Arrange
        last_name = " "

        # Act
        with self.assertRaises(ValueError) as context:
            Client(101, "Anne", last_name, "anne@gmail.com")

        # Assert
        self.assertEqual(str(context.exception),
                        "The last_name cannot be blank.")

    def test_invalid_email_address(self):
        """This function is to check invalid email address."""

        # Arrange
        invalid_email = "anne.clinton.gmail.com"

        # Act
        invalid_email = "anne.clinton.gmail.com"

        #
        with self.assertRaises(ValueError):
            Client(101, "Anne", "Clinton", invalid_email)
        
    def test_get_client_number(self):
        """This function is to check that whether the get_client_number
        function is working or not.
        """

        # Arrange
        client = Client(1212, "Anne", "Clinton", "anne@pixellriver.com")

        # Act
        actual = client.client_number

        # Assert
        self.assertEqual(actual, 1212)

    def test_get_first_name(self):
        """This function is to check that whether the get_first_name
        function is working or not.
        """
        
        # Arrange
        client = Client(1212, "Anne", "Clinton", "anne@pixellriver.com")

        # Act
        actual = client.first_name

        # Assert
        self.assertEqual(actual, "Anne")

    def test_get_last_name(self):
        """This function is to check that whether the get_last_name
        function is working or not.
        """

        # Arrange
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        
        # Act
        actual = client.last_name

        # Assert
        self.assertEqual(actual, "Clinton")

    def test_get_email_address(self):
        """This function is to check that whether the get_email_address 
        function is working or not.
        """

        # Arrange
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        
        # Act
        actual = client.email_address

        # Assert
        self.assertEqual(actual, "anne@pixellriver.com")

    def test__str__(self):
        """This function is to check if the final test result has 
        the correct format as per the assignment requirements.
        """

        # Arrange
        client = Client(1212, "Anne", "Clinton", "anne@pixellriver.com")

        # Act
        actual = str(client)

        # Assert
        expected = "Clinton, Anne [1212] - anne@pixellriver.com"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
