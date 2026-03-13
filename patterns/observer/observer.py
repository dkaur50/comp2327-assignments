"""This module represents the Observer superclass which will be used to 
define the interface for all concrete observers that need to be notified 
of changes in the subject."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """This class is a superclass responsible for defining the interface 
    for all the concrete observers that need to be notified of changes 
    in the subject.
    """
 
    def update(self, message: str):
        """This function is reuired to be implemented in the concrete 
        classes to notify observers when there are changes in the 
        subject.

        Returns:
            message (str): The message or data sent by the subject to 
            the observer.
        """
        pass
    