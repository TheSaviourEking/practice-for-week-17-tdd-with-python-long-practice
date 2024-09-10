def parse(value):
    value_dict = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9
    }

    return value_dict[value] if value_dict[value] else None
