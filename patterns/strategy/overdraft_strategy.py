"""This module is for the overdraft strategy which is a part of the 
ServiceChargeStrategy class.
"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0" 

from bank_account.bank_account import BankAccount

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """This class represents the OverdraftStrategy class related to the 
    ServiceChargeStrategy class."""

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """This function is to initialise the class sattributes based 
        on the class diagram.
        """
        
        self._overdraft_limit = overdraft_limit
        
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, balance) -> float:
        """This class calculates service charges.

        Returns:
            balance (float): This represents the calculated service 
            charge.
        """
                
        if balance >= self._overdraft_limit:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE + \
                   (self._overdraft_limit-balance)*self._overdraft_rate
        
        