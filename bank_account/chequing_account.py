"""This module conatins the Chequing account information."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from bank_account import BankAccount
 
import time

from datetime import date

from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount): 
    """This class represents chequing account inherited from details 
    from BankAccount class.
    """

    def __init__(self, account_number, client_number, balance, 
                 date_created, overdraft_limit, overdraft_rate) -> None: 
        """This class if for initializing the attributes of the 
        BankAccount class.

        Returns:
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
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05
 
        self.__service_charge_strategy = OverdraftStrategy(
                                                self.__overdraft_limit,
                                                self.__overdraft_rate)

    @property
    def overdraft_limit(self) -> None: 
        """This function represents the overdraft limit which is a 
        float.
        """

        return self.__overdraft_limit

    @property
    def overdraft_rate(self) -> None: 
        """This function represents the overdraft rate which is a float.
        """

        return self.__overdraft_rate

    def withdraw(self, amount: float) -> None:

        if type(amount) != float:
            raise ValueError("Withdraw amount must be numeric.")

        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")

        new_balance = self.balance - amount

        if new_balance < -self.overdraft_limit:
            raise ValueError(
                f"Withdrawal exceeds overdraft limit.")

        self._BankAccount__balance = new_balance

    def get_service_charges(self) -> float:
        """This is a function gets the charges.""" 
        
        return self.__service_charge_strategy.calculate_service_charges(self.balance) 
 
    def __str__(self): 
        """This function represents a string representation."""
        
        account_number_and_balance = super().__str__().strip()
        
        account_information = (
            f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
            f"Overdraft Rate: {self.__overdraft_rate*100:.2f}% "
            f"Account Type: Chequing")
        
        return f"{account_number_and_balance}\n{account_information}"
    