import pytest

from phonebook import PhoneBook

@pytest.fixture
def phonebook(tmpdir):
    """Pytest fixture to create a fresh empty phonebook."""
    return PhoneBook(tmpdir)
  

def test_lookup_by_name(phonebook):
    """Name lookup returns number on phonebook when present."""

    phonebook.add("Ed", "123")
    
    assert "123" == phonebook.lookup("Ed")

@pytest.mark.slow
def test_phonebook_contains_all_names(phonebook):
    """Phonebook contains all names."""

    phonebook.add("Ed", 123)

    assert "Ed" in phonebook.get_names()

@pytest.mark.skip("To be changed")
def test_missing_phonebook_lookup_raises_error(phonebook):
    """missing name lookup on phonebook raises KeyError"""

    with pytest.raises(KeyError):
        phonebook.lookup("Ed")

def test_is_singular_returns_False_on_empty(phonebook):
    """is_singular() returns False on empty phonebook."""

    assert phonebook.is_singular() == False

def test_is_singular_retunrs_True_on_single_entry(phonebook):
    """is_singular() returns True on single entry phonebook."""

    phonebook.add("Ed", "123")

    assert phonebook.is_singular() == True

def test_is_singular_returns_False_on_multiple_entry(phonebook):
    """is_singular() is False on multiple entry."""

    phonebook.add("Ed", "123")
    phonebook.add("Joy", "456")

    assert phonebook.is_singular() == False

def test_count_returns_0_on_empty(phonebook):
    """count() returns 0 on no entry phonebook."""

    assert phonebook.count() == 0

def test_count_returns_exact_number_of_entries_on_non_empty(phonebook):
    """count() returns 0 on no entry phonebook."""

    phonebook.add("Ed", "123")
    phonebook.add("Joy", "456")

    assert phonebook.count() == 2