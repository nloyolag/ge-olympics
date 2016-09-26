import multiprocessing
import operator
import os
from functools import reduce


def square(x):
    return x * x


def sum2(x, y):
    return x + y


if __name__ == "__main__":
    squares = list(map(square, range(16)))
    print("Sequential map with squares function", squares)

    squares = list(map(lambda x: x * x, range(16)))
    print("Sequential map with squares lambda", squares)

    cpu_count = os.cpu_count()
    print("CPU count:", cpu_count)
    with multiprocessing.Pool(cpu_count) as pool:
        squares = pool.map(square, range(16))
        print("Parallel map with squares function", squares)

    s = sum(squares)
    print("Using sum function:", s)

    f = list(filter(lambda x: x % 3 == 0, squares[1:]))
    print("Divisible by 3", f)
