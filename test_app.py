from app import add, subtract

def test_add_success():
    assert add(1, 2) == 3

def test_add_zero():
    assert add(0, 0) == 0

def test_subtract_success():
    assert subtract(5, 2) == 3
