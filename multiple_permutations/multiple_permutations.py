import itertools


def is_permutation(number):
    for j in range(2, 7):
        if sorted(str(number)) != sorted(str(j * number)):
            return False
    return True


def multiple_permutations():
    iterator = itertools.count(1)
    result = next(i for i in iterator if is_permutation(i))
    print(f"The smallest positive intiger is {str(result)}")


if __name__ == "__main__":
    multiple_permutations()
