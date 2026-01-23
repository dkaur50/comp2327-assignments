"""Unit testing for the BankAccount class.

Usage: 

To execute all tests in the terminal execute the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(account_number=101, client_number=1, balance=1000.0)

    def test_initial_attributes(self):
        self.assertEqual(self.account._BankAccount__balance, 1000.0)
        self.assertEqual(self.account.account_number, 101)
        self.assertEqual(self.account.client_number, 1)

    def test_deposit_valid(self):
        self.account.deposit(500.0)
        self.assertEqual(round(self.account._BankAccount__balance, 2), 1500.0)

    def test_deposit_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
        with self.assertRaises(ValueError):
            self.account.deposit("abc")

    def test_withdraw_valid(self):
        self.account.withdraw(300.0)
        self.assertEqual(round(self.account._BankAccount__balance, 2), 700.0)

    def test_withdraw_over_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000.0)

    def test_withdraw_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)
        with self.assertRaises(ValueError):
            self.account.withdraw("xyz")

    def test_multiple_operations(self):
        self.account.deposit(200.0)
        self.account.withdraw(150.0)
        expected_balance = 1000 + 200 - 150
        self.assertEqual(round(self.account._BankAccount__balance, 2), round(expected_balance, 2))

if __name__ == '__main__':
    unittest.main()