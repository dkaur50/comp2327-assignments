"""This module file is regarding the BankAccount class."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

import time

from datetime import date

class BankAccount:
    """This class represents a bank account with account number, 
    client number, and balance.
    """

    def __init__(self, account_number, client_number, balance, date_created) -> None:
        """Initializes the attributes of the BankAccount class.

        Args:
            account_number (int): An integer representing the bank 
            account number.
            client_number (int): An integer representing the client 
            number of the account holder.
            balance (float): A float representing the current balance 
            of the bank account.
        """
        if type(account_number) != int:
            raise ValueError("The account_number should be an integer.")
        self.__account_number = account_number

        if type(client_number) != int:
            raise ValueError("The client_number should be an integer.")
        self.__client_number = client_number

        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0
        
        if isinstance(date_created, date):
            self.date_created = date_created

    BASE_SERVICE_CHARGE = 0.50    

    @property
    def account_number(self) -> int:
        
        """This function returns the bank account number."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        
        """This function returns the client number of the account 
        holder.
        """
        return self.__client_number

    @property
    def balance(self) -> float:

        """This function returns the current balance of the bank 
        account.
        """
        return self.__balance
    
    @property
    def date_created(self) -> int:
        
        """"""
        return date.today()

    def update_balance(self, amount: float) -> None:
        
        """This function adds the given amount to the account balance 
        if the amount has valid type which is float.

        Args:
            amount (float): The amount to add (or subtract if negative).
        """
        if type(amount) == float:
            self.__balance += float(amount)
        else: 
            raise ValueError
        
    def deposit(self, amount: float) -> None:

        """This function deposits a positive numeric amount to the 
        account balance.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not numeric or not positive.
        """
        if type(amount) != float:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")

        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:

        """This function withdraws a positive numeric amount from the 
        account if sufficient balance exists.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not numeric, not positive, or 
            exceeds balance.
        """
        if type(amount) != float:
            raise ValueError(
                f"Withdraw amount: {amount} must be numeric.")

        if amount <= 0:
            raise ValueError(
                f"Withdraw amount: ${amount:,.2f} must be positive.")

        if amount > self.__balance:
            raise ValueError(
                f"Withdraw amount: ${amount:,.2f} must not exceed" 
                f"the account balance: ${self.__balance:,.2f}.")

        self.update_balance(-amount)

    def get_service_charges(self):
        
        """This function will return the calculated service charges 
        that a BankAccount will incur.
        """

        return BankAccount.BASE_SERVICE_CHARGE

    def __str__(self) -> str:

        """This function represents the string representation of how 
        the information needs to be returned.
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}\n"
    