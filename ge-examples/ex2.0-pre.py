import multiprocessing
import operator
import os
import functools


def square(x):
    return x * x


def sumxy(x, y):
    return x + y


if __name__ == "__main__":
    squares = list(map(square, range(16)))
    print("Sequential map with squares function", squares)

    squares = list(map(lambda x: x * x, range(16)))
    print("Sequential map with squares lambda", squares)

    s = functools.reduce(sumxy, squares)
    print("Reduced with sum2 function:", s)

    s = functools.reduce(operator.add, squares[1:])
    print("Reduced with operator.add:", s)

    s = sum(squares)
    print("Using sum function:", s)

    f = list(filter(lambda x: x % 3 == 0, squares[1:]))
    print("Divisible by 3", f)

    add10 = functools.partial(sumxy, 10)
    s = list(map(add10, range(16)))
    print("Partial function sumxy(10,y)", s)
