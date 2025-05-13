
from plates import is_valid

def test_hello():
    assert is_valid("AA") == True

def test_correct():
    assert is_valid("JHW20") == True

def test_CS50():
    assert is_valid("??") == False

def test_AAA():
    assert is_valid("???AAA") == False

def test_numbers_first():
    assert is_valid("AAA???") == False

def test_zero_first():
    assert is_valid("22") == False

def test_name():
    assert is_valid(" 2") == False

def test_lots_of_num():
    assert is_valid("ASFAGWE46") == False

def zero_name():
    assert is_valid("") == False
