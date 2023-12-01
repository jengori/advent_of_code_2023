# part 1
def sum_of_calibration_values(lines: list[str]) -> int:
    """takes a list of strings (each string is a line in the calibration
    document) and returns the sum of the calibration values"""
    result = 0

    for line in lines:
        digits_in_line = [char for char in line if char.isnumeric()]
        first_digit = digits_in_line[0]
        last_digit = digits_in_line[-1]
        calibration_value = int("".join([first_digit, last_digit]))
        result += calibration_value

    return result


with open('input.txt') as f:
    my_lines = f.readlines()

print(sum_of_calibration_values(my_lines))
