"""This module conatins the Investment account information."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from bank_account import BankAccount

from datetime import date

class InvestmentAccount(BankAccount):
    """
    This represents Investment Account that inherits from BankAccount.
    """ 

    def __init__(self, account_number, client_number, balance,
                 date_created, management_fee):
        
        """Initializes the attributes of the BankAccount class.

        Args:
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

    def __is_older_than_10_years(self) -> bool:
        
        """
        This function determines if the account is more than 10 years 
        old."""

        today = date.today()
        year_difference = today.year - self.date_created.year

        if year_difference > 10:
            return True

        if year_difference == 10:
            if (today.month, today.day) > (
                    self.date_created.month, self.date_created.day):
                return True

        return False

    def get_service_charges(self) -> float:
        
        """
        This function returns the calculated service charges.
        """

        if self.__is_older_than_10_years():
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return (BankAccount.BASE_SERVICE_CHARGE +
                    self.__management_fee)

    def __str__(self) -> str:
        
        """
        This function returns formatted string representation.
        """

        investment_information = super().__str__().strip()
 
        if self.__is_older_than_10_years():
            fee_display = "Waived"
        else:
            fee_display = f"${self.__management_fee:,.2f}"

        return (f"{investment_information}\n"
            f"Date Created: {self.date_created} "
            f"Management Fee: {fee_display} "
            f"Account Type: Investment")
    