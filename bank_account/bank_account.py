"""Module Documentation"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

class BankAccount:
    """This class represents a bank account with account number, client number, and balance."""

    def __init__(self, account_number, client_number, balance) -> None:
        """Initializes the attributes of the BankAccount class.

        Args:
            account_number (int): An integer representing the bank account number.
            client_number (int): An integer representing the client number of the account holder.
            balance (float): A float representing the current balance of the bank account.
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

    @property
    def account_number(self) -> int:
        """Returns the bank account number."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Returns the client number of the account holder."""
        return self.__client_number

    @property
    def balance(self) -> float:
        """Returns the current balance of the bank account."""
        return self.__balance

    def update_balance(self, amount) -> None:
        """Adds the given amount to the account balance if convertible to float.

        Args:
            amount (float): The amount to add (or subtract if negative).
        """
        try:
            self.__balance += float(amount)
        except (ValueError, TypeError):
            pass
        
    def deposit(self, amount) -> None:
        """Deposits a positive numeric amount to the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not numeric or not positive.
        """
        try:
            amount_float = float(amount)
        except (ValueError, TypeError):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount_float <= 0:
            raise ValueError(f"Deposit amount: ${amount_float:,.2f} must be positive.")

        self.update_balance(amount_float)

    def withdraw(self, amount) -> None:
        """Withdraws a positive numeric amount from the account if sufficient balance exists.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not numeric, not positive, or exceeds balance.
        """
        try:
            amount_float = float(amount)
        except (ValueError, TypeError):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")

        if amount_float <= 0:
            raise ValueError(f"Withdraw amount: ${amount_float:,.2f} must be positive.")

        if amount_float > self.__balance:
            raise ValueError(
                f"Withdraw amount: ${amount_float:,.2f} must not exceed the account balance: ${self.__balance:,.2f}."
            )

        self.update_balance(-amount_float)

    def __str__(self) -> str:
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}\n"