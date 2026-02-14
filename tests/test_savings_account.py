"""Unit testing for the SavingsAccount class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_savings_account.py
"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

import unittest

from datetime import date

from bank_account.savings_account import SavingsAccount

from bank_account.bank_account import BankAccount
 
class TestSavingsAccount(unittest.TestCase):
    
    """This class represents SavingsAccount inherited from the
    BankAccount class.
    """

    def test_init_valid_minimum_balance(self):
        
        """This function tests whether the minimum balance is valid."""

        # Arrange
        self.today = date.today()

        # Act
        account = SavingsAccount(2001, 6001, 1000.0, self.today, 500.0)

        # Assert
        self.assertEqual(account._SavingsAccount__minimum_balance, 
                         500.0)
        self.assertEqual(account.account_number, 2001)
        self.assertEqual(account.client_number, 6001)
        self.assertEqual(account.balance, 1000.0)

    def test_init_invalid_minimum_balance(self):
        
        """This function tests whether the minimum balance is invalid.
        """

        # Act
        account = SavingsAccount(2002, 6002, 800.0, self.today, 
                                 "invalid")

        # Assert
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.0)

    def test_service_charges_above_minimum(self):
        
        """This function tests the service charges when balance is 
        above minimum balance."""

        # Act
        account = SavingsAccount(2003, 6003, 1000.0, self.today, 500.0)

        # Assert
        self.assertEqual(account.get_service_charges(), 
                         BankAccount.BASE_SERVICE_CHARGE)

    def test_service_charges_below_minimum(self):
        
        """This function tests the service charges when balance is 
        below minimum balance."""

        # Act
        account = SavingsAccount(2004, 6004, 200.0, self.today, 500.0)

        expected_charge = (BankAccount.BASE_SERVICE_CHARGE * 
                           SavingsAccount.SERVICE_CHARGE_PREMIUM)

        # Assert
        self.assertEqual(account.get_service_charges(), expected_charge)

    def test_str_representation(self):
        
        """This function tests the string representation of 
        SavingsAccount."""

        # Act
        account = SavingsAccount(2005, 6005, 1000.0, self.today, 500.0)
        account_str = str(account)

        # Assert
        self.assertIn("Minimum Balance: $500.00", account_str)
        self.assertIn("Account Type: Savings", account_str)

if __name__ == "__main__":
    unittest.main()
