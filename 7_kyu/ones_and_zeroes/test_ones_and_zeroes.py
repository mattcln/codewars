import pytest
from ones_and_zeroes import same_length


def test_cases():
    assert same_length("0") == False
    assert same_length("10") == True
    assert same_length("1010") == True
    assert same_length("1001") == False
    assert same_length("101") == False
    assert same_length("110010") == True
    assert same_length("10010") == False
    assert same_length("110") == False
    assert same_length("11001") == False
    assert same_length("1011100010") == True
    assert same_length("11100011000") == False
    assert same_length("11101010010010") == False
    assert same_length("00110100001111") == False
    assert same_length("1100111000100") == False
    assert same_length("00110011100010") == False
