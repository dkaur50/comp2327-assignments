"""This module is for the MinimumBalanceStrategy class"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
 
class MinimumBalanceStrategy(ServiceChargeStrategy):
    """ This class is for the MinimumBalancesStrategy."""

    SERVICE_CHARGE_PREMIUM = 2.00

    def __init__(self, minimum_balance):
        """ This class if for initializing the attributes of 
        MinimumBalanceStrategy."""

        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, balance):
        """This class calculates service charges.

        Returns:
            balance: The calculated service charge.
        """

        if balance >= self._minimum_balance:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE

        return ServiceChargeStrategy.BASE_SERVICE_CHARGE + MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM
    
