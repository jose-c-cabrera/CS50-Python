import pytest
from refueling import convert, gauge


def test_full():
    assert convert("100/100") == 100
    assert gauge(100) == "F"

# def test_no_vowels():
#     assert shorten("rhythm") == "rhythm"

# def test_mixed_case():
#     assert shorten("TwItTeR") == "TwtTR"

# def test_sentence():
#     assert shorten("This is CS50") == "Ths s CS50"

# def test_numbers_and_symbols():
#     assert shorten("email@domain.com") == "ml@dmn.cm"

# def test_empty_string():
#     assert shorten("") == ""
