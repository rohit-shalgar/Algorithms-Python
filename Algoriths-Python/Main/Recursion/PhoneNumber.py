import string

phone_numbers = []


def get_phone_numbers(phone_number: string):
    current_number_combination = ["0"] * len(phone_number)
    phone_numbers_calculator(current_number_combination, 0, phone_number)
    return phone_numbers


def phone_numbers_calculator(current_number_combination, idx, phone_number: string):
    if idx == len(phone_number):
        phone_numbers.append("".join(current_number_combination))
    else:
        number = phone_number[idx]
        numbers_data = PHONE_NUMBER_DATA[number]
        for elem in numbers_data:
            current_number_combination[idx] = elem
            phone_numbers_calculator(current_number_combination, idx + 1, phone_number)


PHONE_NUMBER_DATA = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
