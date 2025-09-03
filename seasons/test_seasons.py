from seasons import transform
import pytest

def test_invalid_month():
    with pytest.raises(SystemExit):
        transform("2000-31-31")
def test_invalid_day():
    with pytest.raises(SystemExit):
        transform("2000-08-32")

def test_invalid_year():
    with pytest.raises(SystemExit):
        transform("200-08-32")

def test_invalid_everything():
    with pytest.raises(SystemExit):
        transform("200-18-32")

def test_invalid_format():
    with pytest.raises(SystemExit):
        transform("January 1, 1999")

def test_invalid_future():
    with pytest.raises(SystemExit):
        transform("2300-01-01")
