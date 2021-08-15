from phonebook import PhoneBook

def test_lookup_by_name():
    """Name lookup returns number on phonebook when present."""
    phonebook = PhoneBook()
    phonebook.add("Ed", "123")
    
    assert "123" == phonebook.lookup("Ed")