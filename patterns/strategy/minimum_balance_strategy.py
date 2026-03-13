"""This module is for the MinimumBalanceStrategy class related to the 
ServiceChargeStrategy class.
"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """This class is for the MinimumBalancesStrategy class related to the 
    ServiceChargeStrategy class.
    """

    # Declaring the constant.
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance):
        """This function is for initializing the attributes of 
        MinimumBalanceStrategy class."""

        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, balance) -> float:
        """This class calculates service charges.

        Returns:
            balance (float): This represents the calculated service 
            charge.
        """

        if balance >= self._minimum_balance:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE

        return ServiceChargeStrategy.BASE_SERVICE_CHARGE * MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM
     