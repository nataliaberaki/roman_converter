def to_roman(number):
    if number < 1:
        raise ValueError("Input must be a positive integer")
        #does not allow negative numbers
    
    #conversion table from integer value to roman numeral symbol
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    
    converted = "" #final string

    #loops the list of value/numeral pairs
    for value, numeral in roman_numerals:
        #removes value from number and adds corresponding roman numeral
        while number >= value:
            converted += numeral # Adds corresponding Roman numeral
            number -= value  # Subtracts the value from the number
    return converted #returns the roman numeral fully converted