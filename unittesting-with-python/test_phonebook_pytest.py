import pytest

from phonebook import PhoneBook

def test_lookup_by_name():
    """Name lookup returns number on phonebook when present."""
    
    phonebook = PhoneBook()
    phonebook.add("Ed", "123")
    
    assert "123" == phonebook.lookup("Ed")

def test_phonebook_contains_all_names():
    """Phonebook contains all names."""

    phonebook = PhoneBook()
    phonebook.add("Ed", 123)

    assert "Ed" in phonebook.get_names()


def test_missing_phonebook_lookup_raises_error():
    """missing name lookup on phonebook raises KeyError"""

    phonebook = PhoneBook()
    
    phonebook.add("Ed", 123)
    with pytest.raises(KeyError):
        phonebook.lookup("Ed")