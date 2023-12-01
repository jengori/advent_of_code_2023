# part 2

numbers = {'one': '1',
           'two': '2',
           'three': '3',
           'four': '4',
           'five': '5',
           'six': '6',
           'seven': '7',
           'eight': '8',
           'nine': '9'}


def get_first_digit(s):
    """gets the first digit in a string (either numeric character or spelled out in letters)"""
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            return s[i]
        else:
            for number in numbers:
                if s[i:i+len(number)] == number:
                    return numbers.get(number)
        i += 1


def get_last_digit(s):
    """gets the last digit in a string (either numeric character or spelled out in letters)"""
    i = len(s) - 1
    while i >= 0:
        if s[i].isnumeric():
            return s[i]
        else:
            for number in numbers:
                if s[i:i+len(number)] == number:
                    return numbers.get(number)

        i -= 1


def sum_of_calibration_values(lines: list[str]) -> int:
    """takes a list of strings (each string is a line in the calibration
    document) and returns the sum of the calibration values"""
    result = 0

    for line in lines:
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        calibration_value = int("".join([first_digit, last_digit]))
        result += calibration_value

    return result


with open('input.txt') as f:
    my_lines = f.readlines()

print(sum_of_calibration_values(my_lines))
