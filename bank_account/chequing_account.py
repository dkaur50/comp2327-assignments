"""This module conatins the Chequing account information."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from bank_account import BankAccount

from abc import ABC, abstractmethod

import time

from datetime import date 

class ChequingAccount(BankAccount):

    """This class represents chequing account inherited from details 
    from BankAccount class.
    """

    def __init__(self, account_number, client_number, balance, 
                 date_created, overdraft_limit, overdraft_rate):
        
        """Initializes the attributes of the BankAccount class.

        Args:
            account_number (int): An integer representing the bank 
            account number.
            client_number (int): An integer representing the client 
            number of the account holder.
            balance (float): A float representing the current balance 
            of the bank account.
            date_created (date): It represents the date.
            overdraft_limit (float): It represents float.
            overdraft_rate (float): It represents float.
        """
        
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
            (self.__overdraft_limit-self.balance)*self.__overdraft_rate

    def __str__(self):
        
        """This function represents a string representation."""
        account_number_and_balance = super().__str__().strip()
        account_information = (
            f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
            f"Overdraft Rate: {self.__overdraft_rate*100:.2f}% "
            f"Account Type: Chequing")
        return f"{account_number_and_balance}\n{account_information}"
    