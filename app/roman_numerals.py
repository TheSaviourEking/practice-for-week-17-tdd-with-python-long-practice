def parse(roman_numeral):
    numerals_to_number_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    number = 0
    i = 0

    while i < len(roman_numeral):
        if i + 1 < len(roman_numeral) and roman_numeral[i:i+2] in numerals_to_number_dict:
            # If the next two characters form a valid Roman numeral
            number += numerals_to_number_dict[roman_numeral[i:i+2]]
            i += 2
        else:
            # else, it's a single character Roman numeral
            number += numerals_to_number_dict[roman_numeral[i]]
            i += 1

    return number
