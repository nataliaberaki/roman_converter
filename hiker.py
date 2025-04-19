def to_roman(number):
    if number < 1:
        raise ValueError("Input must be a positive integer") #error when number is negative

    # Integer values
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    # Roman numeral symbols
    num = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    converted = ""  # Final string
    i = 0  # Index of val and num lists

    while number > 0:
        for _ in range(number // val[i]):
            converted += num[i]  # Adds corresponding Roman numeral
            number -= val[i]  # Subtracts the value from the number
        i += 1  # Moves to the next value
        if i == len(val):  # Prevents index out of range
            break
    
    return converted  # Return the final result