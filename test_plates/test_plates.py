
from plates import is_valid

def test_hello():
    assert is_valid("hello") == True

def test_CS50():
    assert is_valid("CS50") == True

def test_numbers_first():
    assert is_valid("50CS") == False

def test_zero_first():
    assert is_valid("H0505") == False

def test_name():
    assert is_valid("Jose") == True

def test_normal_plate():
    assert is_valid("QC1403") == True
