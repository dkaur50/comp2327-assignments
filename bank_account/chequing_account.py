"""This module file is regarding the BankAccount class."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from bank_account import BankAccount

from abc import ABC, abstractmethod

import time

from datetime import date


class ChequingAccount(BankAccount):
    def __init__(self, account_number, client_number, balance, 
                 date_created, overdraft_limit, overdraft_rate):
        
        super().__init__(account_number, client_number, balance, 
                         date_created)
        
        try:
            self.__overdraft_limit = overdraft_limit
            return ("The overdraft limit value is valid.")
        except ValueError:
            self.__overdraft_limit = -100.0
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05

    @property
    def overdraft_limit(self):

        """This function represents the overdraft limit which is a 
        float.
        """
        return self.__overdraft_limit

    @property
    def overdraft_rate(self):
        
        """This function represents the overdraft rate which is a float.
        """
        return self.__overdraft_rate

    # Override withdraw to include overdraft limit
    def withdraw(self, amount):

        if not isinstance(amount, (int, float)):
            raise ValueError("Withdraw amount must be numeric.")

        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")

        # Check against overdraft limit
        if amount > (self.balance - self.__overdraft_limit):
            raise ValueError(
                f"Withdraw amount ${amount:,.2f} exceeds overdraft limit. "
                f"Max available: ${self.balance - self.__overdraft_limit:,.2f}"
            )

        # Perform withdrawal
        self.update_balance(-amount)

    # Override __str__ to include overdraft info
    def __str__(self):
        account_number_and_balance = super().__str__().strip()
        account_information = (
            f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
            f"Overdraft Rate: {self.__overdraft_rate*100:.2f}% "
            f"Account Type: Chequing")
        return f"{account_number_and_balance}\n{account_information}"
    