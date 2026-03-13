"""This is the module documentation for the ManagementFeeStrategy class 
that relates to the ServiceChargesStrategy class."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from datetime import date, timedelta

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """This class of for the ManagementFeeStrategy that relates to the 
    ServiceChargesStrategy class."""
    
    # Declaring the constant.
    TEN_YEARS_AGO = date.today() - timedelta(days=10*365.25)

    def __init__(self, balance, date_created, management_fee):
        """This function is for initialising the attributes of the 
        ManageFeeStrategy class.
        """
        
        self._balance = balance
        
        self._date_created = date_created
        
        self._management_fee = management_fee

    def calculate_service_charges(self):
        """This function is responsible for calculating the service 
        charges.
        """
        
        if self._date_created <= ManagementFeeStrategy.TEN_YEARS_AGO:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        
        return ServiceChargeStrategy.BASE_SERVICE_CHARGE + self._management_fee
    