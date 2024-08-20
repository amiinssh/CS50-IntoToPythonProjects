import pytest
from numb3rs import validate

def test_valid_ip():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_ip():
    assert validate("256.100.50.25") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("192.168.1.-1") == False
    assert validate("192.168.1.256") == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("192.168.1.a") == False
    assert validate("275.3.6.28") == False
    assert validate("192.168.01.1") == True  

if __name__ == "__main__":
    pytest.main()
