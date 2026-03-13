"""This module contains the Investment account information."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from bank_account import BankAccount

from datetime import date

from datetime import date, timedelta

from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """ This represents Investment Account that inherits from 
    BankAccount.""" 

    def __init__(self, account_number, client_number, balance,
                 date_created, management_fee):
        
        """This class initializes the attributes of the BankAccount 
        class.

        Returns:
            account_number (int): An integer representing the bank 
            account number.
            client_number (int): An integer representing the client 
            number of the account holder.
            balance (float): A float representing the current balance 
            of the bank account.
            date_created (date): It represents the date.
            management_fee (float): A float representing the management 
            fee.
        """

        super().__init__(account_number, client_number, balance, 
                         date_created)

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55

        self.__service_charge_strategy = ManagementFeeStrategy(balance,
                                                        date_created,
                                                self.__management_fee)

    def get_service_charges(self) -> float:
        """This class is to get the service charges using the 
        ManagementFeeStrategy."""
        
        if self.__is_older_than_10_years():
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee
        
    def __is_older_than_10_years(self) -> bool:
        """Return True if the account is older than 10 years."""
        return self.date_created <= date.today() - timedelta(days=10*365.25)

    def __str__(self) -> str:
        """This function returns a string representation."""

        investment_information = super().__str__().strip()
 
        fee_display = "Waived" if self.__is_older_than_10_years() else f"${self.__management_fee:,.2f}"

        return (f"{investment_information}\n"
            f"Date Created: {self.date_created} "
            f"Management Fee: {fee_display} "
            f"Account Type: Investment")
    