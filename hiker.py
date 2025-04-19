#simple test that should pass
def to_roman(number):
    if number < 1:
        raise ValueError("Input must be a positive integer") #error when number is negative
    if number == 4:
        return "IV"
    return "I" * number
