#!/usr/bin/python3
"""Funtion that adds 2 integers"""

def add_integer(a, b=98):
    """Return the addition of a and b
    Float should be casted to integers
    Raises:
        TypeError: If a or b is a non-integer or non float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))