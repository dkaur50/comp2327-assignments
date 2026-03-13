"""This is the module documentation"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

from bank_account.bank_account import BankAccount

from service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy used to calculate service charges for Investment accounts.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_creation_date):
        """
        Initializes the ManagementFeeStrategy object.

        Parameters
        ----------
        account_creation_date : date
            The date when the account was created.
        """

        self._account_creation_date = account_creation_date

    def calculate_service_charges(self, balance):
        """
        Calculates service charges based on account age.

        Parameters
        ----------
        balance : float
            The current account balance.

        Returns
        -------
        float
            The calculated service charge.
        """

        if self._account_creation_date <= ManagementFeeStrategy.TEN_YEARS_AGO:
            return 0.0

        return ServiceChargeStrategy.BASE_SERVICE_CHARGE