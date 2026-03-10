"""This is the module documentation"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

from bank_account.bank_account import BankAccount

from service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ABC):
    """This class represents the OverdraftStrategy."""

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """This function is to initialise the class sattributes based 
        on the class diagram."""
        self.overdraft_limit = overdraft_limit
        self.overdraft_rate = overdraft_rate
        