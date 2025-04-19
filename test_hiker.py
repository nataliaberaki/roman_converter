from hiker import to_roman

#simple tests
def test_1_to_I():
    assert to_roman(1) == "I"

def test_2_to_II():
    assert to_roman(2) == "II"
    
def test_4_to_IV():
    assert to_roman(4) == "IV"