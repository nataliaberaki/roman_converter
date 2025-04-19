
import pytest
from hiker import to_roman

#edge case tests
    #raises error for 0 (not a valid roman numeral)
def test_zero_raises_error():
    with pytest.raises(ValueError):
        to_roman(0)
    
    #raises error for negative numbers (not a valid roman numeral)
def test_negative_number_raises_error():
    with pytest.raises(ValueError):
        to_roman(-1)

#simple tests
def test_1_to_I():
    assert to_roman(1) == "I"

def test_2_to_II():
    assert to_roman(2) == "II"
    
def test_4_to_IV():
    assert to_roman(4) == "IV"

def test_5_to_V():
    assert to_roman(5) == "V"

def test_9_to_IX():
    assert to_roman(9) == "IX"

def test_10_to_X():
    assert to_roman(10) == "X"

#complex cases
def test_1990_to_MCMXC():
    assert to_roman(1990) == "MCMXC"

def test_2023_to_MMXXIII():
    assert to_roman(2023) == "MMXXIII"

def test_3999_to_MMMCMXCIX():
    assert to_roman(3999) == "MMMCMXCIX"     

def test_1987_to_MCMLXXXVII():
    assert to_roman(1987) == "MCMLXXXVII"