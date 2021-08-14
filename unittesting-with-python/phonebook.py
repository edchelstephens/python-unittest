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

    def is_empty(self):
        """Check if phonebook is empty."""
        return len(self.phonebook.items()) == 0


    def has_duplicate_number(self):
        """Check if phonebook has duplicated number entry."""

        numbers = self.phonebook.values()
        unique_numbers = set(numbers)

        return len(numbers) > len(unique_numbers)


    def is_consistent(self):
        """Check if phonebook is consistent or correct with unique entries."""
        
        consistent = self.is_empty() or not self.has_duplicate_number()

        return consistent

    
        