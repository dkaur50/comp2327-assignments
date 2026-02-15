"""Unit testing for the BankAccount class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest

from datetime import date

from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    
    """This class represents testing for the BankAccount class."""

    def test_init_valid_inputs(self):

        """This function tests for valid inputs."""

        # Arrange
        account_number = 101
        client_number = 1
        balance = 1000.00
        date_created = date.today()

        # Act
        account = BankAccount(account_number, client_number, balance,
                              date_created)

        # Assert
        self.assertEqual(account.account_number, 101)
        self.assertEqual(account.client_number, 1)
        self.assertEqual(account._BankAccount__balance, 1000.00)
        self.assertEqual(account.date_created, date_created)

    def test_deposit_valid(self):
        
        """This function tests for a valid deposit."""

        # Arrange
        account = BankAccount(101, 1, 1000.00, date.today())

        # Act
        account.deposit(500.00)

        # Assert
        self.assertEqual(1500.00, round(account._BankAccount__balance, 2))

    def test_deposit_invalid_amount(self):
        
        """This function is for testing invalid deposit amount."""

        # Arrange
        account = BankAccount(101, 1, 1000.00, date.today())

        # Assert
        with self.assertRaises(ValueError):
            account.deposit(-100)

        with self.assertRaises(ValueError):
            account.deposit("abc")

    def test_withdraw_valid(self):
        
        """This function tests for a valid withdraw."""

        # Arrange
        account = BankAccount(101, 1, 1000.00, date.today())

        # Act
        account.withdraw(300.00)

        # Assert
        self.assertEqual(700.00, round(account._BankAccount__balance, 2))

    def test_withdraw_over_balance(self):
        
        """This function is for testing the withdraw over balance."""

        # Arrange
        account = BankAccount(101, 1, 1000.00, date.today())

        # Assert
        with self.assertRaises(ValueError):
            account.withdraw(2000.00)

    def test_withdraw_invalid_amount(self):
        
        """This function tests for an invalid withdraw."""

        # Arrange
        account = BankAccount(101, 1, 1000.00, date.today())

        # Assert
        with self.assertRaises(ValueError):
            account.withdraw(-50)

        with self.assertRaises(ValueError):
            account.withdraw("xyz")

    def test_multiple_operations(self):
        
        """This function tests for multiple operations."""

        # Arrange
        account = BankAccount(101, 1, 1000.00, date.today())

        # Act
        account.deposit(200.00)
        account.withdraw(150.00)

        # Assert
        expected_balance = 1000 + 200 - 150
        self.assertEqual(round(expected_balance, 2),
                         round(account._BankAccount__balance, 2))


if __name__ == "__main__":
    unittest.main()
