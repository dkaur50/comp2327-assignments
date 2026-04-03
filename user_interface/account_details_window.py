"""Defines the AccountDetailsWindow class."""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Divjot Kaur"

class AccountDetailsWindow(DetailsWindow):
    """Represents a detail window used to display account details and 
    perform bank account transactions.gave
    """

    balance_updated = Signal(object)

    def __init__(self, account: BankAccount) -> None:
        """Initializes a new instance of the AccountDetailsWindow class.
        
        Args:
            account (BankAccount): The bank account to be displayed.
        """

        super().__init__()

        if isinstance(account, BankAccount): 

            self.account = account
            
            # Setting labels.
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # Establishing connections.
            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)

        else:
            # This happens when the account parameter is not of any 
            # BankAccount type.
            raise TypeError("Invalid type of Bank Account.")

    def on_apply_transaction(self):
        """This funtion acts as a slot methord for the deposit_button 
        and the withdraw_button clicked signals.
        """
        
        try:
            # Below is the code to convert the amount entered into the 
            # transaction_amount_edit widget to float. 
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            sender = self.sender()

            # This is when the sender is the deposit_button.
            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)

            # This is when the sender is the withdraw button.
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)
 
            # Below codes are to update the balance_label widget with the 
            # updated balance value of the account attribute.

            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.balance_updated.emit(self.account)
        
        except Exception as error:
                QMessageBox.warning(self, f"{transaction_type} Failed",
                    f"{transaction_type} has been failed: {(error)}")

    def on_exit(self):
        """This function acts as a slot for the exit_button clicked 
        signal.
        """
        
        self.close()
     