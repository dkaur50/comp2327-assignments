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
__credits__ = "Divjot Kaur"

class ClientLookupWindow(LookupWindow):
    """Represents a main window for looking up BankAccounts.""" 

    def __init__(self):
        """This function is to perform all super class initializations.
        """    

        super().__init__()

        # Calling out the load_data method.
        self.client_listing, self.accounts = load_data()

        # Establishing the three connections here.
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)

    def on_lookup_client(self) -> None:
        """This function is look for the client's account information 
        using client number.
        """

        # Obtaining the client number that has been entered into the 
        # client_number_edit widget.
        client_details = self.client_number_edit.text()

        try:
            client_number = int(client_details)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "The client number must be a numeric value.")
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.warning(self, "Not Found", f"Client number: {client_number} not found.")
            self.reset_display()
            return
            
        client = self.client_listing[client_number]

        self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")

        self.account_table.setRowCount(0)

        add_row = 0
        
        for account in self.accounts.values():
            
            # Below is the case when the client_number matches the key 
            # in the client_listing dictionary.
            if account.client_number == client_number:

                self.account_table.insertRow(add_row)

                # Creating QTableWidgetItems for each of the 
                # account_table columns.
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

        # Below code ensures none of the table is truncated.
        self.account_table.resizeColumnsToContents()
    
    def on_text_changed(self) -> None:
        """This function would act as a slot for the client_number_edit 
        textChanged signal
        """

        # This would remove all existing rows from the dsiplay, leaving 
        # the account table with no data displayed.
        self.account_table.setRowCount(0)

    def update_data(self, account: BankAccount) -> None:
        """This function would update the account information after 
        there are any changes made to the account balances due to a 
        transaction.
        """

        for row in range(self.account_table.rowCount()):

            if int(self.account_table.item(row, 0).text()) == account.account_number:
                
                # This would update the new balance and even align it 
                # accordingly.
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                self.account_table.setItem(row, 1, balance_item)

        self.accounts[account.account_number] = account

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """This function acts as a slot for the account_table 
        cellClicked signal."""
        
        user_input = self.account_table.item(row, 0)

        # This case is possible if the selected account_number does not 
        # reside in the accounts dictionary.
        if  user_input is None or account_number_of_client == "":
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid record.")
            return
 
        account_number_of_client = user_input.text().strip() 
        account_number = int(account_number_of_client)

        if account_number not in self.accounts:
            QMessageBox.warning(self, "No Bank Account", "Bank Account selected does not exist.")
            return

        account = self.accounts[account_number]

        dialog = AccountDetailsWindow(account)
        dialog.balance_updated.connect(self.update_data) 
        dialog.exec()
