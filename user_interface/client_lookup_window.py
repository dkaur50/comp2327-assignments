"""Defines the ClientLookupWindow class."""

from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

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
        self.client_listing, self.accounts = self.load_data()

        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)