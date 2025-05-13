import pytest
from refueling import convert, gauge


def test_full():
    assert convert("100/100") == 100
    assert gauge(100) == "F"

def test_empty():
    assert convert("0/100") == 0
    assert gauge(0) == "E"


def test_half():
    assert convert("1/2") == 50
    assert gauge(50) == "50%"


def test_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_near_full():
    assert gauge(99) == "F"
    assert gauge(98) == "98%"


def test_near_empty():
    assert gauge(1) == "E"
    assert gauge(2) == "2%"


def test_invalid_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_invalid_fraction_order():
    with pytest.raises(ValueError):
        convert("3/2")


def test_non_integer_input():
    with pytest.raises(ValueError):
        convert("cat/dog")

