"""Unit testing for the Client class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client


class TestClient(unittest.TestCase):

    # ---------- __init__ TESTS ----------

    def test_init_valid_inputs(self):
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")

        # name-mangled attribute access
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
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        self.assertEqual(client.last_name, "Clinton")

    def test_get_email_address(self):
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        self.assertEqual(client.email_address, "anne.clinton@pixellriver.com")

    # ---------- __str__ TEST ----------

    def test_str_returns_expected_format(self):
        client = Client(1212, "Anne", "Clinton", "anne.clinton@pixellriver.com")
        expected = "Clinton, Anne [1212] - anne.clinton@pixellriver.com"
        self.assertEqual(str(client), expected)


if __name__ == "__main__":
    unittest.main()