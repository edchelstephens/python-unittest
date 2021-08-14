from unittest import TestCase
from unittest import skip

from phonebook import PhoneBook

class PhoneBookTestCase(TestCase):
    """Test case for Phonebook class."""

    def setUp(self) -> None:
        """Run setUp for each test to create a fresh phonebook."""
        self.phonebook = PhoneBook()

    def test_lookup_by_name(self):
        """Phonebook lookup by name returns contact if present."""
        
        name = "Ed"
        number = "123456"

        self.phonebook.add(name, number)
        
        lookup_number = self.phonebook.lookup(name)

        self.assertEqual(lookup_number, number)

    def test_lookup_missing_name_raises_KeyError(self):
        """Not found phonebook name raises KeyError"""

        with self.assertRaises(KeyError):
            self.phonebook.lookup("not there")  
    
    def test_empty_phonebook_is_consistent(self):
        """Empty phonebook is consistent(no duplicates)."""

        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_on_unique_entries(self):
        """Unique entried name and number in phonebook is consistent."""

        self.phonebook.add("Ed", "123")
        self.phonebook.add("Joy", "456")

        self.assertTrue(self.phonebook.is_consistent())


    def test_in_consistent_on_duplicate_number(self):
        """Phonebook with duplicated number is inconsistent."""

        self.phonebook.add("Ed", "123")
        self.phonebook.add("Joy", "123")

        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_on_duplicate_number_prefix(self):
        """Phonebook with a number having a prefix duplicate on another is inconsistent."""

        self.phonebook.add("Ed", "123456")
        self.phonebook.add("Joy", "123")

        self.assertFalse(self.phonebook.is_consistent())

    def test_is_empty_returns_True_on_empty(self):
        """Phonebook is empty when no entries."""

        new_phonebook = PhoneBook()

        self.assertTrue(new_phonebook.is_empty())

    def test_is_empty_returns_False_on_non_empty(self):
        """Phonebook with entries is not empty."""

        self.phonebook.add("Ed", "123")
        self.assertFalse(self.phonebook.is_empty())
    
    def test_has_duplicate_number_returns_False_on_empty_entries(self):
        """Empty entries has no duplicate numbers."""

        empty_phonebook = PhoneBook()

        self.assertFalse(empty_phonebook.has_duplicate_number())

    def test_has_duplicate_number_returns_True_on_duplicated_number(self):
        """has_duplicate_number returns True on duplicated number."""

        self.phonebook.add("Ed", "123")
        self.phonebook.add("Joy", "123")

        self.assertTrue(self.phonebook.has_duplicate_number())
        