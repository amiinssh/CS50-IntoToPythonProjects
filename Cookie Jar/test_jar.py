import pytest
from jar import Jar


def test_initial_capacity():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_default_capacity():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_deposit_valid():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5


def test_deposit_exceed_capacity():
    jar = Jar(10)
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw_valid():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2


def test_withdraw_exceed_size():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)


def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("ten")


def test_invalid_deposit_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
