"""Defines the ClientLookupWindow class."""

from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from client.client import Client


__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "<your name here>"

class ClientLookupWindow(LookupWindow):
    """Represents a main window for looking up BankAccounts.""" 

    def __init__(self):
        """This function is to perform all super class initializations.
        """    

        super().__init__()

        # Calling out the load_data method.
        self.client_listing, self.accounts = load_data()

        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)

    def on_lookup_client(self):
        client_details = self.client_number_edit.text()

        try:
            client_number = int(client_details)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "The client number must be a numeric value.")
            self.reset_display()
            return
    
        if client_number not in self.client_listing:
            self.client_info_label.setText(self, f"Client number:{client_number} not found.")
            self.reset_display()
            return
            
        client = self.client_listing[client_number]

        self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")

        self.account_table.setRowCount(0)

        add_row = 0
        
        for account in self.accounts.values():
            if account.client_number == client_number:

                self.account_table.insertRow(add_row)

                client_account_number = QTableWidgetItem(str(account.account_number))
                client_account_number.setTextAlignment(Qt.AlignCenter)

                client_balance = QTableWidgetItem(f"${account.balance:,.2f}")
                client_balance.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                account_date_created = QTableWidgetItem(str(account.date_created))
                account_date_created.setTextAlignment(Qt.AlignCenter)

                type_of_account = QTableWidgetItem(account.__class__.__name__)
                type_of_account.setTextAlignment(Qt.AlignCenter)

                self.account_table.setItem(add_row, 0, client_account_number)
                self.account_table.setItem(add_row, 1, client_balance)
                self.account_table.setItem(add_row, 2, account_date_created)
                self.account_table.setItem(add_row, 3, type_of_account)

                add_row += 1

        self.account_table.resizeColumnsToContents()

    def on_text_changed(self):
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
    
        user_input = self.account_table.item(row, 0)

        # if item is None:
        #     QMessageBox.warning(self, "Warning", "No account has been selected.")
        #     return
        
        account_number_of_client = user_input.text().strip()
            
        if account_number_of_client == "":
            QMessageBox.warning(self, "Warning", "Please select a valid record.")
            return

        account_number = int(account_number_of_client)

        if account_number not in self.accounts:
            QMessageBox.warning(self, "Warning", "Bank Account selected does not exist.")
            return

        account = self.accounts[account_number]

        dialog = AccountDetailsWindow(account)
        dialog.exec()
        