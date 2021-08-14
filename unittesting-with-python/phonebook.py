"""Phonebook module."""

class PhoneBook:
    """Phonebook class.
    
    Characteristics:
        - lookup by name
        - raises KeyError on not found lookup
        - consistent when empty
        - consistent when all different
        - inconsistent if has duplicates
        - inconsitent if with duplicate prefix 
    """

    def __init__(self) -> None:
        """Initialize phonebook with a phonebook dictionary."""
        self.phonebook = {}

    def add(self, name:str, number:str) -> None:
        """Add name and number to phonebook"""
        self.phonebook[name] = number

    def lookup(self, name:str) -> str:
        """Return phonebook number for name."""
        return self.phonebook[name]