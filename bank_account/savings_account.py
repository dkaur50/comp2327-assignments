"""This module file is regarding the BankAccount class."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    This represents Savings Account that inherits from BankAccount.
    """

    SERVICE_CHARGE_PREMIUM = 2.00

    def __init__(self, account_number, client_number, balance,
                 date_created, minimum_balance):
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
        
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.0

    def get_service_charges(self) -> float:
        
        """
        This function returns the calculated service charges.
        """

        if self.balance >= self.__minimum_balance:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return (BankAccount.BASE_SERVICE_CHARGE*SavingsAccount.SERVICE_CHARGE_PREMIUM)

    def __str__(self) -> str:
      
      """This function represents a string representation."""

        base_information = super().__str__().strip()

        return (f"{base_information}\n"
            f"Minimum Balance: ${self.__minimum_balance:,.2f} "
            f"Account Type: Savings"
        )