"""This module is for the MinimumBalanceStrategy class"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from strategy.service_charge_strategy import ServiceChargeStrategy
 
class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy used to calculate service charges for Savings accounts.
    """

    SERVICE_CHARGE_PREMIUM = 2.00

    def __init__(self, minimum_balance):
        """
        Initializes the MinimumBalanceStrategy object.

        Parameters
        ----------
        minimum_balance : float
            The minimum required balance.
        """

        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, balance):
        """
        Calculates service charges based on minimum balance rules.

        Parameters
        ----------
        balance : float
            The current account balance.

        Returns
        -------
        float
            The calculated service charge.
        """

        if balance >= self._minimum_balance:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE

        return ServiceChargeStrategy.BASE_SERVICE_CHARGE + MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM
    
