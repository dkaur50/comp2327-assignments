"""This is the module documentation"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0" 

from bank_account.bank_account import BankAccount

from service_charge_strategy import ServiceChargeStrategy

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """This class represents the OverdraftStrategy."""

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """This function is to initialise the class sattributes based 
        on the class diagram."""
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, balance):
        if balance >= self._overdraft_limit:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE + \
                   (self._overdraft_limit-balance)*self._overdraft_rate
        