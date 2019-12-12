"""This is a module level docstring.

This module is an example of idiomatic Python code.
"""

__version__ = "0.0.1"
__author__ = "Zac Slade"

from typing import Tuple


def getAuthor() -> str:
    """The function foo takes no argument and returns a string"""
    return __author__


def addTwoNumbers(x: int, y: int) -> int:
    """This trivial function adds two integers and returns the result"""
    return x + y


class ExampleClass:
    """An example class to show some basics"""

    pair: Tuple[int, int]

    def __init__(self, p: Tuple[int, int]):
        """The instance initializer for ExampleClass"""
        self.pair = p

    def __new__(cls, p: Tuple[int, int]):
        """The class level, static, method will call __init__ if a class instance is returned"""
        return super(ExampleClass, cls).__new__(cls)

    def __str__(self) -> str:
        """The stringifier for the class"""
        x, y = self.pair
        return "Pair (x={}, y={})".format(x, y)


def a_custom_main():
    """This toy main function takes no arguments and returns no values"""
    [print(ExampleClass((p[0], p[1]))) for p in zip(range(10), range(10))]


if __name__ == "__main__":
    """The initialization of a Python program should live here"""
    # Do setup here
    a_custom_main()
