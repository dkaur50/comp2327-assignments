"""This is the module documentation"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from datetime import date, timedelta

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """This class if for the ManagementFeeStrategy"""
    
    TEN_YEARS_AGO = date.today() - timedelta(days=10*365.25)

    def __init__(self, balance, date_created, management_fee):
        """Initialize attributes for the strategy."""
        self._balance = balance
        self._date_created = date_created
        self._management_fee = management_fee

    def calculate_service_charges(self):
        """Calculate service charges based on account age."""
        if self._date_created <= ManagementFeeStrategy.TEN_YEARS_AGO:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        return ServiceChargeStrategy.BASE_SERVICE_CHARGE + self._management_fee
    