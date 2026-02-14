"""Unit testing for the InvestmentAccount class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_investment_account.py
"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

import unittest

from datetime import date

from bank_account.investment_account import InvestmentAccount

from bank_account.bank_account import BankAccount
 
class TestInvestmentAccount(unittest.TestCase):
    
    """This class represents InvestmentAccount inherited from 
    BankAccount class.
    """

    def setUp(self):
        
        """This function is for setting up common dates for tests."""

        self.today = date.today()
        self.old_date = self.today.replace(year = self.today.year - 11)
        self.recent_date = self.today.replace(year = self.today.year - 5)

    def test_init_valid_fee(self):
        
        """This function tests initialization with valid management fee.
        """

        # Act
        account = InvestmentAccount(1001, 5001, 1000.0, 
                                    self.recent_date, 5.0)

        # Assert
        self.assertEqual(account._InvestmentAccount__management_fee, 
                         5.0)
        self.assertEqual(account.account_number, 1001)
        self.assertEqual(account.client_number, 5001)
        self.assertEqual(account.balance, 1000.0)

    def test_init_invalid_fee(self):
        
        """This function tests initialization with invalid management 
        fee."""

        # Act
        account = InvestmentAccount(1002, 5002, 2000.0, 
                                    self.recent_date, "invalid")

        # Assert
        self.assertEqual(account._InvestmentAccount__management_fee, 
                         2.55)

    def test_is_older_than_10_years_true(self):
        
        """This function tests if account older than 10 years returns 
        True."""

        # Act
        account = InvestmentAccount(1003, 5003, 3000.0, self.old_date, 
                                    4.0)

        # Assert
        self.assertEqual(
            account._InvestmentAccount__is_older_than_10_years(), True)

    def test_is_older_than_10_years_false(self):
        
        """This function tests if account newer than 10 years returns 
        False."""

        # Act
        account = InvestmentAccount(
            1004, 5004, 4000.0, self.recent_date, 4.0)

        # Assert
        self.assertEqual(
            account._InvestmentAccount__is_older_than_10_years(), False)

    def test_service_charges_older_account(self):
        
        """This function tests service charges for account older than 
        10 years."""

        # Act
        account = InvestmentAccount(1005, 5005, 5000.0, self.old_date, 
                                    6.0)

        # Assert
        self.assertEqual(account.get_service_charges(), 
                         BankAccount.BASE_SERVICE_CHARGE)

    def test_service_charges_new_account(self):
        
        """This function tests service charges for account newer than 
        10 years."""

        # Act
        account = InvestmentAccount(1006, 5006, 6000.0, 
                                    self.recent_date, 6.0)
        expected_charge = BankAccount.BASE_SERVICE_CHARGE + 6.0

        # Assert
        self.assertEqual(account.get_service_charges(), expected_charge)

    def test_str_older_account(self):
        
        """This function tests string representation for older accounts.
        """

        # Act
        account = InvestmentAccount(1007, 5007, 7000.0, self.old_date, \
                                    7.0)
        account_str = str(account)

        # Assert
        self.assertIn("Waived", account_str)
        self.assertIn("Account Type: Investment", account_str)

    def test_str_new_account(self):
        
        """This function tests string representation for newer accounts.
        """

        # Act
        account = InvestmentAccount(1008, 5008, 8000.0, 
                                    self.recent_date, 7.0)
        account_str = str(account)

        # Assert
        self.assertIn("$7.00", account_str)
        self.assertIn("Account Type: Investment", account_str)

if __name__ == "__main__":
    unittest.main()
