"""Unit testing for the ChequingAccount class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_chequing_account.py
"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

import unittest

from datetime import date

from bank_account.chequing_account import ChequingAccount

from bank_account.bank_account import BankAccount

class TestChequingAccount(unittest.TestCase):
    
    """This class represents chequing account inherited from details 
    from BankAccount class.
    """
    
    def test_init_valid_inputs(self):
        
        """This function is to test the validity of valid inputs."""

        # Arrange
        account_number = 1001
        client_number = 2001
        balance = 500.00
        date_created = date.today()
        overdraft_limit = 100.00
        overdraft_rate = 0.05

        # Act
        account = ChequingAccount(account_number, client_number,
                                   balance, date_created,
                                   overdraft_limit, overdraft_rate)

        # Assert
        self.assertEqual(account._ChequingAccount__overdraft_limit,
                         100.00, 0.05)

    def test_init_invalid_overdraft_limit(self):
        
        """This function is to test invalid overdraft limit."""

        # Act
        account = ChequingAccount(1002, 2002, 500.00, date.today(),
                                  "invalid", 0.05)

        # Assert
        self.assertEqual(account._ChequingAccount__overdraft_limit,
                         0.0, 0.05)

    def test_withdraw_within_balance(self):
        
        """This function tests withdraw within balance."""

        # Arrange
        account = ChequingAccount(1003, 2003, 500.00, date.today(), 
                                  100.00, 0.05)

        # Act
        account.withdraw(200.00)

        # Assert
        self.assertEqual(300.00, round(account.balance, 2))

    def test_withdraw_using_overdraft(self):
        
        """This function tests withdraw using overdraft."""

        # Arrange
        account = ChequingAccount(1004, 2004, 100.00, date.today(),
                                  200.00, 0.05)

        # Act
        account.withdraw(250.00)

        # Assert
        self.assertEqual(-150.00, round(account.balance, 2))

    def test_withdraw_exceeds_overdraft(self):
        
        """This function tests withdraw exceeding overdraft."""

        # Arrange
        account = ChequingAccount(1005, 2005, 100.00, date.today(), 
                                  50.00, 0.05)

        # Act / Assert
        with self.assertRaises(ValueError):
            account.withdraw(200.00)

    def test_get_service_charges(self):
        
        """This function tests service charge calculation."""

        # Arrange
        account = ChequingAccount(1006, 2006, 500.00, date.today(), 
                                  100.00, 0.05)

        # Act
        actual = account.get_service_charges()

        # Assert
        expected = BankAccount.BASE_SERVICE_CHARGE
        self.assertEqual(expected, round(actual, 2))

    def test__str__(self):
        
        """This function checks if the string format is correct or not.
        """

        # Arrange
        account = ChequingAccount(1007, 2007, 500.00, date.today(),
                                  100.00, 0.05)

        # Act
        actual = str(account)

        # Assert
        self.assertIn("Account Type: Chequing", actual) 
 
if __name__ == "__main__":
    unittest.main()
