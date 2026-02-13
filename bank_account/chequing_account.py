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
            self.__overdraft_limit = float(overdraft_limit)
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

    def get_service_charges(self) -> float:
        
        """This is a function gets the charges."""
        if self.balance >= self.__overdraft_limit:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + \
            (self.__overdraft_limit - self.balance) * self.__overdraft_rate

    def __str__(self):
        
        """This function represents a string representation."""
        account_number_and_balance = super().__str__().strip()
        account_information = (
            f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
            f"Overdraft Rate: {self.__overdraft_rate*100:.2f}% "
            f"Account Type: Chequing")
        return f"{account_number_and_balance}\n{account_information}"
    