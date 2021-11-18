import math


def powered_sequence(series_length):
    sum = 0

    for i in range(1, series_length + 1):
        sum += i**i
        # print(i, sum)

    print(f"Last 10 digits of the series with length {series_length} is {str(sum)[-10:]}")


if __name__ == "__main__":
    powered_sequence(10)
    powered_sequence(1000)