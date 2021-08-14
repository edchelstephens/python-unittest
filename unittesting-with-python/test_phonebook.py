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
    
    @skip("INCOMPLETE")
    def test_empty_phonebook_is_consistent(self):
        """Test phonebook consistency on unqiue name to number recording."""

        self.assertTrue(self.phonebook.is_consistent())