"""Module Documentation"""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError

class Client:
    """This is the main class"""
    def __init__(self, client_number, first_name, 
                 last_name, email_address) -> None:
        """This function has been created to initialise the atributes 
        of the class Client.
        
        Args:
            client_number (int): An integer value for representing 
            the client number.
            first_name (str): A string value the client's first name.
            last_name (str): A string value the client's last name.
            email_address (str): A string value the client's 
            email address.
        """

        if type(client_number) != int:
            raise ValueError("The client number should be an integer.")
        self.client_number = client_number

        if first_name.strip() == "":
            raise ValueError("The first_name cannot be blank.")
        self.first_name = first_name
        
        if last_name.strip() == "":
            raise ValueError("The last_name cannot be blank.")
        self.last_name = last_name

        try:
            validate_email(email_address)
        except EmailNotValidError:
            raise ValueError("The email_address is not valid.")
        
        self.__email_address = email_address

    ## Accessor methods:

    def get_client_number(self) -> int:
        """This function represents the unique number of the client.
        
        Returns:
            int: An integer that is the client number.
        """

        return self.__client_number
    
    def get_first_name(self) -> str:
        """This function gets the first name of the client.

        Returns:
            str: A string value which is the client's first name.
        """

        return self.__first_name
    
    def get_last_name(self) -> str:
        """This function is for the client's last name.
        
        Returns:
            str: A string value that is the client's last name."""
        
        return self.__last_name

    def get_email_address(self) -> str:
        """This function is regarding the client's email address.
        
        Returns:
            str: A string value in the form of email address."""
        
        return self.__email_address
    
def __str__(self):
    return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"