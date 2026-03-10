"""Module Documentation"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """This class has been created to the service charge strategy."""

    def calculate_service_charges(self, account: BankAccount,
                                  BASE_SERVICE_CHARGE: float= 0.50):

        pass
