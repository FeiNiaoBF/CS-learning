import pytest
import jar

def test_jar_class():
    cookie_jar = jar.Jar()
    assert cookie_jar.capacity == 12
    assert cookie_jar.size == 0
    assert type(cookie_jar) == jar.Jar

def test_deposit():
    cookie_jar = jar.Jar()
    cookie_jar.deposit(5)
    assert cookie_jar.size == 5
    cookie_jar.deposit(5)
    assert cookie_jar.size == 10
    with pytest.raises(ValueError):
        cookie_jar.deposit(5)

def test_withdraw():
    cookie_jar = jar.Jar()
    cookie_jar.deposit(5)
    cookie_jar.withdraw(3)
    assert cookie_jar.size == 2
    cookie_jar.withdraw(2)
    assert cookie_jar.size == 0
    with pytest.raises(ValueError):
        cookie_jar.withdraw(1)

def test_str():
    cookie_jar = jar.Jar()
    cookie_jar.deposit(5)
    assert str(cookie_jar) == '🍪🍪🍪🍪🍪'
    cookie_jar.deposit(5)
    assert str(cookie_jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'
    cookie_jar.withdraw(3)
    assert str(cookie_jar) == '🍪🍪🍪🍪🍪🍪🍪'
