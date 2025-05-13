
from plates import is_valid

def test_hello():
    assert is_valid("AA") == True

def test_CS50():
    assert is_valid("A2") == False

def test_numbers_first():
    assert is_valid("2A") == False

def test_zero_first():
    assert is_valid("22") == False

def test_name():
    assert is_valid(" 2") == False
