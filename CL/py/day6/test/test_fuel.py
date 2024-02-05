import fuel

def test_convert():
    assert fuel.convert("1/2") == 0.5
    assert fuel.convert("3/4") == 0.75
    assert fuel.convert("5/8") == 0.625
    assert fuel.convert("4/0") == "Invalid input!"
    assert fuel.convert("3") == "Invalid input!"
    assert fuel.convert("3/4/5") == "Invalid input!"

def test_gauge():
    assert fuel.gauge(100) == 'F'
    assert fuel.gauge(50) == '50%'
    assert fuel.gauge(0) == 'E'
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(1) == 'E'
