"""A program to demonstrate the use of the BankAccount subclasses.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime

from datetime import date
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.

chequing_account_instances = ChequingAccount(account_number=101,
                                             client_number=1001,
                                             balance=-50.0, 
                                             date_created=date.today(),
                                             overdraft_limit=100.0,
                                             overdraft_rate=0.05)

# 3. Print the ChequingAccount created in step 2.

print("\nChequing Account (Initial):")
print(chequing_account_instances)

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

print("\nChequing Account Service Charges:", 
      chequing_account_instances.get_service_charges())
 
# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.

try:
    chequing_account_instances.deposit(200.0)
except ValueError as error:
    print(error)

# 4b. Print the ChequingAccount

print("\nChequing Account (After Deposit):")
print(chequing_account_instances)

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

print("\nChequing Account Service Charges:", 
      chequing_account_instances.get_service_charges()) 

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.

savings_account_instance = SavingsAccount(account_number=102,
                                          client_number=1002,
                                          balance=1000.0,
                                          date_created=date.today(),
                                          minimum_balance=500.0)

# 6. Print the SavingsAccount created in step 5.

print("\nSavings Account (Initial):")
print(savings_account_instance)

# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

print("\nSavings Account Service Charges:",
      savings_account_instance.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.

try:
    savings_account_instance.withdraw(600.0)
except ValueError as exception:
    print(exception)

# 7b. Print the SavingsAccount.

print("\nSavings Account (After Withdraw):")
print(savings_account_instance)

# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

print("\nSavings Account Service Charges:",
      savings_account_instance.get_service_charges())

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.

investment_account_last_ten_years = InvestmentAccount(
                                          account_number=201,
                                          client_number=2001,
                                          balance=5000.0,
                                          date_created=date(
                                              date.today().year - 5,6,15),
                                          management_fee=50.0)

# 9a. Print the InvestmentAccount created in step 8.

print("\nInvestment Account (Recent):")
print(investment_account_last_ten_years)

# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.

print("\nInvestment Account Service Charges:",
      investment_account_last_ten_years.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.

investment_account_prior_ten_years = InvestmentAccount(
                                                account_number=202,
                                                client_number=2002,
                                                balance=7000.0,
                                                date_created=date(
                                                    date.today().year - 15,6,15),
                                                management_fee=50.0)


# 11a. Print the InvestmentAccount created in step 10.

print("\nInvestment Account (Older than 10 years):")
print(investment_account_prior_ten_years)

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.

print("\nInvestment Account Service Charges:",
      investment_account_prior_ten_years.get_service_charges())

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.

for account in [chequing_account_instances,
                savings_account_instance,
                investment_account_last_ten_years,
                investment_account_prior_ten_years]:
    try:
        account.withdraw(account.get_service_charges())
    except ValueError as new_error:
        print(new_error)

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

print("\nChequing Account (After Service Charges Deducted):")
print(chequing_account_instances)

print("\nSavings Account (After Service Charges Deducted):")
print(savings_account_instance)

print("\nInvestment Account (Recent - After Service Charges Deducted):")
print(investment_account_last_ten_years)

print("\nInvestment Account (Old - After Service Charges Deducted):")
print(investment_account_prior_ten_years)
