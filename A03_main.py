"""A program to demonstrate your understanding of the Observer Pattern.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "<your name here>"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account.chequing_account import ChequingAccount

from bank_account.savings_account import SavingsAccount

from bank_account.investment_account import InvestmentAccount

from datetime import date

from client.client import Client

# 2. Create a Client object with data of your choice.

first_client = Client(1, "Anne", "Clinton", "Anneclinton@xyz.com")

# 3a. Create a ChequingAccount object with data of your choice, using 
#   the client_number of the client created in step 2.

first_client_chequing = ChequingAccount(1001, first_client.client_number, 
                                       500.0, date.today(), -200.0, 0.05
                                       )

# 3b. Create a SavingsAccount object with data of your choice, using the
#   client_number of the client created in step 2.

first_client_savings = SavingsAccount(2001, first_client.client_number, 
                                      800.0,date.today(), 100.0)

# 4. The ChequingAccount and SavingsAccount objects are 'Subject' 
# objects. The Client object is an 'Observer' object.  
# 4a. Attach the Client object (created in step 1) to the 
#   ChequingAccount object (created in step 2).

first_client_chequing.attach(first_client)

# 4a. Attach the Client object (created in step 1) to the 
#   SavingsAccount object (created in step 2).

first_client_savings.attach(first_client)

# 5a. Create a second Client object with data of your choice.

second_client = Client(1, "Bob", "Frank", "Bobfrank@mno.com")

# 5b. Create a SavingsAccount object with data of your choice, using the
#   client_number of the client created in this step.

second_client_savings = SavingsAccount(1002, second_client.client_number, 
                                      600.0,date.today(), 100.0)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and 
# withdraws) which would cause the Subject (BankAccount) to notify the 
# Observer (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.

# First Client:

# Chequing Account:
try:
    first_client_chequing.deposit(50.0)
except ValueError as first_error:
    print(first_error)

try:
    first_client_chequing.withdraw(510.0)
except ValueError as second_error:
    print(second_error)

try:
    first_client_chequing.withdraw(20.0)
except ValueError as third_error:
    print(third_error)

# Savings Account:
try:
    first_client_savings.deposit(50.0)
except ValueError as fourth_error:
    print(fourth_error)

try:
    first_client_savings.withdraw(800.0)
except ValueError as fifth_error:
    print(fifth_error)

try:
    first_client_savings.withdraw(25.0)
except ValueError as sixth_error:
    print(sixth_error)

# Second Client:

# Savings Account:
try:
    second_client_savings.deposit(50.0)
except ValueError as seventh_error:
    print(seventh_error)

try:
    second_client_savings.withdraw(600.0)
except ValueError as eight_error:
    print(eight_error)

try:
    second_client_savings.deposit(10.0)
except ValueError as ninth_error:
    print(ninth_error)

print(first_client_chequing)

print(first_client_savings)

print(second_client_savings)

# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
