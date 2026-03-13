"""This is the obeserver module."""

__author__ = "Divjot Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """Abstract base class for observers in the Observer Pattern."""

    @abstractmethod
    def update(self, message: str):
        """
        Notify the observer of a change in the subject.

        Args:
            message (str): The message or data sent by the subject to the observer.
        """
        pass