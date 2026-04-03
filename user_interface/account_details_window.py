"""Defines the AccountDetailsWindow class."""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "<your name here>"

class AccountDetailsWindow(DetailsWindow):
    """Represents a detail window used to display account details and 
    perform bank account transactions.
    """

    balance_updated = Signal(object)

    def __init__(self, account: BankAccount) -> None:
        """Initializes a new instance of the AccountDetailsWindow class.
        
        Args:
            account (BankAccount): The bank account to be displayed.
        """

        super().__init__()

        if isinstance(account, BankAccount):

            # self.account = BankAccount(account.account_number,
            #                             account.client_number,
            #                             account.balance,
            #                             account.date_created)

            self.account = account
            
            # set labels
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # connect buttons
            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)

        else:
            raise TypeError("Invalid type of Bank Account.")

    def on_apply_transaction(self):
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            sender = self.sender()

            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)

            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)


            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.balance_updated.emit(self.account)
        
        except Exception as error:
                QMessageBox.warning(self, f"{transaction_type} Failed",
                    f"{transaction_type} has been failed: {(error)}")

    def on_exit(self):
        self.close()
    
    