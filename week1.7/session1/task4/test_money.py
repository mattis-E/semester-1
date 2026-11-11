# Week 1.7, Session 1: Task 4 - unit tests for methods in Money

import pytest

from money import Money

# test that an exception will be raised with an invalid pounds value.
def test_invalid_type_pound():
    with pytest.raises(TypeError) as excinfo:
        Money(1.2, 99)
    assert str(excinfo.value) == "pounds must be an integer"

# test that an exception will be raised with an invalid pounds value.
def test_invalid_value_pound():
    with pytest.raises(ValueError) as excinfo:
        Money(-1, 0)
    assert str(excinfo.value) == "pounds must be >= 0"

# test that an ecxeption will be raised with an invalid operation on a Money object.
def test_add_invalid_type():
    m1 = Money(5, 0)
    with pytest.raises(TypeError) as excinfo:
        m1 + 42
    assert str(excinfo.value) == "other object must be a Money"

# test that an exception will be raised for an invalid pence type.
def test_invalid_type_pence():
    with pytest.raises(TypeError) as excinfo:
        m1 = Money(5, "abc")
    assert str(excinfo.value) == "pence must be an integer"
    
# test that an exception will be raised for an invalid pence value.
def test_invalid_value_pence():
    with pytest.raises(ValueError) as excinfo:
        m1 = Money(10, -50)
    assert str(excinfo.value) == "pence must be in range 0-99"
    
# test that two MOney objects can be added together.
def test_valid_add():
    m1 = Money(10, 10)
    m2 = Money(10, 90)
    assert str(m1 + m2) == str(Money(21, 0))

    m3 = Money(0, 50)
    m4 = Money(1, 50)
    assert str(m3 + m4) == str(Money(2, 0))