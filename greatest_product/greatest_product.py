import os
from functools import reduce


def greatest_product(adjacent_length):
    file_path = os.path.join(os.path.dirname(__file__), 'thousand_digit_input.txt')
    f = open(file_path, 'r')
    thousand_digit_number = f.read()
    thousand_digit_number = thousand_digit_number.replace("\n", "")

    digits = None
    largest_product = 1

    for i in range(0, len(thousand_digit_number) - adjacent_length + 1):
        product = reduce(lambda x, y: int(x) * int(y), thousand_digit_number[i: i + adjacent_length])

        if product > largest_product:
            largest_product = product
            digits = int(thousand_digit_number[i: i + adjacent_length])

    print(f"Adjacent {adjacent_length} digits with largest product are: {digits}")
    print(f"Product: {largest_product}")


if __name__ == "__main__":
    greatest_product(4)
    greatest_product(13)
