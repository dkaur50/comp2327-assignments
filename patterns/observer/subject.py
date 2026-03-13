"""This module contains the Subject class that is responsible for 
maintaining a list of its observers and notifying them of state changes 
or events."""

from abc import ABC, abstractmethod

from .observer import Observer

class Subject(ABC):
    """This class is responsible for maintaining a list of its 
    observers and notifying them of state changes or events."""

    def __init__(self):
        """This function is for initialization of the attributes."""
        
        # Creating an empty list for now, so that the observers list 
        # can be stored.
        self._observers = []

    def attach(self, observer: Observer):
        """This function represents attach method for the observers.

        Returns:
            observer (Observer): The observer to be added.
        """
        
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """This function represents detach method for the observers.

        Returns:
            observer (Observer): The observer to be removed.
        """

        if observer in self._observers:
            self._observers.remove(observer)

    @abstractmethod
    def notify(self, message: str):
        """This function is to notify all observers about any change.
        
        Returnd:
            message (str): The message to notify the observers.
        """
        
        pass
