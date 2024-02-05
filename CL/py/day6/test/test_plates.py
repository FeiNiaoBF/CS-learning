from plates import is_valid

def test_is_valid_len():
    assert is_valid("CS50") == True
    assert is_valid("Goodbye") == False
    assert is_valid("CS50x") == False
    assert is_valid("CS09a") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
