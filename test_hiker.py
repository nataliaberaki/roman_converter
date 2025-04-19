
import pytest
from hiker import to_roman

#tests if the number is positive
def test_zero_raises_error():
    with pytest.raises(ValueError):
        to_roman(0)

#simple tests
def test_1_to_I():
    assert to_roman(1) == "I"

def test_2_to_II():
    assert to_roman(2) == "II"
    
def test_4_to_IV():
    assert to_roman(4) == "IV"