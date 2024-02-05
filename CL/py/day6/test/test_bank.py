from bank_d import value

def test_value_hundred():
    assert value("Goodbye") == "$100"
    assert value("goodbye") == "$100"


def test_value_zero():
    assert value("hello") == "$0"
    assert value("hello world") == "$0"

def test_value_Tten():
    assert value("h") == "$20"
    assert value("H") == "$20"
    assert value("hi") == "$20"
