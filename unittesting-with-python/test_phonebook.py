from unittest import TestCase

from phonebook import PhoneBook

class PhoneBookTestCase(TestCase):
    """Test case for Phonebook class."""

    def test_lookup_by_name(self):
        """Phonebook lookup by name returns contact if present."""
        
        phonebook = PhoneBook()
        
        name = "Ed"
        number = "123456"
        phonebook.add(name, number)
        
        
        lookup_number = phonebook.lookup(name)

        self.assertEqual(lookup_number, number)

    def test_missing_name(self):
        """Not found phonebook name raises KeyError"""

        phonebook = PhoneBook()

        with self.assertRaises(KeyError):
            phonebook.lookup("not there")