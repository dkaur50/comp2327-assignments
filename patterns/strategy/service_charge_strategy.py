"""This is the main module for strategy which contains the 
ServiceChargeStrategy class which is linked to all the other strategy 
classes."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """This class represents the ServiceChargeStrategy."""

    # Declaring the constant.
    BASE_SERVICE_CHARGE = 0.50

    def calculate_service_charges(self, account: BankAccount,
                                  BASE_SERVICE_CHARGE: float= 0.50):
        """This class calculates the service charges."""

        pass
