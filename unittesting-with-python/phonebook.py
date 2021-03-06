"""Phonebook module."""

import os

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

    def __init__(self, cache_directory=None) -> None:
        """Initialize phonebook with a phonebook dictionary and new phonebook file."""
        self.phonebook = {}

        if cache_directory is not None: 
            self.filename = os.path.join(cache_directory, "phonebook.txt")
            self.cache = open(self.filename, "w")
        else:
            self.cache = None

    def add(self, name:str, number:str) -> None:
        """Add name and number to phonebook"""
        self.phonebook[name] = number

    def lookup(self, name:str) -> str:
        """Return phonebook number for name."""
        return self.phonebook[name]

    def clear(self):
        """clear the cached phonebook."""
        if self.cache is not None:
            self.cache.close()
            os.remove(self.filename)

    def count(self):
        """Return number of entries on phonebook."""
        return len(self.phonebook.items())

    def is_empty(self):
        """Check if phonebook is empty."""
        return self.count() == 0


    def has_duplicate_number(self):
        """Check if phonebook has duplicated number entry."""

        numbers = self.phonebook.values()
        unique_numbers = set(numbers)

        return len(numbers) > len(unique_numbers)
    
    def has_duplicated_number_prefix(self):
        """Check if a number is a prefix to another entry on phonebook."""

        if self.is_empty():
            duplicated = False
        elif self.has_duplicate_number():
            duplicated = True
        else:
            numbers = set(self.phonebook.values())

            duplicated = any([
                compared_number.startswith(number) for number in numbers for compared_number in numbers if number != compared_number
            ])

        return duplicated
            

    def is_consistent(self) -> bool:
        """Check if phonebook is consistent or correct with unique entries."""
        
        consistent = self.is_empty() or all([
            not self.has_duplicate_number(),
            not self.has_duplicated_number_prefix()
        ])
 
        return consistent

    def get_names(self) -> list:
        """Return list of names on phonebook."""

        return list(self.phonebook.keys())

    def get_numbers(self):
        """Return list of numbers on phonebook."""

        return list(self.phonebook.values())
    
        
    def is_singular(self):
        """Check if phonebook only has 1 entry."""

        return self.count() == 1