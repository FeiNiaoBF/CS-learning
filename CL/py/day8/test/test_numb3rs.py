from numb3rs.numb3rs import validate

def test_validate_T():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_validate_F():
    assert validate("Hello, World!") == False
    assert validate("256.256.256.256") == False
    assert validate("999.999.999.999") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
