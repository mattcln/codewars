# https://www.codewars.com/kata/650a86e8404241005fc744ca
from itertools import groupby


def is_first_number_0(numbers) -> bool:
    return True if numbers[0] == "0" else False


def is_correct(numbers) -> bool:
    numbers_group = groupby(numbers)
    result = [(label, sum(1 for _ in group)) for label, group in numbers_group]
    if len(result) % 2 == 0:
        for _ in range(0, len(result), 2):
            if result[_][1] != result[_ + 1][1]:
                return False
    else:
        return False
    return True


def same_length(txt):
    if is_first_number_0(txt):
        return False
    return is_correct(txt)
