from bank import value


def test_Hi ():
    assert value("Hi") == int(20)

def test_hola ():
    assert value("hola") == int(20)

def test_my_friend ():
    assert value("my friend") == int(100)

def test_Hello ():
    assert value("Hello") == int(0)

def test_hello ():
    assert value("hello") == int(0)

