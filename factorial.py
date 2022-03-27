from math import factorial
from tkinter import W


def findFactorialRecursive(number):
    if number == 0:
        return 1
    return number * findFactorialRecursive(number - 1)


def findFactorialIterative(number):
    factorial = 1
    while number != 0:
        factorial = factorial * number
        number = number - 1
    return factorial


if __name__ == '__main__':
    print(findFactorialIterative(2))
    print(findFactorialRecursive(8))
