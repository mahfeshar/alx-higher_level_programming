#!/usr/bin/python3
"""returns the number of characters written"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    count = 0
    with open(filename) as file:
        for line in file:
            count += 1
    return count
