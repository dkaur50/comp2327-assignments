import unittest
from datetime import date
from chequing_account import ChequingAccount


class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        self.account = ChequingAccount(
            1001,
            2001,
            -600.0,
            date(2024, 1, 1),
            -100.0,
            0.05
        )

    # ------------------------------
    # Test Initialization
    # ------------------------------

    def test_overdraft_limit_initialized(self):
        self.assertEqual(
            -100.0,
            self.account._ChequingAccount__overdraft_limit
        )

    def test_overdraft_rate_initialized(self):
        self.assertEqual(
            0.05,
            self.account._ChequingAccount__overdraft_rate
        )

    # ------------------------------
    # Test Service Charges
    # ------------------------------

    def test_service_charge_when_below_limit(self):
        expected_value = 25.50
        actual_value = self.account.get_service_charges()

        self.assertEqual(expected_value, round(actual_value, 2))

    def test_service_charge_when_equal_limit(self):
        account = ChequingAccount(
            1002,
            2002,
            -100.0,
            date(2024, 1, 1),
            -100.0,
            0.05
        )

        expected_value = 0.50
        actual_value = account.get_service_charges()

        self.assertEqual(expected_value, round(actual_value, 2))

    def test_service_charge_when_above_limit(self):
        account = ChequingAccount(
            1003,
            2003,
            0.0,
            date(2024, 1, 1),
            -100.0,
            0.05
        )

        expected_value = 0.50
        actual_value = account.get_service_charges()

        self.assertEqual(expected_value, round(actual_value, 2))


if __name__ == "__main__":
    unittest.main()