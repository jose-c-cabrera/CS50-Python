
from plates import is_valid

def test_hello():
    assert is_valid("hello") == True

def test_no_vowels():
    assert is_valid("CS50") == True

def test_mixed_case():
    assert is_valid("50CS") == False

def test_sentence():
    assert is_valid("H0505") == False

def test_numbers_and_symbols():
    assert is_valid("Jose") == True

def test_empty_string():
    assert is_valid("QC1403") == True
