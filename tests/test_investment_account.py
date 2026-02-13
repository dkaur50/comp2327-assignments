import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount


class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        """Set up reusable dates"""
        self.recent_date = date.today()
        self.old_date = date.today() - timedelta(days=11 * 365)

    # -------------------------------------------------
    # __init__ Tests
    # -------------------------------------------------

    def test_management_fee_valid_float(self):
        account = InvestmentAccount(1001, 2001, 1000.00,
                                    self.recent_date, 1.99)

        self.assertEqual(1.99,
                         account._InvestmentAccount__management_fee)

    def test_management_fee_convertible_string(self):
        account = InvestmentAccount(1002, 2002, 1000.00,
                                    self.recent_date, "3.25")

        self.assertEqual(3.25,
                         account._InvestmentAccount__management_fee)

    def test_management_fee_invalid_value_defaults(self):
        account = InvestmentAccount(1003, 2003, 1000.00,
                                    self.recent_date, "invalid")

        self.assertEqual(2.55,
                         account._InvestmentAccount__management_fee)

    # -------------------------------------------------
    # get_service_charges Tests
    # -------------------------------------------------

    def test_service_charge_recent_account(self):
        account = InvestmentAccount(1004, 2004, 1000.00,
                                    self.recent_date, 2.00)

        expected = BankAccount.BASE_SERVICE_CHARGE + 2.00
        actual = account.get_service_charges()

        self.assertEqual(expected, round(actual, 2))

    def test_service_charge_old_account_fee_waived(self):
        account = InvestmentAccount(1005, 2005, 1000.00,
                                    self.old_date, 2.00)

        expected = BankAccount.BASE_SERVICE_CHARGE
        actual = account.get_service_charges()

        self.assertEqual(expected, round(actual, 2))

    # -------------------------------------------------
    # __str__ Tests
    # -------------------------------------------------

    def test_str_recent_account_shows_fee(self):
        account = InvestmentAccount(1006, 2006, 1000.00,
                                    self.recent_date, 2.00)

        result = str(account)

        self.assertIn("Management Fee: $2.00", result)
        self.assertIn("Account Type: Investment", result)

    def test_str_old_account_shows_waived(self):
        account = InvestmentAccount(1007, 2007, 1000.00,
                                    self.old_date, 2.00)

        result = str(account)

        self.assertIn("Management Fee: Waived", result)
        self.assertIn("Account Type: Investment", result)


if __name__ == '__main__':
    unittest.main()