"""A program to demonstrate the use of the BankAccount subclasses.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime

from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.

chequing_account_instances = ChequingAccount(account_number=101,
                                             client_number=1001,
                                             balance=-50.0, 
                                             date_created=date.today(),
                                             overdraft_limit=100.0)

# 3. Print the ChequingAccount created in step 2.

print("Chequing Account (Initial):")
print(chequing_account_instances)

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

print("Chequing Account Service Charges:", 
      chequing_account_instances.get_service_charges())


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.

chequing_account_instances.deposit(100.0)  

# 4b. Print the ChequingAccount

print("\nChequing Account (After Deposit):")
print(chequing_account_instances)

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

print("Chequing Account Service Charges:", 
      chequing_account_instances.get_service_charges()) 

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
 
# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.


print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.

recent_investment_acc = InvestmentAccount(
    account_number=201,
    client_number=2001,
    balance=5000.0,
    date_created=date(date.today().year - 5, 6, 15),  # 5 years ago
    management_fee=50.0 )

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.


# 11a. Print the InvestmentAccount created in step 10.

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
