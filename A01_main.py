""""A program written to demonstrate the use of the BankAccount and 
Client classes.
"""

from bank_account.bank_account import BankAccount
from client.client import Client

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Divjot Kaur"

def main():
    """The main function."""

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  When exceptions are 
    # 'caught', display the exception message to the console.

    # 1. Code a statement which creates a valid instance of the Client 
    # class.
    # - Use your own unique valid values for the inputs to the class.
    
    try:
        client = Client(2001, "Div", "Kaur", "div.kaur@pixellriver.com")
    except ValueError as error:
        print(error)

    # 2. Declare a variable used to store a BankAccount object and 
    # initialize the variable as None and it would be defined later on.
    
    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a 
    # statement to instantiate the BankAccount object.
    # - Use any integer value for the BankAccount number.
    # - Use the client_number used to create the Client object in step 1 
    # for the BankAccount's client_number. 
    # - Use a floating point value for the balance.

    try:
        bank_account = BankAccount(3001, client.client_number, 500.75)
    except ValueError as second_error:
        print(second_error)

    # 4. Code a statement which creates an instance of the BankAccount 
    # class.
    # - Use any integer value for the BankAccount number.
    # - Use the client_number used to create the Client object in step 1
    # for the BankAccount's client_number. 
    # - Use an INVALID value (non-float) for the balance.

    try:
        invalid_account = BankAccount(3002, client.client_number, "invalid")
    except ValueError as third_error:
        print(third_error)

    # 5. Code a statement which prints the Client instance created in 
    # step 1. 
    # Code a statement which prints the BankAccount instance created in
    # step 3.

    print(client)
    print(bank_account)

    # 6. Attempt to deposit a non-numeric value into the BankAccount 
    # create in step 3. 

    try:
        bank_account.deposit("abc")
    except ValueError as fourth_error:
        print(fourth_error)

    # 7. Attempt to deposit a negative value into the BankAccount create
    # in step 3. 

    try:
        bank_account.deposit(-50)
    except ValueError as fifth_error:
        print(fifth_error)

    # 8. Attempt to withdraw a valid amount of your choice from the 
    # BankAccount create in step 3. 

    try:
        bank_account.withdraw(100.25)
    except ValueError as sixth_error:
        print(sixth_error)

    # 9. Attempt to withdraw a non-numeric value from the BankAccount 
    # create in step 3. 

    try:
        bank_account.withdraw("xyz")
    except ValueError as seventh_error:
        print(seventh_error)


    # 10. Attempt to withdraw a negative value from the BankAccount 
    # create in step 3. 

    try:
        bank_account.withdraw(-20)
    except ValueError as eighth_error:
        print(eighth_error)

    # 11. Attempt to withdraw a value from the BankAccount create in 
    # step 3 which exceeds the current balance of the account. 
 
    try:
        bank_account.withdraw(10000)
    except ValueError as nine_error:
        print(nine_error)

    # 12. Code a statement which prints the BankAccount instance created
    # in step 3.  

    print(bank_account)

if __name__ == "__main__":
    main()
