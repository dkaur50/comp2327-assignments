"""This module conatins the Chequing account information."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from bank_account import BankAccount

from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """
    This represents Investment Account that inherits from BankAccount.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

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
            overdraft_limit (float): It represents float.
            overdraft_rate (float): It represents float.
        """
        
        super().__init__(account_number, client_number, balance, date_created)

        # Validate management_fee
        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55

    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges.

        If account is more than 10 years old:
            service charge = BASE_SERVICE_CHARGE
        Otherwise:
            service charge = BASE_SERVICE_CHARGE + management_fee
        """

        if self.date_created < InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self) -> str:
        """
        Returns formatted string representation.
        """

        base_info = super().__str__().strip()

        # Determine if management fee is waived
        if self.date_created < InvestmentAccount.TEN_YEARS_AGO:
            fee_display = "Waived"
        else:
            fee_display = f"${self.__management_fee:,.2f}"

        return (
            f"{base_info}\n"
            f"Date Created: {self.date_created} "
            f"Management Fee: {fee_display} "
            f"Account Type: Investment"
        )